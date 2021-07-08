doThres     = 0
doNoise     = 0 # Thres with high stat for few Q
doPedestal  = 0
doLinearity = 0 # Thres for many Q
doVthcScan  = 0

doTW        = 0
doTWHS      = 1
doTWdelay   = 0
doTWscan    = 0
doPS        = 0 # TW with thres. scan
doPSdelay   = 0 # TW with thres. scan

doTOA       = 0
doClockTree = 0 # TOA with at least Q=63 and maybe larger N
doDNL       = 0 # TOA step=1
doXtalk     = 0 # TOA Channels should be ON



#ch list
chList=None
#chList=[0,3,6,10]#B29
#chList=[3,6,10,19]#B28
#chList=[7,21,3,17,13]#B13 TB
#chList=[1,15,16,17,0,4]
chList=range(0,25)
#chList=[4]
#chList=[1,4,6,11,16,21]#  0,2,3]
#chList=[0,1,2,3,4,15,16,17,18,19]
#chList=[1]

#cd list 
cdZeroForASICAlone=True #overwritten to 0 for sensor boards
cdList=[4]

#TOA
doFullQScanForTOA = 0
#QTOAList=[6,7,9,16,63]#6,9,16]  #v2:5,7,13,63  v3:6,7,8,9,16,63
#QTOAList=[6,9,16,32,45,63]  #v2:5,7,13,63  v3:6,9,16,63
QTOAList=[5,6,7,8,9,10,12,16,63]
QTOAList=[10]
#QTOAList=[6,7,8,9,16,63]  #v2:5,7,13,63  v3:6,9,16,63

#THRES
QThresList=[4]#default
#QThresList=[3,4,5,6,13]#default
#QThresList=[7,13]#B13 TB


#special settings
dac_biaspa=2+0
Rin_Vpa=0
ON_rtest=1
#toa_busy=0

prefix=None
#prefix="Cp7WithProbePA"
#prefix="Cp7"

dacOffset=0
