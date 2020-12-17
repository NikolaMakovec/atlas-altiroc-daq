#!/usr/bin/env python3
#################################################################
import sys                                                     ##
import time                                                    ##
import random                                                  ##
import argparse                                                ##
import pickle                                                  ##
import numpy as np                                             ##
import os                                                      ##
import math                                                    ##
#################################################################
from DAC import *
from computeVth import *
from runParameters import *

doSepDir = 1
#####################
# 
#####################

if doTOA+doClockTree +doXtalk+doDNL>1:
    print ("Prb TOA")
    sys.exit()
if doThres+doNoise+doVthcScan+doLinearity >1:
    print ("Prb Thres")
    sys.exit()
if doTW+doTWscan+doPS>1:
    print ("Prb TW")
    sys.exit()



delayList=[]

#####################
# TW
#####################
qMin=0
qMax=63#63#63
qStep=1#1 or x4
Ntw=50
morePointsAtLowQ=1
if doTWdelay:
    doTW=1
    #delayList=range(2350,2550+1,100)
    
if doPSdelay:
    doPS=1
    doTW=1
    #delayList=range(2350,2550+1,100)
    #toooot

if doPS:
    doTW=1
    morePointsAtLowQ=0
    Ntw=20
    
if doTWscan:
    doTW=1
    

# TOA
#####################
    
Ntoa=50;
delayStep=10 
delayMin=2200
delayMax=2700

if doDNL:
    doTOA=1
    delayStep=1
    QTOAList=[63]
    Ntoa=500
        
if doClockTree:
    doTOA=1
    delayStep=5
    QTOAList=[63]#ClockTree
    Ntoa=100
    #Ntoa=400
    #delayStep=10
    
if doXtalk == 1:
    doTOA=1
    QTOAList=[63]#13,60]
    args.useVthc=True
    #delayMin=2400#200
    #delayMax=2500
    #delayStep=10
    Ntoa=200
    
#####################
# Threshold
#####################

Nthres=100
#QThresList=[1,2,3,5]
thresMin=220  #overwritten for large Q
thresMax=600 #max is 1023
thresStep=2
if doLinearity:
    doThres= 1
    Nthres=100
    thresStep=2
    thresMax=1000
    QThresList=[0,2,4,8,16,32,63]#[0,3,5,9,13,18,26,39,63]
    
if doNoise:
    doThres=1
    Nthres=100
    thresStep=1
    thresMax=600

if doVthcScan:
    doThres= 1
    Nthres=100
    thresMin=0 
    thresMax=128
    thresStep=1
    
#if doThres:chList=range(25)

def getDelay(board,ch,cd):
    #delay
    delay=2450
    if board==3:
        delay=2500
    if board==8:
        delay=2500
    elif board==21:
        #delay=2350
        ## #if ch>=20:delay=2400
        #if cd<4 or ch>=20:
        delay=2400
        #print (ch,cd,delay)
    elif board==24:
        delay=2400
    elif board==28:
        delay=2400
    elif board==29:
        delay=2400
    elif board==31:
        delay=2400
    return delay

def parse_arguments():    
    parser = argparse.ArgumentParser()
    argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
    parser.add_argument("--ip", required = False, default = '192.168.1.196', help = "IP address")
    parser.add_argument("-o", "--outputDir", default = "Data/")
    parser.add_argument("-b", "--board", type = int, required = False, default = 8,help = "Choose board")
    parser.add_argument("-c","--ch", type = int, required = False, default = 4, help = "channel")
    parser.add_argument("--cfg", required = False, default = None)
    parser.add_argument("-p","--prefix", required = False, default = prefix)
    parser.add_argument("--chON", action="store_true", default = False)
    parser.add_argument("--toabusyON", action="store_true", default = False)
    parser.add_argument("--probePAON", action="store_true", default = False)
    parser.add_argument("--ckSRAMON", action="store_true", default = False)
    parser.add_argument("--ctestON", action="store_true", default = False)
    parser.add_argument("--useVthc", action="store_true", default = False)
    parser.add_argument("--readAllChannels", action="store_true", default = False)

    args = parser.parse_args()
    return args



if __name__ == "__main__":
    args = parse_arguments()
    

    boardASICAlone=[4,8,9,10,11,12,14,15,21,24,31]
    boardASICV3=[21,24,27,28,29,31]
    board=args.board
    asicVersion=2
    if board in boardASICV3: asicVersion=3
    ip=args.ip


    if doFullQScanForTOA == 1:
        if asicVersion==2:            
            QTOAList=[4,5,6,7,9,13,19,26,63]#v2
        else:
            QTOAList=[5,6,7,9,11,16,24,32,63]#v3
    elif len(QTOAList)==0:
        if asicVersion==2:            
            QTOAList=[7,13,26,63]#v2:7,13,26,63
        elif asicVersion==2:            
            QTOAList=[9,16,32,63]#v3
            
    if doNoise:
        if asicVersion==3:            
            QThresList=[8,17]#V3
        else:
            QThresList=[6,13]#V2



        
    #detector capacitance
    #cdList=[4]
    if board not in boardASICAlone and cdZeroForASICAlone:
        cdList=[0];

    #output dir name
    if doSepDir:
        bName="B"
        if args.board<10:
            bName+="0"
        bName+=str(args.board)
        thresDir=bName+"-thres"
        if doNoise:thresDir+="-noise"
        if doVthcScan:thresDir+="-vthcScan"
        if doLinearity:thresDir+="-lin"
        twDir=bName+"-tw"
        if doPS:twDir+="-ps"
        if doTWscan:twDir+="-scan"
        toaDir=bName+"-toa"
        if doClockTree:toaDir+="-clkTree"
        if doDNL:toaDir+="-dnl"
        if doXtalk:toaDir+="-xtalk"

        if args.useVthc:
            toaDir+="-Vthc"
            twDir+="-Vthc"
            thresDir+="-Vthc"

        if args.toabusyON:
            toaDir+="-toabusyON"
            twDir+="-toabusyON"
            thresDir+="-toabusyON"
            
        if args.probePAON:
            toaDir+="-probePAON"
            twDir+="-probePAON"
            thresDir+="-probePAON"
            
        if args.ckSRAMON:
            toaDir+="-ckSRAMON"
            twDir+="-ckSRAMON"
            thresDir+="-ckSRAMON"
            
        if args.chON:
            toaDir+="-chON"
            twDir+="-chON"
            thresDir+="-chON"
            
        if args.ctestON:
            toaDir+="-ctestON"
            twDir+="-ctestON"
            thresDir+="-ctestON"
            
        if ON_rtest>0:
            toaDir+="-rtestON"
            twDir+="-rtestON"
            thresDir+="-rtestON"
            
        if Rin_Vpa>0:
            toaDir+="-RinVpa"+str(Rin_Vpa)
            twDir+="-RinVpa"+str(Rin_Vpa)
            thresDir+="-RinVpa"+str(Rin_Vpa)
            
        if dacOffset!=0:
            sign=""
            if dacOffset<0:sign="minus"
            
            toaDir+="-dacOffset"+sign+str(abs(dacOffset))
            twDir+="-dacOffset"+sign+str(abs(dacOffset))
            thresDir+="-dacOffset"+sign+str(abs(dacOffset))


        if args.prefix is not None:
            toaDir+="-"+args.prefix
            twDir+="-"+args.prefix
            thresDir+="-"+args.prefix



    
    fname="runPulser"#TW_B"+str(board)
    if args.useVthc:
        fname+="_useVthc"
    if args.toabusyON:
        fname+="_toabusyON"
    if args.ckSRAMON:
        fname+="_ckSRAMON"
    if args.chON:
        fname+="_chON"
    if args.ctestON:
        fname+="_ctestON"
    fname+=".sh"
    f=open(fname,"w")






        
    #threshold
    dacMap=None
    dacMap=getDACList(board)
    dacRef=0

    #channel list
    if chList==None:
        if board in boardASICAlone:
            if board  in boardASICV3:
                chList=list(range(20))+[24]
            else:
                chList=[4,9,14,19,24]
        elif dacMap==None or len(dacMap)==0:
            chList=range(25)
        else:            
            chList= set([k[1] for k in sorted(dacMap.keys())])
        #chList=list(range(15,25))+list(range(0,15))



        


        
    ###############################
    # TW and TOA
    ###############################
    for ch in chList:
        for cd in cdList:




            delay=getDelay(board,ch,cd)
    
            if doTWdelay or doPSdelay:
                step=80
                delayList=[delay-step,delay,delay+step]
            else:
                if len(delayList)==0:
                    delayList=[delay]


                
            #if ch not in [4,9,14] ans:
            #dac list
            dacNom=0
            if args.useVthc:                
                #dacRef,vthcMap=getVthc(board,cd)
                dacNom=-1#dacRef
                vthcList=[-1]
            else:
                vthcList=[64]
                if (board,ch,cd) in dacMap.keys():
                    dacNom=dacMap[(board,ch,cd)]
                elif (board,ch,4) in dacMap.keys():
                    print (ch,"Take thres. for cd=4 while using cd=",cd)
                    dacNom=dacMap[(board,ch,4)]
                    #time.sleep(1)
                else:
                    print ("********** PRB with dacMap, break*****",(board,ch,4))
                    time.sleep(0.005)
                    break
            dacNom+=dacOffset
            dacListLocal=[dacNom]

            
            if doPS:
                qMin=8;#for pedestal
                qMax=48+1#48+1;
                qStep=8   #default 8
                #dacListLocal=[dacNom]
                # dacStep=4 #default 4 
                # dacListLocal=list(range(dacNom-20,dacNom+100,dacStep))
                # dacListLocal+=list(range(dacNom+100,dacNom+160,dacStep))                
                # #dacListLocal+=list(range(dacNom-10,dacNom+10,2))#more point at low value
                # if board in boardASICAlone:
                #     dacListLocal+=list(range(dacNom+160,dacNom+200,dacStep))
                #     if cd<=3:dacListLocal+=list(range(dacNom+200,dacNom+280,8))
                #     if cd<=1:dacListLocal+=list(range(dacNom+280,dacNom+360,16))
                # dacListLocal=sorted(list(set([dac for dac in dacListLocal if dac<1024 ])))#remove value larger than max
                
                #print (dacListLocal)
                if args.useVthc:
                    dacListLocal=[-1]
                    vthcList=range(32,96+1,32)


            #print(ch,cd,delay,dacListLocal,vthcList)            
            for dac in dacListLocal:   
                #print (dac)
                ###############################
                # measure TW
                ###############################
                if doTW:
                    for vthc in vthcList:
                        for delay in delayList:
                            outdir=args.outputDir+"/"+twDir+"/"

                            try:os.makedirs(outdir)
                            except:pass
                            cmd="python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ %d --debug False --display False -N %d --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board %d  --delay %d  --QMin %d --QMax %d --QStep %d --out %s  --ch %d  --Cd %d --DAC %d --Rin_Vpa %d --toa_busy %d --ON_rtest %d --asicVersion %d --ip %s"%(morePointsAtLowQ,Ntw,board,delay,qMin,qMax,qStep,outdir,ch,cd,dac,Rin_Vpa,args.toabusyON,ON_rtest,asicVersion,ip)

                            if args.probePAON:
                                cmd+=" --useProbePA True "
                            if not args.useVthc  or (args.useVthc and doPS):#take the one from config
                                #vthc=64
                                cmd+=" --Vthc "+str(vthc)
                                pass
                            if args.chON:
                                cmd+=" --allChON True"
                                pass
                            if args.ckSRAMON:
                                cmd+=" --allCkSRAMON True"
                                pass
                            if args.ctestON:
                                cmd+=" --allCtestON True"
                                pass
                            if args.cfg is not None:
                                cmd+=" --cfg "+args.cfg
                                pass
                            if doPS :
                                cmd+=" --doPS True "
                                pass
                            if doTWscan :
                                cmd+=" --doTWscan True "
                                pass

                            f.write(cmd+"\n sleep 5 \n")
                    
                ###############################
                # measure TOA
                ###############################
            
                if doTOA:
                    #print ("/ppppppppppppp",dacNom,dac)
                    for vthc in vthcList:
                        if dac!=dacNom: continue
                        for Q in QTOAList:
                            if Q<0:#trig ext                        
                                delayMin=1800
                                delayMax=2300
                            outdir=args.outputDir+"/"+toaDir+"/"
                            logName=outdir+'/delayTOA_B_%d_rin_%d_toabusy_%d_rtest_%d_ch_%d_cd_%d_Q_%d_thres_%d.log'%(board,Rin_Vpa,args.toabusyON,ON_rtest,ch,cd,Q,dac)
                            try:os.makedirs(outdir)
                            except:pass
                            cmd="python scripts/TestBench/measureTOA.py --skipExistingFile True -N %d --debug False --display False --Cd %d --checkOFtoa False --checkOFtot False --ch %d --board %d --DAC %d --Q %d --delayMin %d --delayMax %d --delayStep %d --out %s/delay  --Rin_Vpa %d   --toa_busy %d --ON_rtest %d --asicVersion %d --ip %s"%(Ntoa,cd,ch,board,dac,Q,delayMin,delayMax,delayStep,outdir,Rin_Vpa,args.toabusyON,ON_rtest,asicVersion,ip)


                            if args.probePAON:
                                cmd+=" --useProbePA True "
                            
                            if not args.useVthc:#take the one from config
                                #vthc=64
                                cmd+=" --Vthc "+str(vthc)
                                pass
                            if args.chON:
                                cmd+=" --allChON True"
                                pass
                            if args.ckSRAMON:
                                cmd+=" --allCkSRAMON True"
                                pass
                            if args.ctestON:
                                cmd+=" --allCtestON True"
                                pass
                            if Q<0:
                                cmd+=" --useExt True "
                            if doXtalk:
                                cmd+=" --readAllChannels True  --allChON True "
                                cmd+=" |& tee "+logName
                            if args.readAllChannels:
                                cmd+=" --readAllChannels True "
                                cmd+=" |& tee "+logName

                            f.write(cmd+"\n sleep 5 \n")





    ###############################
    # thres. scan
    ###############################        
    if doThres:
        for ch in chList:
            for cd in cdList:
                for Q in QThresList:#ATT TRIG EXT
                    if Q >10 and (board,ch,cd) in dacMap.keys():
                        thresMinLocal=dacMap[(board,ch,cd)]#-20+(Q-3)*7
                        #thresMinLocal=min(thresMinLocal,450)
                    else:
                        thresMinLocal=thresMin

                    delay=getDelay(board,ch,cd)

                    if  (board,ch) not in [ ele[0:2] for ele in dacMap.keys()]:
                        print ("Thres. skip ",board,ch)
                        continue
                    
                    #print (Nthres,board,delay,thresMinLocal,thresMax,thresStep,cd,ch,Q,args.outputDir)
                    outdir=args.outputDir+"/"+thresDir+"/"
                    try:os.makedirs(outdir)
                    except:pass
                    cmd="python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N %d --debug False --display False --checkOFtoa False --checkOFtot False  --board %d --delay %d --minVth %d --maxVth %d --VthStep %d --Cd %d --ch %d  --Q %d --out %s  --Rin_Vpa %d  --toa_busy %d --ON_rtest %d --asicVersion %d --ip %s"%(Nthres,board,delay,thresMinLocal,thresMax,thresStep,cd,ch,Q,outdir,Rin_Vpa,args.toabusyON,ON_rtest,asicVersion,ip)
                    cmd+=" --Vthc 64"

                    
                    if args.ckSRAMON:
                        cmd+=" --allCkSRAMON True"
                        pass
                    if args.chON:
                        cmd+=" --allChON True"
                        pass
                    if args.ctestON:
                        cmd+=" --allCtestON True"
                        pass
                    if doVthcScan:
                        cmd+=" --vthcScan True "
                    else:
                        cmd+=" --autoStop True "

                    f.write(cmd+"\n sleep 5 \n")


print ("*********************************************")
print ("---------------------------------")
print ("doThres     ",doThres     )
print ("doNoise     ",doNoise     )
print ("doLinearity ",doLinearity )
print ("doVthcScan  ",doVthcScan     )
print ("---------------------------------")
print ("doTW        ",doTW        )
print ("doTWscan    ",doTWscan        )
print ("doPS        ",doPS        )
print ("---------------------------------")
print ("doTOA       ",doTOA       )
print ("doClockTree ",doClockTree )
print ("doXtalk     ",doXtalk     )
print ("*********************************************")
                    
                    
print (" ") 
print ("args.useVthc:",args.useVthc)
print (" " )
print (" ************ CHECK TRIG EXT ***************")
print (" ************ CHECK TRIG EXT ***************")
print (" ************ CHECK TRIG EXT ***************")
print ("Rin_vpa:",Rin_Vpa)
print ("ON_rtest:",ON_rtest)
print ("EN_toabusy:",args.toabusyON)


print("===========================================> board: "+str(args.board))
print ("Cd:",cdList)
print ("Ch:",chList)
print ("Delay:",delayList)
print("source "+fname)



