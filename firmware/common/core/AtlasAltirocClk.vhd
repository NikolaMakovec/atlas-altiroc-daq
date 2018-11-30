-------------------------------------------------------------------------------
-- File       : AtlasAltirocClk.vhd
-- Company    : SLAC National Accelerator Laboratory
-------------------------------------------------------------------------------
-- Description: PLL Wrapper and external 160 MHz clock MUX
-------------------------------------------------------------------------------
-- This file is part of 'ATLAS ALTIROC DEV'.
-- It is subject to the license terms in the LICENSE.txt file found in the 
-- top-level directory of this distribution and at: 
--    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html. 
-- No part of 'ATLAS ALTIROC DEV', including this file, 
-- may be copied, modified, propagated, or distributed except according to 
-- the terms contained in the LICENSE.txt file.
-------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

use work.StdRtlPkg.all;

library unisim;
use unisim.vcomponents.all;

entity AtlasAltirocClk is
   generic (
      TPD_G        : time    := 1 ns;
      SIMULATION_G : boolean := false);
   port (
      -- Jitter Cleaner PLL Ports
      localRefClkP : in  sl;
      localRefClkN : in  sl;
      pllClkOutP   : out sl;
      pllClkOutN   : out sl;
      pllClkInP    : in  slv(3 downto 0);
      pllClkInN    : in  slv(3 downto 0);
      pllSpiRstL   : out sl;
      pllSpiOeL    : out sl;
      pllClkSel    : out slv(1 downto 0);
      pllIntrL     : in  sl;
      pllLolL      : in  sl;
      -- Status/Config Interface
      axilClk      : in  sl;
      axilRst      : in  sl;
      clkSel       : in  slv(1 downto 0);
      oscOe        : out slv(3 downto 0);
      pwrSyncSclk  : out sl;
      pwrSyncFclk  : out sl;
      extPllLocked : out sl;
      intPllLocked : out sl;
      pllClkFreq   : out Slv32Array(3 downto 0);
      pllRst       : in  sl;
      -- Reference Clock/Reset Interface
      deserClk     : out sl;
      deserRst     : out sl;
      clk160MHz    : out sl;
      rst160MHz    : out sl;
      clk40MHz     : out sl;
      rst40MHz     : out sl);
end AtlasAltirocClk;

architecture mapping of AtlasAltirocClk is

   signal localRefClock : sl;
   signal localRefClk   : sl;
   signal pllClkIn      : slv(3 downto 0);
   signal pllClkInBufg  : slv(3 downto 0);
   signal refRst        : sl;
   signal refReset      : sl;

begin

   pllClkSel <= clkSel;

   U_pllLocked : entity work.Synchronizer
      generic map (
         TPD_G => TPD_G)
      port map (
         clk     => axilClk,
         dataIn  => pllLolL,
         dataOut => extPllLocked);

   --------------------------------------------   
   -- On-board 160 MHz reference for SI5345 PLL
   --------------------------------------------      
   U_IBUFDS : IBUFDS_GTE2
      port map (
         I     => localRefClkP,
         IB    => localRefClkN,
         CEB   => '0',
         ODIV2 => open,
         O     => localRefClock);

   U_localRefClk : BUFG
      port map (
         I => localRefClock,
         O => localRefClk);

   U_ClkOutBufDiff : entity work.ClkOutBufDiff
      generic map (
         TPD_G => TPD_G)
      port map (
         clkIn   => localRefClk,
         clkOutP => pllClkOutP,
         clkOutN => pllClkOutN);

   ---------------------------------
   -- FPGA_CLK_IN[3:1] Input buffers
   ---------------------------------
   GEN_VEC : for i in 3 downto 0 generate
      U_IBUFDS : IBUFDS
         port map (
            I  => pllClkInP(i),
            IB => pllClkInN(i),
            O  => pllClkIn(i));

      U_BUFG : BUFG
         port map (
            I => pllClkIn(i),
            O => pllClkInBufg(i));

      U_SyncClockFreq : entity work.SyncClockFreq
         generic map (
            TPD_G          => TPD_G,
            REF_CLK_FREQ_G => 156.25E+6,
            REFRESH_RATE_G => 1.0,
            CNT_WIDTH_G    => 32)
         port map (
            -- Frequency Measurement (locClk domain)
            freqOut => pllClkFreq(i),
            -- Clocks
            clkIn   => pllClkInBufg(i),
            locClk  => axilClk,
            refClk  => axilClk);

   end generate GEN_VEC;

   -----------------------------------------   
   -- External Trigger/CMD Pulse Clock/Reset
   -----------------------------------------   
   refReset <= pllRst or not(pllLolL);

   U_refRst : entity work.RstSync
      generic map(
         TPD_G          => TPD_G,
         IN_POLARITY_G  => '1',
         OUT_POLARITY_G => '1')
      port map (
         clk      => axilClk,
         asyncRst => refReset,
         syncRst  => refRst);

   U_PLL : entity work.ClockManager7
      generic map(
         TPD_G            => TPD_G,
         SIMULATION_G     => SIMULATION_G,
         TYPE_G           => "PLL",
         BANDWIDTH_G      => "HIGH",
         INPUT_BUFG_G     => false,
         FB_BUFG_G        => true,
         NUM_CLOCKS_G     => 2,
         CLKIN_PERIOD_G   => 25.0,      -- 40 MHz
         DIVCLK_DIVIDE_G  => 1,         -- 40 MHz = 40 MHz/1
         CLKFBOUT_MULT_G  => 32,        -- 1.28 GHz = 40 MHz x 32
         CLKOUT0_DIVIDE_G => 8,         -- 160 MHz = 1.28 GHz/8
         CLKOUT1_DIVIDE_G => 32)        -- 40 MHz = 1.28 GHz/32
      port map(
         clkIn     => pllClkInBufg(0),
         rstIn     => refRst,
         -- Clock Outputs
         clkOut(0) => clk160MHz,
         clkOut(1) => clk40MHz,
         -- Reset Outputs
         rstOut(0) => rst160MHz,
         rstOut(1) => rst40MHz,
         -- Status
         locked    => intPllLocked);

   ---------------------------
   -- Deserializer Clock/Reset
   ---------------------------
   deserClk <= pllClkInBufg(1);

   U_deserRst : entity work.PwrUpRst
      generic map(
         TPD_G          => TPD_G,
         IN_POLARITY_G  => '0',
         OUT_POLARITY_G => '1',
         SIM_SPEEDUP_G  => SIMULATION_G)
      port map (
         arst   => pllLolL,
         clk    => pllClkInBufg(1),
         rstOut => deserRst);

   ----------------------------------------------
   -- Not synchronizing the DC/DC to system clock
   ----------------------------------------------
   pwrSyncSclk <= '0';
   pwrSyncFclk <= '0';

   ---------------------
   -- OSC Always enabled
   ---------------------
   oscOe <= x"F";

   ------------------------
   -- PLL OE Always enabled
   ------------------------
   pllSpiOeL <= '0';

   -----------------------------------------------------
   -- Reset SPI interface with respect to AXI-Lite reset
   -----------------------------------------------------
   U_pllSpiRstL : entity work.PwrUpRst
      generic map(
         TPD_G          => TPD_G,
         IN_POLARITY_G  => '1',
         OUT_POLARITY_G => '0',
         SIM_SPEEDUP_G  => SIMULATION_G)
      port map (
         clk    => axilClk,
         arst   => axilRst,
         rstOut => pllSpiRstL);

end mapping;
