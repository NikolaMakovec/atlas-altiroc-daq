dacOffset=0
dir=Data//B03-tw-delayScan/
mkdir $dir
for delay in {2300..2550..50}
do
    sleep 5
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 15  --Cd 0 --DAC 358 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 17  --Cd 0 --DAC 348 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 18  --Cd 0 --DAC 352 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 20  --Cd 0 --DAC 378 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 21  --Cd 0 --DAC 414 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 22  --Cd 0 --DAC 348 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 23  --Cd 0 --DAC 356 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 

 


    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 1  --Cd 0 --DAC 382 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 2  --Cd 0 --DAC 286 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 3  --Cd 0 --DAC 322 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 4  --Cd 0 --DAC 296 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 5  --Cd 0 --DAC 350 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 6  --Cd 0 --DAC 336 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 7  --Cd 0 --DAC 314 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 8  --Cd 0 --DAC 330 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 10  --Cd 0 --DAC 312 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 11  --Cd 0 --DAC 348 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 12  --Cd 0 --DAC 334 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 13  --Cd 0 --DAC 352 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
 sleep 5 


 



done



