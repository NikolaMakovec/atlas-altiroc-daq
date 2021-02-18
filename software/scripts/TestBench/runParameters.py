doThres     = 0
doNoise     = 0 # Thres with high stat for few Q
doLinearity = 0 # Thres for many Q

doTW        = 1
doTWdelay   = 0
doTWscan    = 0
doPS        = 0 # TW with thres. scan
doPSdelay   = 0 # TW with thres. scan

doTOA       = 0
doClockTree = 0 # TOA with at least Q=63 and maybe larger N
doDNL       = 0 # TOA step=1
doXtalk     = 0 # TOA Channels should be ON

doVthcScan=0

#ch list
chList=None
#chList=[0,3,6,10]#B29
#chList=[3,6,10,19]#B28
#chList=[7,21,3,17,13]#B13 TB
#chList=[1,15,16,17,0,4]
#chList=range(0,25)

#cd list 
cdZeroForASICAlone=True #overwritten to 0 for sensor boards
cdList=[4]

#TOA
doFullQScanForTOA = 0
QTOAList=[7,8,63]#6,9,16]  #v2:5,7,13,63  v3:6,9,16,63


#THRES
QThresList=[3,4]#default
QThresList=[7,13]#B13 TB


#special settings
Rin_Vpa=0
ON_rtest=0
#toa_busy=0

prefix=None
#prefix="Cp7WithProbePA"
#prefix="Cp7"

dacOffset=10
