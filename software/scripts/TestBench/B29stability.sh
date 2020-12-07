mkdir Data//B29-tw-stability/
mkdir Data//B29-toa-stability/


python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 29  --delay 2400  --QMin 0 --QMax 63 --QStep 1 --out Data//B29-tw-stability/  --ch 0  --Cd 0 --DAC 330 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 0 --board 29 --DAC 330 --Q 6 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B29-toa-stability//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 0 --board 29 --DAC 330 --Q 9 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B29-toa-stability//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 0 --board 29 --DAC 330 --Q 16 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B29-toa-stability//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 29  --delay 2400  --QMin 0 --QMax 63 --QStep 1 --out Data//B29-tw-stability/  --ch 3  --Cd 0 --DAC 296 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 3 --board 29 --DAC 296 --Q 6 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B29-toa-stability//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 3 --board 29 --DAC 296 --Q 9 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B29-toa-stability//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 3 --board 29 --DAC 296 --Q 16 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B29-toa-stability//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 29  --delay 2400  --QMin 0 --QMax 63 --QStep 1 --out Data//B29-tw-stability/  --ch 6  --Cd 0 --DAC 306 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 6 --board 29 --DAC 306 --Q 6 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B29-toa-stability//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 6 --board 29 --DAC 306 --Q 9 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B29-toa-stability//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 6 --board 29 --DAC 306 --Q 16 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B29-toa-stability//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 29  --delay 2400  --QMin 0 --QMax 63 --QStep 1 --out Data//B29-tw-stability/  --ch 10  --Cd 0 --DAC 268 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 10 --board 29 --DAC 268 --Q 6 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B29-toa-stability//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 10 --board 29 --DAC 268 --Q 9 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B29-toa-stability//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTOA.py --skipExistingFile True -N 50 --debug False --display False --Cd 0 --checkOFtoa False --checkOFtot False --ch 10 --board 29 --DAC 268 --Q 16 --delayMin 2200 --delayMax 2700 --delayStep 10 --out Data//B29-toa-stability//delay  --Rin_Vpa 0   --toa_busy 0 --ON_rtest 0 --asicVersion 3 --ip 192.168.1.198 --Vthc 64
 sleep 5 
