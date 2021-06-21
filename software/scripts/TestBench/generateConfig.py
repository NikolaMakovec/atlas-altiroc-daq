#!/usr/bin/env python

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# Import Modules                                                             # 
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
import sys, os, string, shutil,pickle, subprocess, math
import getpass
from array import array
from math import *
from time import *
import time
import numpy as np


def getProbe(ch):
    #print ch
    if ch<5:
        probe="0x1"
    elif ch<10:
        probe="0x2"
    elif ch<15:
        probe="0x4"
    elif ch<20:
        probe="0x8"
    elif ch<25:
        probe="0x16"
    #print probe
    return probe

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# 
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

from optparse import OptionParser
parser = OptionParser()
            

parser.add_option("-f","--fname",  default = "Inputs/BXv2_ch12_probePA_probeDiscri.yml", help = "")
parser.add_option("-c","--chRef", type = int,  default = 12, help = "ch")
(options, args) = parser.parse_args()


fname=options.fname
chRef=options.chRef

probeRef=getProbe(chRef)

if fname.find("ch"+str(chRef)+"_")<0:
    print ("ch nb not found in fname")
    sys.exit()


for ch in range(25):
    if ch==chRef: continue
    print ("============> ",ch)
    probe=getProbe(ch)


    fnew=open(fname.split("/")[-1].replace("ch"+str(chRef) ,"ch"+str(ch)),"w")
    f=open(fname,"r")
    for line in f.readlines():

        if line.find("Fpga")<0:
            line=line.replace("[%d]"%(chRef),"[%d]"%(ch))
        
        if line.find("RdIndexLut[0]")>=0:
            line=line.replace(str(chRef),str(ch))

        if any(np.array([line.find(l) for l in ["en_probe_dig","en_probe_pa"]])>=0):
            if line.find(probeRef)<0: 
                print ("Strange")
                print (line,probeRef,probe)
            line=line.replace(str(probeRef),str(probe))


        
        #print line
        fnew.write(line)

    fnew.close()
        
