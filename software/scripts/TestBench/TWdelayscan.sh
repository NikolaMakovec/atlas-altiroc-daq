# DONT FORGET TO REPLACE DELAY!!!!!!!!!!!!!!!!!!!

dacOffset=0
dir=Data//B03-tw-delayScan/
mkdir $dir

# for delay in {2300..2550..50}
# do
#     sleep 5


#     python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 0 --debug False --display False -N 20 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 55 --QStep 8 --out Data//B03-tw-ps-ckSRAMON/  --ch 15  --Cd 0 --DAC 358 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64 --allCkSRAMON True --doPS True 
#  sleep 5 
# python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 0 --debug False --display False -N 20 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 55 --QStep 8 --out Data//B03-tw-ps/  --ch 15  --Cd 0 --DAC 358 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64 --doPS True 
# sleep 5


# python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 0 --debug False --display False -N 20 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 55 --QStep 8 --out Data//B03-tw-ps-ckSRAMON/  --ch 1  --Cd 0 --DAC 382 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64 --allCkSRAMON True --doPS True 
#  sleep 5 

# python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 0 --debug False --display False -N 20 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 55 --QStep 8 --out Data//B03-tw-ps/  --ch 1  --Cd 0 --DAC 382 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64 --doPS True 
#  sleep 5 


# done



for delay in {2300..2550..50}
do
    sleep 5


#python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 0 --debug False --display False -N 20 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 55 --QStep 8 --out Data//B03-tw-ps-ckSRAMON/  --ch 23  --Cd 0 --DAC 356 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64 --allCkSRAMON True --doPS True 
# sleep 5 
python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 0 --debug False --display False -N 20 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 55 --QStep 8 --out Data//B03-tw-ps/  --ch 23  --Cd 0 --DAC 356 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64 --doPS True 
# sleep 5 
#python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 0 --debug False --display False -N 20 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 55 --QStep 8 --out Data//B03-tw-ps/  --ch 8  --Cd 0 --DAC 330 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64 --doPS True 
# sleep 5 
#python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ 0 --debug False --display False -N 20 --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board 3  --delay $delay  --QMin 0 --QMax 55 --QStep 8 --out Data//B03-tw-ps-ckSRAMON/  --ch 8  --Cd 0 --DAC 330 --Rin_Vpa 0 --toa_busy 0 --ON_rtest 0 --asicVersion 2 --ip 192.168.1.10 --Vthc 64 --allCkSRAMON True --doPS True 
# sleep 5

done
