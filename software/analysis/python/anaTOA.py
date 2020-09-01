#!/usr/bin/env python

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# Import Modules                                                             # 
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
import sys, os, string, shutil,pickle, subprocess, math, getpass, collections,glob

from optparse import OptionParser
from math import *
from time import *

import numpy as np
import matplotlib
import matplotlib.gridspec as gridspec
from matplotlib import pyplot as plt
#from scipy import optimize
from Utils import *


###########################################################################
# command line arguments
###########################################################################



parser = OptionParser()

parser.add_option("--QRef", help="Charge values to make some plots", default=52,type=int)
parser.add_option("-f","--fileList", help="file containing a list of input file", default=None)
parser.add_option("-i","--inputDir", help="Data location", default=None)#"Data/B8_toa_clkTree/")
parser.add_option("-s","--select", help="select only file names containing this string", default="")
parser.add_option("-a","--allPlots", help="make all plots for debugging purpose", default=False,action="store_true")
parser.add_option("-d","--display", help="display summary plots on screen", default=False,action="store_true")
parser.add_option("-b","--bidim", help="make TOA vs delay bidimensionnal plot (a bit slower) ", default=False,action="store_true")
(options, args) = parser.parse_args()

#make list of input files
fileNameList=getFileList(options.inputDir,options.fileList,measType="TOA_B",select=options.select)

###########################################################################
# some parameters
###########################################################################

DelayStep=9.5582
Qconv=0.6#10./13.
delayRef=2450*DelayStep
nChannelsMax=25

###########################################################################
# 
###########################################################################

#define figures
figTOAMean=plt.figure('TOAMean')
axTOAMean = figTOAMean.add_subplot(1,1,1)
figJitter=plt.figure('Jitter')
axJitter = figJitter.add_subplot(1,1,1)

#define lists to store data
allData=collections.OrderedDict()
LSBList=[]
chList=[]
TOARefList=[]
JitterRefList=[]
QList=[]
jitterMeanList=[]
for i in range(nChannelsMax):
    QList.append([])
    jitterMeanList.append([])

counterColor=0
for fileNb,fileName in enumerate(sorted(fileNameList,key=lambda n: getInfoFromFileName(n)[1])):
    print ("===> process ",fileName)
    #define lists  to store data
    delayList=[]
    delayDACList=[]
    toaMeanList=[]
    jitterList=[]
    allTOAList=[]
    effList=[]
    allDelayList=[]

    # extract information from the file name
    board,ch,cd,thres,vthc,Q=getInfoFromFileName(fileName)
    if int(board)==21:
        Qconv=0.59
        
    label="B"+str(board)+" ch"+str(ch)+" Vth="+str(thres)+" Vthc="+str(vthc)+" Q="+str(Q)

    #get data
    delayMap,dataMap,Nevts=readTOAFile(fileName,Qconv=Qconv,DelayStep=DelayStep)

    #loop over data
    nMax=0
    for delay in sorted(dataMap.keys()):

        #convert data to numpy array
        toaList=np.array(dataMap[delay])

        #extract information
        okTOA=toaList!=127 #used to remove saturated toa
        toaOKList=toaList[okTOA]#data without saturated toa

        #compute mean and jitter
        TOAMean=0
        jitter=0
        if len(toaList)>    nMax:
            nMax=len(toaList)
        if len(toaOKList)>10:#compute mean and jitter with at N events
            TOAMean=np.median(toaOKList)
            jitter=np.std(toaOKList)


        #store information in list
        toaMeanList.append(TOAMean)
        jitterList.append(jitter)
        delayList.append(delay)
        delayDACList.append(delayMap[delay])
        effList.append(len(toaOKList))
        for toa in toaList:
            allTOAList.append(toa)
            allDelayList.append(delay)

    #skip when no data
    if len(effList)==0: continue
    if nMax<0.5*Nevts: continue
    
    #convert to np array
    effArray=np.array(effList)/Nevts
    delayArray=np.array(delayList)
    toaMeanArray=np.array(toaMeanList)
    jitterArray=np.array(jitterList)
    allDelayArray=np.array(allDelayList)
    allTOAArray=np.array(allTOAList)

    # efficiency selection
    okEff=effArray>0.8
    try:
        delayMin=int(min(delayArray[okEff])*0.99)
        delayMax=int(max(delayArray[okEff])*1.01)
    except:
        delayMin=20000
        delayMax=25000
        
    #compute LSB from a fit
    #params, covariance = optimize.curve_fit(pol1, delayArray[okEff],toaMeanArray[okEff],p0=[1/20, 10000])#fit using scipy
    params=np.polyfit(delayArray[okEff],toaMeanArray[okEff], 1)
    LSBTOA=0
    if params[0]!=0:
        LSBTOA=abs(1/params[0])
    #compute TOA with the fit a given delay value
    TOARef=pol1(delayRef , params[0], params[1])*LSBTOA


    #compute local LSB
    if len(delayArray)<12: continue
    deltaT=delayArray[11]-delayArray[10]
    #localLSB=abs(1/(np.concatenate((np.ediff1d(toaMeanArray),np.zeros(1)))/deltaT))
    #localLSB=np.concatenate((abs(deltaT/np.ediff1d(toaMeanArray)),np.zeros(1)))
    localLSB=abs(deltaT/np.ediff1d(toaMeanArray))
    localLSB=np.concatenate((localLSB,np.zeros(1))) #add one dummy ele


    #TOA vs delay 2D Hist
    if options.bidim:
        xedges = range(delayMin,delayMax,10)
        yedges = range(0,128,1)
        HTOA, xedges, yedges = np.histogram2d(allDelayArray, allTOAArray, bins=(xedges, yedges))
        HTOA = HTOA.T  # Let each row list bins with common y range.
        HTOA[HTOA==0]=np.nan
        current_cmap = matplotlib.cm.get_cmap()
        current_cmap.set_bad(color='white')
        X, Y = np.meshgrid(xedges, yedges)        



    #save more data
    jitterMean=np.median(jitterArray[okEff])*LSBTOA
    QList[ch].append(Q)
    jitterMeanList[ch].append(jitterMean)


    #additionnal plot for one Q value
    if Q==options.QRef:
        counterColor+=1
        # plots with LSB applied
        fig, ax = plt.subplots(3,1)
        ax[0].plot(delayArray,effArray,label="eff")
        ax[0].set_ylabel("Efficiency", fontsize = 10)
        ax[0].set_title('Qdac='+str(options.QRef), fontsize = 11)
        ax[1].plot(delayArray,toaMeanArray*LSBTOA,label="TOA")
        ax[1].set_ylabel("<TOA> [ps]", fontsize = 10)
        ax[2].plot(delayArray,jitterArray*LSBTOA,label="Jitter")
        ax[2].set_ylabel("jitter [ps]", fontsize = 10)
        ax[2].set_xlabel("Delay [ps]", fontsize = 10)
        if options.allPlots:plt.savefig("TOA_"+os.path.basename(fileName)+"_All.pdf")
        plt.close()

        # TOA mean only without LSB applied
        figTOA=plt.figure(figsize=(6,6))
        gs = gridspec.GridSpec(4,1)
        ax1 = plt.subplot(gs[:2, :])
        ax1.set_title('Qdac='+str(options.QRef), fontsize = 11)
        ax1.scatter(delayArray[okEff],toaMeanArray[okEff],label="TOA with eff cut", facecolors='none', edgecolors='green')
        ax1.plot(delayArray[okEff], pol1(delayArray[okEff], params[0], params[1]),label='pol1',color='r')
        if options.bidim:    ax1.pcolormesh(X, Y, HTOA,cmap=plt.cm.jet)
        ax1.set_ylabel("<TOA> [dac]", fontsize = 10)
        ax1.set_xlabel("Delay [ps]", fontsize = 10)
        ax1.set_xlim(left=delayMin)
        ax1.set_xlim(right=delayMax)
        ax1.text(0.8,0.8,'LSB='+str(round(LSBTOA,1))+"ps",horizontalalignment='center',verticalalignment='center', transform = ax1.transAxes)
        ax2 = plt.subplot(gs[2, :]) 
        ax2.scatter(delayArray[okEff],toaMeanArray[okEff]-pol1(delayArray[okEff], params[0], params[1]),label="TOA with eff cut", facecolors='none', edgecolors='green')
        ax2.set_xlim(left=delayMin)
        ax2.set_xlim(right=delayMax)
        ax2.set_ylabel("Fit residual", fontsize = 10)
        ax2.set_xlabel("Delay [ps]", fontsize = 10)
        ax3 = plt.subplot(gs[3, :]) 
        ax3.scatter(delayArray[okEff][:-1],localLSB[okEff][:-1],label="TOA with eff cut", facecolors='none', edgecolors='green')
        ax3.set_xlim(left=delayMin)
        ax3.set_xlim(right=delayMax)
        #ax3.set_ylim(top=40)
        ax3.set_ylim(bottom=0)
        ax3.set_ylabel("Local LSB [ps]", fontsize = 10)
        ax3.set_xlabel("Delay [ps]", fontsize = 10)
        if options.allPlots:plt.savefig("TOA_"+os.path.basename(fileName)+"_toaMean.pdf")
        plt.close()

        #print(localLSB[okEff])              
        #print(np.mean(localLSB[okEff][:-1]))              
        
        #comparison plots TOAMean
        plt.figure(figTOAMean.number)
        axTOAMean.scatter(delayArray[okEff],toaMeanArray[okEff]*LSBTOA,s=10,label=label              , color=colors[counterColor-1])#)

        #comparison plots Jitter
        plt.figure(figJitter.number)
        axJitter.scatter(delayArray[okEff],jitterArray[okEff]*LSBTOA,s=10,label=label              , color=colors[counterColor-1])#)

        #save some data
        LSBList.append(LSBTOA)
        chList.append(ch)
        JitterRefList.append(jitterMean)
        TOARefList.append(TOARef)



    #print
    #print (board,ch,cd,thres,vthc,Q,LSBTOA,jitterMean,TOARef)

#toaMean summary plot
plt.figure(figTOAMean.number)
axTOAMean.set_title('Qdac='+str(options.QRef), fontsize = 11)
#axToaMean.set_ylim(top=1.2)
axTOAMean.set_xlabel("Delay [ps]", fontsize = 10)
axTOAMean.set_ylabel("<TOA> [ps]", fontsize = 10)
plt.legend(loc='upper right', prop={"size":6})
plt.savefig("TOA_SummaryTOAMean.pdf")
#plt.savefig("TOA_SummaryTOAMean.png")


#jitter summary plot
plt.figure(figJitter.number)
axJitter.set_title('Qdac='+str(options.QRef), fontsize = 11)
axJitter.set_xlabel("Delay [ps]", fontsize = 10)
axJitter.set_ylabel("Jitter [ps]", fontsize = 10)
axJitter.set_ylim(top=100)
axJitter.set_ylim(bottom=0)
plt.legend(loc='upper right', prop={"size":6})
plt.savefig("TOA_SummaryJitter.pdf")

#convert to numpy array
jitterMeanArray=np.array(jitterMeanList)
QArray=np.array(QList)
chArray=np.array(chList)
LSBArray=np.array(LSBList)
TOARefArray=np.array(TOARefList)
JitterRefArray=np.array(JitterRefList)


#TOA vs channel
figTOARef=plt.figure('TOARef')
axTOARef = figTOARef.add_subplot(1,1,1)
axTOARef.set_title('Qdac='+str(options.QRef), fontsize = 11)
axTOARef.scatter(chArray,TOARefArray)
axTOARef.set_xlabel("Channel number", fontsize = 10)
axTOARef.set_ylabel("TOA for delay="+str(int(delayRef))+"ps [ps]", fontsize = 10)
plt.savefig("TOA_TOARefvsCh.pdf")

#Jitter vs channel
figJitterRef=plt.figure('JitterRef')
axJitterRef = figJitterRef.add_subplot(1,1,1)
axJitterRef.set_title('Qdac='+str(options.QRef), fontsize = 11)
axJitterRef.scatter(chArray,JitterRefArray)
axJitterRef.set_xlabel("Channel number", fontsize = 10)
axJitterRef.set_ylabel("Jitter for delay="+str(int(delayRef))+"ps [ps]", fontsize = 10)
plt.savefig("TOA_JitterRefvsCh.pdf")





#jitter vs Q
figjitterMean=plt.figure('jitterMean')
axjitterMean = figjitterMean.add_subplot(1,1,1)
for ich in range(nChannelsMax):
    axjitterMean.scatter(np.multiply(QArray[ich],Qconv),jitterMeanArray[ich],label="ch"+str(ich),color=colors[ich])
axjitterMean.set_xlabel("Injected charge [fC]", fontsize = 10)
axjitterMean.set_ylabel("Jitter [ps]", fontsize = 10)
jitterMax=max(max(jitterMeanArray))                 
axjitterMean.set_ylim(bottom=0,top=jitterMax*1.5)#np.max(jitterMeanArray[ich])*1.5)
axjitterMean.set_xlim(left=0,right=45)#np.max(jitterMeanArray[ich])*1.5)
plt.legend(loc='upper right', prop={"size":6})
plt.savefig("TOA_jitterMeanvsQ.pdf")



#LSB vs channel
figLSB=plt.figure('LSB')
axLSB = figLSB.add_subplot(1,1,1)
axLSB.set_title('Qdac='+str(options.QRef), fontsize = 11)
axLSB.scatter(chArray,LSBArray)
axLSB.set_xlabel("Channel nb", fontsize = 10)
axLSB.set_ylabel("LSB", fontsize = 10)
plt.savefig("TOA_LSBvsCh.pdf")

#display figures
if options.display:
    plt.show()