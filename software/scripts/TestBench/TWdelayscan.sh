dacOffset=0
for delay in {2300..2550..50}
do

    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw/  --ch 15  --Cd 0 --DAC 366+$dacOffset --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw/  --ch 16  --Cd 0 --DAC 316+$dacOffset --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw/  --ch 17  --Cd 0 --DAC 370+$dacOffset --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw/  --ch 21  --Cd 0 --DAC 334+$dacOffset --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw/  --ch 22  --Cd 0 --DAC 404+$dacOffset --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
    sleep 5 
    python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 1 --debug False --display False -N 50 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 13  --delay $delay  --QMin 0 --QMax 63 --QStep 1 --out Data//B13-tw/  --ch 23  --Cd 0 --DAC 376+$dacOffset --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64
    sleep 5

done
