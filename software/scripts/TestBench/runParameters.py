doThres     = 0
doNoise     = 0 # Thres with high stat for few Q
doLinearity = 0 # Thres for many Q
doVthcScan  = 0

doTW        = 0
doTWdelay   = 0
doTWscan    = 0
doPS        = 0 # TW with thres. scan
doPSdelay   = 1 # TW with thres. scan

doTOA       = 0
doClockTree = 0 # TOA with at least Q=63 and maybe larger N
doDNL       = 0 # TOA step=1
doXtalk     = 0 # TOA Channels should be ON

doVthcScan=0

#ch list
chList=None
#chList=[4,9]#,14,19,24]#,19,24]
chList=[3]#,3,6,10]#B29
#chList=[1,3,7,15,17]#B13
#chList=[0]
#chList=range(0,25)



#cd list 
cdZeroForASICAlone=True #overwritten to 0 for sensor boards
cdList=[4,7]


doFullQScanForTOA = 0
QTOAList=[]  #v2:5,7,13  v3:6,9,16
#QTOAList=[7,13,26]#v2
QTOAList=[6,9,16]#v3

QThresList=[3,4]#default
#QThresList=[4]









#special settings
Rin_Vpa=0
ON_rtest=0
#toa_busy=0



prefix=None
#prefix="Cp7WithProbePA"
#prefix="Cp7"

dacOffset=0
