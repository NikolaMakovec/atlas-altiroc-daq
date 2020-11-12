IB=IBv2_I3
dirtw=Data//B13-tw_$IB
dirtoa=Data//B13-toa_$IB

mkdir $dirtw
mkdir $dirtoa

while true

      do


	  python scripts/TestBench/measureTimeWalk.py --skipExistingFile False --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out $dirtw/  --ch 0  --Cd 0 --DAC 320 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
	  sleep 5 
	  python scripts/TestBench/measureTOA.py --skipExistingFile False -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 0 --board 13 --DAC 320 --Q 5 --delayMin 2200 --delayMax 2700 --delayStep 5 --out $dirtoa/  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
	  sleep 5 
	  python scripts/TestBench/measureTimeWalk.py --skipExistingFile False --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out $dirtw/  --ch 15  --Cd 0 --DAC 366 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
	  sleep 5 
	  python scripts/TestBench/measureTOA.py --skipExistingFile False -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 15 --board 13 --DAC 366 --Q 5 --delayMin 2200 --delayMax 2700 --delayStep 5 --out $dirtoa/  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
	  sleep 5 
       done
