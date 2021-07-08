from ASICInfo import *

def printStatus(top):
    PAList=[]
    DiscriList=[]
    SRAMList=[]
    CtestList=[]
    TrigExtList=[]
    for ipix in range(0,25):
        if top.Fpga[0].Asic.SlowControl.disable_pa[ipix].value()==0:
            PAList.append(ipix)
        if top.Fpga[0].Asic.SlowControl.ON_discri[ipix].value()==1:
            DiscriList.append(ipix)
        if top.Fpga[0].Asic.SlowControl.EN_ck_SRAM[ipix].value()==1:
            SRAMList.append(ipix)
        if top.Fpga[0].Asic.SlowControl.ON_Ctest[ipix].value()==1:
            CtestList.append(ipix)
        if top.Fpga[0].Asic.SlowControl.EN_trig_ext[ipix].value()==1:
            TrigExtList.append(ipix)
            
    print ("PAOn:",PAList)
    print ("DiscriOn:",DiscriList)
    print ("SRAMOn:",SRAMList)
    print ("CtestOn:",CtestList)
    print ("TrigExtOn:",TrigExtList)
    
def set_pixel_specific_parameters(top, pixel_number,args):
        
    #Ctest,discri,PA,SRAM off for all channels
    for ipix in range(25):
        top.Fpga[0].Asic.SlowControl.disable_pa[ipix].set(0x1)	
        top.Fpga[0].Asic.SlowControl.ON_discri[ipix].set(0x0)
        top.Fpga[0].Asic.SlowControl.EN_ck_SRAM[ipix].set(0x0)#ALWAYS ON
        top.Fpga[0].Asic.SlowControl.ON_Ctest[ipix].set(0x0)
        top.Fpga[0].Asic.SlowControl.EN_trig_ext[ipix].set(0x0)

    #for ipix in range(0,25):top.Fpga[0].Asic.SlowControl.EN_ck_SRAM[ipix].set(0x1)
    
    #turn on only one channel
    top.Fpga[0].Asic.SlowControl.disable_pa[pixel_number].set(0x0)
    top.Fpga[0].Asic.SlowControl.ON_discri[pixel_number].set(0x1)
    top.Fpga[0].Asic.SlowControl.EN_ck_SRAM[pixel_number].set(0x1)
    top.Fpga[0].Asic.SlowControl.ON_Ctest[pixel_number].set(0x1)


    #Other slow control parameters
    #top.Fpga[0].Asic.SlowControl.bit_vth_cor[pixel_number].set(0x40)
    top.Fpga[0].Asic.SlowControl.EN_hyst[pixel_number].set(0x1)
 #   top.Fpga[0].Asic.SlowControl.cBit_f_TOA[pixel_number].set(0x0)
 #   top.Fpga[0].Asic.SlowControl.cBit_s_TOA[pixel_number].set(0x0)
    top.Fpga[0].Asic.SlowControl.cBit_f_TOT[pixel_number].set(0x0)#V3: Was 0xf
    top.Fpga[0].Asic.SlowControl.cBit_s_TOT[pixel_number].set(0x0)
    top.Fpga[0].Asic.SlowControl.cBit_c_TOT[pixel_number].set(0x0)#V3 was 0xf Laurent 

    # for ipix in range(25):
    #     if ipix==pixel_number: continue
    #     top.Fpga[0].Asic.SlowControl.en_rstb_toa[ipix].set(1)  # if 1, tdc under reset
    #     top.Fpga[0].Asic.SlowControl.en_rstb_tot[ipix].set(1)

    #find columns
    if pixel_number in range(0, 5): bitset=0x1
    if pixel_number in range(5, 10): bitset=0x2
    if pixel_number in range(10, 15): bitset=0x4
    if pixel_number in range(15, 20): bitset=0x8
    if pixel_number in range(20, 25): bitset=16
    
    #Probes off
    top.Fpga[0].Asic.Probe.EN_dout.set(bitset)
    top.Fpga[0].Asic.Probe.en_probe_pa.set(bitset) # was bitset
    top.Fpga[0].Asic.Probe.en_probe_dig.set(bitset) # was bitset
    top.Fpga[0].Asic.Probe.pix[pixel_number].probe_pa.set(0x0)
    top.Fpga[0].Asic.Probe.pix[pixel_number].probe_vthc.set(0x0)
    top.Fpga[0].Asic.Probe.pix[pixel_number].probe_dig_out_disc.set(0x0)
    top.Fpga[0].Asic.Probe.pix[pixel_number].probe_toa.set(0x0)
    top.Fpga[0].Asic.Probe.pix[pixel_number].probe_tot.set(0x0)
    top.Fpga[0].Asic.Probe.pix[pixel_number].totf.set(0x0)
    top.Fpga[0].Asic.Probe.pix[pixel_number].tot_overflow.set(0x0)
    top.Fpga[0].Asic.Probe.pix[pixel_number].toa_busy.set(0x0)
    top.Fpga[0].Asic.Probe.pix[pixel_number].tot_busy.set(0x0)
    top.Fpga[0].Asic.Probe.pix[pixel_number].tot_ready.set(0x0)
    top.Fpga[0].Asic.Probe.pix[pixel_number].toa_busy.set(0x0)
    top.Fpga[0].Asic.Probe.pix[pixel_number].en_read.set(0x1)


    #probes
    for ipix in range(0,25):top.Fpga[0].Asic.Probe.pix[ipix].probe_pa.set(0x0)
    if not args.useProbePA:
        top.Fpga[0].Asic.Probe.en_probe_pa.set(0x0) 
        top.Fpga[0].Asic.Probe.pix[pixel_number].probe_pa.set(0x0)
    else:
        top.Fpga[0].Asic.Probe.en_probe_pa.set(bitset) 
        top.Fpga[0].Asic.Probe.pix[pixel_number].probe_pa.set(0x1)
    for ipix in range(0,25):top.Fpga[0].Asic.Probe.pix[ipix].probe_dig_out_disc.set(0x0)
    if not args.useProbeDiscri:
        top.Fpga[0].Asic.Probe.en_probe_dig.set(0x0) 
        top.Fpga[0].Asic.Probe.pix[pixel_number].probe_dig_out_disc.set(0x0)
    else:
        top.Fpga[0].Asic.Probe.en_probe_dig.set(bitset) 
        top.Fpga[0].Asic.Probe.pix[pixel_number].probe_dig_out_disc.set(0x1)

    #Detector capacitance
    if args.Cd>=0:
        for i in range(5):
            top.Fpga[0].Asic.SlowControl.cd[i].set(args.Cd)  



    #some more config
    #top.Fpga[0].Asic.CalPulse.CalPulseDelay.set(2000) # CAL pulse frequency 4000=0xfa0 = 100 KHz (100 µs)
    #top.Fpga[0].Asic.CalPulse.CalPulseWidth.set(12) # CAL pulse width 12 = 0xc= 75 ns
    top.Fpga[0].Asic.CalPulse.CalPulseDelay.set(2000)
    top.Fpga[0].Asic.CalPulse.CalPulseWidth.set(2000)


    top.Fpga[0].Asic.SlowControl.Rin_Vpa.set(args.Rin_Vpa)
    if args.asicVersion==3:
        top.Fpga[0].Asic.SlowControl.ON_rtest.set(args.ON_rtest)
        top.Fpga[0].Asic.SlowControl.EN_toa_busy.set(args.toa_busy)
        
    if args.Vthc>0:        top.Fpga[0].Asic.SlowControl.bit_vth_cor[pixel_number].set(args.Vthc) # alignment
        
    #Readout: only 1 channel
    top.Fpga[0].Asic.Readout.ReadoutSize.set(0)
    top.Fpga[0].Asic.Readout.RdIndexLut[0].set(pixel_number)


    #read all channels
    if args.readAllChannels:
        N=25
        #chList=[pixel_number]+[x for x in range(N) if x != pixel_number]
        chList=range(N)
        print (chList,len(chList))
        top.Fpga[0].Asic.Readout.ReadoutSize.set(len(chList)-1)
        for ipix,pix in enumerate(chList):
            top.Fpga[0].Asic.SlowControl.EN_ck_SRAM[ipix].set(0x1)
            top.Fpga[0].Asic.Readout.RdIndexLut[ipix].set(pix)




    #B13 6dead 7prb et 13prb
    #for ipix in range(0,15):
    #for ipix in list(range(0,6))+list(range(7,15)):
    #for ipix in [0,1,2,3,4,5,7,8,9,10,11,12,13,14]:
    #for ipix in list(range(0,5))+list(range(10,15)):
        #top.Fpga[0].Asic.SlowControl.disable_pa[ipix].set(0x0)	
        #top.Fpga[0].Asic.SlowControl.ON_discri[ipix].set(0x1)
        #top.Fpga[0].Asic.SlowControl.EN_ck_SRAM[ipix].set(0x1)#New
        #top.Fpga[0].Asic.SlowControl.ON_Ctest[ipix].set(0x1)
        #######top.Fpga[0].Asic.SlowControl.EN_trig_ext[ipix].set(0x1)  BLUE SWITH!!!!!!!!!
        #pass




        

    ckSRAMList=list(set(range(0,25)))
    if args.allCkSRAMON:
        for ipix in ckSRAMList:
            top.Fpga[0].Asic.SlowControl.EN_ck_SRAM[ipix].set(0x1)#New

    deadChannels={}
    deadChannels[3]=[]
    deadChannels[8]=[]
    deadChannels[13]=[6,14,18,19,24]
    deadChannels[21]=[6,11,16,21]
    deadChannels[24]=[7,14,20,21,22,23]
    deadChannels[27]=[]
    deadChannels[28]=[]
    deadChannels[29]=[1,5,14,19,23]
    deadChannels[43]=[]
    deadChannels[44]=[]
    deadChannels[45]=[3,7,9,10,13,18]
    deadChannels[46]=[]
    deadChannels[47]=[]
    deadChannels[48]=[]
    deadChannels[100]=[]
    deadChannels[102]=[]

    
    #chONList=list(set(range(0,25)).difference(set([6,11,16,20,21,22,23])))
    #chONList=list(set(range(0,25)))
    chONList=list(set(range(0,25)).difference(set(deadChannels[args.board]))) #B45
    
    
    
    print (chONList)

    if args.allChON:
        #for ipix in range(0,14):
        for ipix in chONList:
            top.Fpga[0].Asic.SlowControl.disable_pa[ipix].set(0x0)	
            top.Fpga[0].Asic.SlowControl.ON_discri[ipix].set(0x1)
            top.Fpga[0].Asic.SlowControl.EN_ck_SRAM[ipix].set(0x1)#New

    
    #ctestONList=[0,12,24]#range(0,25,8)
    #ctestONList=[7,8,9]#range(0,25,8)
    #ctestONList=[12,13,14]#range(0,25,8)
    #ctestONList=[0,1,2]#range(0,25,8)
    #ctestONList=[0,5,10]#range(0,25,8)
    #ctestONList=chONList[::4]
    #ctestONList=[20,21,22,23,24]
    #ctestONList=[23]
    #ctestONList=[4,14,19,24]
    #ctestONList=[14,15,16,17,19]
    #ctestONList=[1,6,11,16,21]
    ctestONList=chONList[::4]
    
    if args.CtestONList is not None:
        ctestONList=[int(c) for c in args.CtestONList.split(",")]
    print (ctestONList)
    if args.allCtestON:
        #for ipix in range(0,14,2):
        for ipix in ctestONList:
            top.Fpga[0].Asic.SlowControl.ON_Ctest[ipix].set(0x1)
            pass


    if int(args.board) in boardASICV3b:
        if isTZ(int(args.board),int(args.ch)):
            top.Fpga[0].Asic.SlowControl.Cp_Vpa.set(0)
        else:
            top.Fpga[0].Asic.SlowControl.Cp_Vpa.set(0)
    if args.dac_biaspa>=0:
        top.Fpga[0].Asic.SlowControl.dac_biaspa.set(args.dac_biaspa)
    #print ( " ===> ",top.Fpga[0].Asic.SlowControl.Cp_Vpa.value())
    #toto

    




def writeParameters(top,f):
    
    f.write("Parameter %s %d \n"%(  "dac_biaspa ",  top.Fpga[0].Asic.SlowControl.dac_biaspa.value()  ))
    f.write("Parameter %s %d \n"%(  "Cp_Vpa ",  top.Fpga[0].Asic.SlowControl.Cp_Vpa.value()  ))
    f.write("Parameter %s %d \n"%(  "SatFVa",  top.Fpga[0].Asic.SlowControl.SatFVa.value()  ))
    f.write("Parameter %s %d \n"%(  "IntFVa",  top.Fpga[0].Asic.SlowControl.IntFVa.value()  ))
    f.write("Parameter %s %d \n"%(  "ON_rtest ",  top.Fpga[0].Asic.SlowControl.ON_rtest.value()  ))
    f.write("Parameter %s %d \n"%(  "Rin_Vpa ",  top.Fpga[0].Asic.SlowControl.Rin_Vpa.value()  ))
    f.write("Parameter %s %d \n"%(  "DAC10bit ",  top.Fpga[0].Asic.SlowControl.DAC10bit.value()  ))
    f.write("Parameter %s %d \n"%(  "coarse_Lcomp_b ",  top.Fpga[0].Asic.SlowControl.coarse_Lcomp_b.value()  ))
    f.write("Parameter %s %d \n"%(  "coarse_Up_Downb ",  top.Fpga[0].Asic.SlowControl.coarse_Up_Downb.value()  ))
    f.write("Parameter %s %d \n"%(  "fast_Lcomp_b ",  top.Fpga[0].Asic.SlowControl.fast_Lcomp_b.value()  ))
    f.write("Parameter %s %d \n"%(  "fast_Up_Downb ",  top.Fpga[0].Asic.SlowControl.fast_Up_Downb.value()  ))
    f.write("Parameter %s %d \n"%(  "slow_Lcomp_b ",  top.Fpga[0].Asic.SlowControl.slow_Lcomp_b.value()  ))
    f.write("Parameter %s %d \n"%(  "slow_Up_Downb ",  top.Fpga[0].Asic.SlowControl.slow_Up_Downb.value()  ))
    f.write("Parameter %s %d \n"%(  "cBitf ",  top.Fpga[0].Asic.SlowControl.cBitf.value()  ))
    f.write("Parameter %s %d \n"%(  "Cbits ",  top.Fpga[0].Asic.SlowControl.Cbits.value()  ))
    f.write("Parameter %s %d \n"%(  "Cbitc ",  top.Fpga[0].Asic.SlowControl.Cbitc.value()  ))
    #f.write("Parameter %s %d \n"%(  " ",  top.Fpga[0].Asic.SlowControl..value()  ))
 
 
   #    EN_hyst[:]: 0x1
   # cd[0]: 0x0 
   #      cd[1]: 0x0 
   #      cd[2]: 0x0
   #      cd[3]: 0x0
   #      cd[4]: 0x0 
