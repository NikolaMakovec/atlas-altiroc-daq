IB=IBv2_I3
dirtw=Data//B13-tw_$IB
dirtoa=Data//B13-toa_$IB

#mkdir $dirtw
#mkdir $dirtoa

while true

      do



	  python scripts/TestBench/measureTimeWalk.py --skipExistingFile 0 --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw-stability/  --ch 15  --Cd 0 --DAC 366 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile 0 --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw-stability/  --ch 16  --Cd 0 --DAC 316 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
 python scripts/TestBench/measureTimeWalk.py --skipExistingFile 0 --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw-stability/  --ch 5  --Cd 0 --DAC 380 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5



	  
	  sleep 180 
       done
