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
    parser.add_argument("--tot", action="store_true", default = False)

    # Get the arguments
    args = parser.parse_args()
    return args




if __name__ == "__main__":
    args = parse_arguments()

    boardASICV3=[21,24,27,29,31]
    board=args.board
    asicVersion=2
    if board in boardASICV3: asicVersion=3


    chList=list(range(0,25))

    NTOT=20
    totRiseEdgeMin=700
    totRiseEdgeMax=3000
    totRiseEdgeStep=20   #Need 1 for TOTf


    NTOA=100#was 500
    toaDelayStep=1
    toaDelayMin=1750
    toaDelayMax=2350
    
    if board==14:
        toaDelayMin=1750
        toaDelayMax=2300
        #chList=[7,8,6,10,12,13,14,5]
        
    if board in boardASICV3:
        toaDelayMin=1750
        toaDelayMax=2200





    
    for ch in chList:
        if args.toa:
            #nameTOA='Data/delayScanTrigExt_B_%d_ch_%d_'%(board,ch)
            nameTOA='Data/delayScanTrigExt_'
            cmdTOA="python scripts/TestBench/measureTOA.py --skipExistingFile True -N %s --debug False --display False --checkOFtoa False --checkOFtot False  --board %d --ch %d --Cd 0 --useExt True --delayMin %d --delayMax %d --delayStep %d  --out %s --asicVersion %d"%(NTOA,board,ch,toaDelayMin,toaDelayMax,toaDelayStep,nameTOA,asicVersion)
            print(cmdTOA)
            print("sleep 5")


        if args.tot:
            #nameTOT='Data/widthScanTrigExt_B_%d_ch_%d_'%(board,ch)
            nameTOT='Data/widthScanTrigExt_'
            cmdTOT="python scripts/TestBench/measureTOT.py --skipExistingFile True  -N %s --debug False --display False --checkOFtoa False --checkOFtot False  --board %d --ch %d --Cd 0 --useExt True --riseEdgeMin %d --riseEdgeMax %d --riseEdgeStep %s --out %s --asicVersion %d"%(NTOT,board,ch,totRiseEdgeMin,totRiseEdgeMax,totRiseEdgeStep,nameTOT,asicVersion)
            print(cmdTOT)
            print("sleep 5")

