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

#####################
# 
#####################

doSepDir = 1

doThres     = 0
doNoise     = 0 # Thres with high stat for few Q
doLinearity = 0 #  Thres for many Q

doTW        = 0
doPS        = 0 # TW with thres. scan

doTOA       = 1
doClockTree = 0 # TOA with at least Q=63 and maybe larger N
doDNL       = 0 # TOA step=1
doXtalk     = 0 # TOA Channels should be ON

#ch list
chList=None
#chList=range(25)
#chList=range(5)
#chList=[0,10,12,15,24]
#chList=[4]

        
#####################
# 
#####################



if doTOA+doClockTree +doXtalk+doDNL>1:
    print ("Prb TOA")
    sys.exit()
if doThres+doNoise+doLinearity >1:
    print ("Prb Thres")
    sys.exit()
if doTW+doPS>1:
    print ("Prb TW")
    sys.exit()
    
#####################
# TW
#####################
qMin=0
qMax=63#63#63
qStep=8#1 or x4
Ntw=50
if doPS:
    doTW=1

    
#####################
# TOA
#####################
    
Ntoa=100;
delayStep=5 
delayMin=2150
delayMax=2700
QTOAList=[4,5,6,8,12,16,32,63]#default
QTOAList=[6,8,16,63]#6,7,16,63]#default
QTOAList=[8,63]
#Ntoa=500;delayStep=20;#QTOAList=[63] #Default to check distributions


if doDNL:
    doTOA=1
    delayStep=1
    QTOAList=[63]
    Ntoa=500
        
if doClockTree:
    doTOA=1
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
QThresList=[3]#default
#QThresList=[1,2,3,5]
thresMin=240  #overwritten for large Q
thresMax=1023 #max is 1023
thresStep=2
if doLinearity:
    doThres= 1
    Nthres=100
    thresStep=2
    QThresList=[0,2,4,8,16,32,63]#[0,3,5,9,13,18,26,39,63]
    
if doNoise:
    doThres=1
    Nthres=100
    thresStep=1
    thresMax=600
    QThresList=[8,16]#10
    #QThresList=[5,9,6,13]


#if doThres:chList=range(25)


    
def parse_arguments():
    parser = argparse.ArgumentParser()
    argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
    parser.add_argument("-o", "--outputDir", default = "Data/")
    parser.add_argument("-b", "--board", type = int, required = False, default = 8,help = "Choose board")
    parser.add_argument("-c","--ch", type = int, required = False, default = 4, help = "channel")
    parser.add_argument("--cfg", required = False, default = None)
    parser.add_argument("--chON", action="store_true", default = False)
    parser.add_argument("--ctestON", action="store_true", default = False)
    parser.add_argument("--useVthc", action="store_true", default = False)
    parser.add_argument("--readAllChannels", action="store_true", default = False)

    args = parser.parse_args()
    return args



if __name__ == "__main__":
    args = parse_arguments()
    

    boardASICAlone=[4,8,9,10,11,12,14,15,21]
    boardASICV3=[21]
    board=args.board
    asicVersion=2
    if board in boardASICV3: asicVersion=3
    
    #detector capacitance
    cdList=[4]
    if board not in boardASICAlone:
        cdList=[0];

    #output dir name
    if doSepDir:
        bName="B"
        if args.board<10:
            bName+="0"
        bName+=str(args.board)
        thresDir=bName+"-thres"
        if doNoise:thresDir+="-noise"
        if doLinearity:thresDir+="-lin"
        twDir=bName+"-tw"
        if doPS:twDir+="-ps"
        toaDir=bName+"-toa"
        if doClockTree:toaDir+="-clkTree"
        if doDNL:toaDir+="-dnl"
        if doXtalk:toaDir+="-xtalk"

        if args.useVthc:
            toaDir+="-Vthc"
            twDir+="-Vthc"
            thresDir+="-Vthc"

        if args.chON:
            toaDir+="-chON"
            twDir+="-chON"
            thresDir+="-chON"
            
        if args.ctestON:
            toaDir+="-ctestON"
            twDir+="-ctestON"
            thresDir+="-ctestON"





    
    fname="runPulser"#TW_B"+str(board)
    if args.useVthc:
        fname+="_useVthc"
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
        if dacMap==None or len(dacMap)==0:
            chList=range(15)
        else:            
            chList= set([k[1] for k in sorted(dacMap.keys())])
        #chList=list(range(15,25))+list(range(0,15))



        
    #special settings
    Rin_Vpa=0
    delay=2450
    if board==8:
        delay=2500
    elif board==21:
        delay=2350


        
    ###############################
    # TW and TOA
    ###############################
    for ch in chList:
        for cd in cdList:
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
                else:
                    print ("PRB with dacMap, break")
                    break
            dacListLocal=[dacNom]

            
            if doPS:
                qMin=0;#for pedestal
                qMax=26+1#26;
                qStep=4 #for pulse shape#PULSESHAPE
                dacListLocal=list(range(dacNom-20,dacNom+110,10))

                qMax=63;qStep=8 #Larger range
                dacListLocal=list(range(dacNom-20,dacNom+20,2))
                dacListLocal=list(range(dacNom-52,dacNom,2))
                
                #dacListLocal=list(range(dacNom-100,dacNom+150,10))
                #dacListLocal=list(range(dacNom+150,dacNom+250,10))

            
            #print(ch,cd,delay,dacListLocal,vthcList)            
            for dac in dacListLocal:   

                ###############################
                # measure TW
                ###############################
                if doTW:
                    for vthc in vthcList:
                        outdir=args.outputDir+"/"+twDir+"/"

                        try:os.makedirs(outdir)
                        except:pass
                        cmd="python scripts/TestBench/measureTimeWalk.py --skipExistingFile True --moreStatAtLowQ False --morePointsAtLowQ True --debug False --display False -N %d --useProbePA False --useProbeDiscri False  --checkOFtoa False --checkOFtot False --board %d  --delay %d  --QMin %d --QMax %d --QStep %d --out %s  --ch %d  --Cd %d --DAC %d --Rin_Vpa %d --asicVersion %d"%(Ntw,board,delay,qMin,qMax,qStep,outdir,ch,cd,dac,Rin_Vpa,asicVersion)


                        if not args.useVthc:#take the one from config
                            #vthc=64
                            cmd+=" --Vthc "+str(vthc)
                            pass
                        if args.chON:
                            cmd+=" --allChON True"
                            pass
                        if args.ctestON:
                            cmd+=" --allCtestON True"
                            pass
                        if args.cfg is not None:
                            cmd+=" --cfg "+args.cfg
                            pass
                        
                        f.write(cmd+"\n sleep 5 \n")
                    
                ###############################
                # measure TOA
                ###############################
            
            if doTOA:
                for vthc in vthcList:
                    if dac!=dacNom: continue
                    for Q in QTOAList:
                        if Q<0:#trig ext                        
                            delayMin=1800
                            delayMax=2300
                        outdir=args.outputDir+"/"+toaDir+"/"
                        logName=outdir+'/delayTOA_B_%d_rin_%d_ch_%d_cd_%d_Q_%d_thres_%d.log'%(board,Rin_Vpa,ch,cd,Q,dac)
                        try:os.makedirs(outdir)
                        except:pass
                        cmd="python scripts/TestBench/measureTOA.py --skipExistingFile True -N %d --debug False --display False --Cd %d --checkOFtoa False --checkOFtot False --ch %d --board %d --DAC %d --Q %d --delayMin %d --delayMax %d --delayStep %d --out %s/delay  --Rin_Vpa %d --asicVersion %d"%(Ntoa,cd,ch,board,dac,Q,delayMin,delayMax,delayStep,outdir,Rin_Vpa,asicVersion)

                        if not args.useVthc:#take the one from config
                            #vthc=64
                            cmd+=" --Vthc "+str(vthc)
                            pass
                        if args.chON:
                            cmd+=" --allChON True"
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


                    #print (Nthres,board,delay,thresMinLocal,thresMax,thresStep,cd,ch,Q,args.outputDir)
                    outdir=args.outputDir+"/"+thresDir+"/"
                    try:os.makedirs(outdir)
                    except:pass
                    cmd="python scripts/TestBench/thresholdScan.py  --skipExistingFile True --N %d --debug False --display False --checkOFtoa False --checkOFtot False  --board %d --delay %d --minVth %d --maxVth %d --VthStep %d --Cd %d --ch %d --autoStop True  --Q %d --out %s  --Rin_Vpa %d --asicVersion %d"%(Nthres,board,delay,thresMinLocal,thresMax,thresStep,cd,ch,Q,outdir,Rin_Vpa,asicVersion)
                    cmd+=" --Vthc 64"

                    f.write(cmd+"\n sleep 5 \n")


print ("*********************************************")
print ("---------------------------------")
print ("doThres     ",doThres     )
print ("doNoise     ",doNoise     )
print ("doLinearity ",doLinearity )
print ("---------------------------------")
print ("doTW        ",doTW        )
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

print("===========================================> board: "+str(args.board))
print ("Cd:",cdList)
print ("Ch:",chList)
print("source "+fname)



