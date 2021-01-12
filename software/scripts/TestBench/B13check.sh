IP=192.168.1.198

mkdir Data//B13-tw-checks/
mkdir Data//B13-toa-checks/
mkdir Data//B13-thres-noise-checks/

python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw-checks/  --ch 7  --Cd 0 --DAC 336 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 7 --board 13 --DAC 336 --Q 13 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa-checks//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 7 --board 13 --DAC 336 --Q 26 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa-checks//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw-checks/  --ch 21  --Cd 0 --DAC 352 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 21 --board 13 --DAC 352 --Q 13 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa-checks//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 21 --board 13 --DAC 352 --Q 26 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa-checks//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw-checks/  --ch 3  --Cd 0 --DAC 350 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 3 --board 13 --DAC 350 --Q 13 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa-checks//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 3 --board 13 --DAC 350 --Q 26 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa-checks//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw-checks/  --ch 17  --Cd 0 --DAC 400 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 17 --board 13 --DAC 400 --Q 13 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa-checks//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 17 --board 13 --DAC 400 --Q 26 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa-checks//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw-checks/  --ch 13  --Cd 0 --DAC 388 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 13 --board 13 --DAC 388 --Q 13 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa-checks//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 13 --board 13 --DAC 388 --Q 26 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa-checks//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 220 --maxVth 600 --VthStep 1 --Cd 0 --ch 7  --Q 6 --out Data//B13-thres-noise-checks/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 336 --maxVth 600 --VthStep 1 --Cd 0 --ch 7  --Q 13 --out Data//B13-thres-noise-checks/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 220 --maxVth 600 --VthStep 1 --Cd 0 --ch 21  --Q 6 --out Data//B13-thres-noise-checks/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 352 --maxVth 600 --VthStep 1 --Cd 0 --ch 21  --Q 13 --out Data//B13-thres-noise-checks/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 220 --maxVth 600 --VthStep 1 --Cd 0 --ch 3  --Q 6 --out Data//B13-thres-noise-checks/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 350 --maxVth 600 --VthStep 1 --Cd 0 --ch 3  --Q 13 --out Data//B13-thres-noise-checks/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 220 --maxVth 600 --VthStep 1 --Cd 0 --ch 17  --Q 6 --out Data//B13-thres-noise-checks/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 400 --maxVth 600 --VthStep 1 --Cd 0 --ch 17  --Q 13 --out Data//B13-thres-noise-checks/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 220 --maxVth 600 --VthStep 1 --Cd 0 --ch 13  --Q 6 --out Data//B13-thres-noise-checks/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 388 --maxVth 600 --VthStep 1 --Cd 0 --ch 13  --Q 13 --out Data//B13-thres-noise-checks/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip $IP  --Vthc 64 --autoStop True 
 sleep 5 
