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


#################################################################
# 
#################################################################
def parse_arguments():
    parser = argparse.ArgumentParser()
    
    # Convert str to bool
    argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
    # Add arguments
    parser.add_argument("-b", "--board", type = int, required = False, default = 2,help = "Choose board")
    parser.add_argument("--toa", action="store_true", default = False)
    parser.add_argument("-p","--prefix", required = False, default = None)#"FPGA-C01-08")
    parser.add_argument("--tot", action="store_true", default = False)
    parser.add_argument("--ip", required = False, default = '192.168.1.197', help = "IP address")
    # Get the arguments
    args = parser.parse_args()
    return args




if __name__ == "__main__":
    args = parse_arguments()

    boardASICV3=[21,24,27,28,29,31,45,102    ,48]
    board=args.board
    asicVersion=2
    if board in boardASICV3: asicVersion=3
    ip=args.ip

    chList=list(range(15,25))+list(range(0,15)) # ATTENTION A L ORDRE!!!!!!!!!!!!!!!!!!!!!!!!
    #chList=[15,17,22,13,1,8]+list(range(15,25))+list(range(0,15))
    #chList=list(range(15,25))+list(range(0,15))
    #chList=list(range(15,25))+list(range(0,15))
    chList=list(range(0,25))
    #chList=[7,21,3,17,13]#B13 TB
    #chList=[14,19,24,4,9]#v2
    #chList=[0,2,4,6,9,10,15,18,20,21,24]
    #chList=[0]

    #TOA
    toaDelayStep=1
    NTOA=20
    toaDelayMin=1750
    toaDelayMax=2350

    #TOT
    totRiseEdgeStep=1
    NTOT=20
    totRiseEdgeMin=700
    totRiseEdgeMax=3000
    totRiseEdgeMinTZ=1800
    
        
    if board==14:
        toaDelayMin=1750
        toaDelayMax=2300
        #chList=[7,8,6,10,12,13,14,5]
        
    if board in boardASICV3:
        toaDelayMin=1650
        toaDelayMax=2200


    bName="B"
    if args.board<10:
        bName+="0"
    bName+=str(args.board)
    

    
    for ch in chList:
        if args.toa:
            outdir="Data/"+bName+"-toaTrigExt"+str(toaDelayStep)
            if args.prefix is not None:
                outdir+="-"+args.prefix
                
            try:os.makedirs(outdir)
            except:pass
            nameTOA=outdir+'/delayScanTrigExt_'
            cmdTOA="python scripts/TestBench/measureTOA.py --skipExistingFile True -N %s --debug False --display False --checkOFtoa False --checkOFtot False  --board %d --ch %d --Cd 0 --useExt True --delayMin %d --delayMax %d --delayStep %d  --out %s --asicVersion %d --ip %s"%(NTOA,board,ch,toaDelayMin,toaDelayMax,toaDelayStep,nameTOA,asicVersion,ip)
            print(cmdTOA)
            print("sleep 5")


        if args.tot:
            totRiseEdgeMinLocal=totRiseEdgeMin
            if ch>=15 and     asicVersion==2:
                totRiseEdgeMinLocal=totRiseEdgeMinTZ
                pass
            outdir="Data/"+bName+"-totTrigExt"+str(totRiseEdgeStep)
            if args.prefix is not None:
                outdir+="-"+args.prefix
            try:os.makedirs(outdir)
            except:pass
            nameTOT=outdir+'/widthScanTrigExt_'
            cmdTOT="python scripts/TestBench/measureTOT.py --skipExistingFile True  -N %s --debug False --display False --checkOFtoa False --checkOFtot False  --board %d --ch %d --Cd 0 --useExt True --riseEdgeMin %d --riseEdgeMax %d --riseEdgeStep %s --out %s --asicVersion %d --ip %s"%(NTOT,board,ch,totRiseEdgeMinLocal,totRiseEdgeMax,totRiseEdgeStep,nameTOT,asicVersion,ip)
            print(cmdTOT)
            print("sleep 5")

