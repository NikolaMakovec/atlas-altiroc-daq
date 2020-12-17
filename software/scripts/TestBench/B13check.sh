#USING Nov 2019 TB thres.

mkdir Data//B13-tw/
mkdir Data//B13-toa/
mkdir Data//B13-thres/

python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw/  --ch 3  --Cd 0 --DAC 380 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 3 --board 13 --DAC 380 --Q 13 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 3 --board 13 --DAC 380 --Q 26 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw/  --ch 13  --Cd 0 --DAC 430 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 13 --board 13 --DAC 430 --Q 13 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 13 --board 13 --DAC 430 --Q 26 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw/  --ch 17  --Cd 0 --DAC 460 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 17 --board 13 --DAC 460 --Q 13 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 17 --board 13 --DAC 460 --Q 26 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay 2450  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw/  --ch 21  --Cd 0 --DAC 380 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 21 --board 13 --DAC 380 --Q 13 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 21 --board 13 --DAC 380 --Q 26 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B13-toa//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 300 --maxVth 600 --VthStep 2 --Cd 0 --ch 3  --Q 7 --out Data//B13-thres/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 380 --maxVth 600 --VthStep 2 --Cd 0 --ch 3  --Q 13 --out Data//B13-thres/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 300 --maxVth 600 --VthStep 2 --Cd 0 --ch 13  --Q 7 --out Data//B13-thres/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 430 --maxVth 600 --VthStep 2 --Cd 0 --ch 13  --Q 13 --out Data//B13-thres/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 300 --maxVth 600 --VthStep 2 --Cd 0 --ch 17  --Q 7 --out Data//B13-thres/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 460 --maxVth 600 --VthStep 2 --Cd 0 --ch 17  --Q 13 --out Data//B13-thres/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 300 --maxVth 600 --VthStep 2 --Cd 0 --ch 21  --Q 7 --out Data//B13-thres/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64 --autoStop True 
 sleep 5 
python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N 100 --debug False --display False --checkOFtoa False --checkOFtot False  --board 13 --delay 2450 --minVth 380 --maxVth 600 --VthStep 2 --Cd 0 --ch 21  --Q 13 --out Data//B13-thres/  --Rin_Vpa 0  --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.198 --Vthc 64 --autoStop True 
 sleep 5 
