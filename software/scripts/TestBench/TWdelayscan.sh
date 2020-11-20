dacOffset=0
dir=Data//B13-tw-ckSRAMON-delayScan-dacPlus2/
mkdir $dir
for delay in {2300..2550..50}
do

    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 15  --Cd 0 --DAC 368 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64  --allCkSRAMON True 
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 16  --Cd 0 --DAC 318 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64  --allCkSRAMON True
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 17  --Cd 0 --DAC 372 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64  --allCkSRAMON True 
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 21  --Cd 0 --DAC 336 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64  --allCkSRAMON True
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 22  --Cd 0 --DAC 406 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64  --allCkSRAMON True
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 23  --Cd 0 --DAC 378 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64  --allCkSRAMON True
    sleep 5

done




dacOffset=0
dir=Data//B13-tw-ckSRAMON-delayScan-dacPlus4/
mkdir $dir
for delay in {2300..2550..50}
do

    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 15  --Cd 0 --DAC 370 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64  --allCkSRAMON True 
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 16  --Cd 0 --DAC 320 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64  --allCkSRAMON True
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 17  --Cd 0 --DAC 374 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64  --allCkSRAMON True 
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 21  --Cd 0 --DAC 338 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64  --allCkSRAMON True
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 22  --Cd 0 --DAC 408 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64  --allCkSRAMON True
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out $dir  --ch 23  --Cd 0 --DAC 380 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64  --allCkSRAMON True
    sleep 5

done
