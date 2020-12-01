doThres     = 0
doNoise     = 0 # Thres with high stat for few Q
doLinearity = 0 # Thres for many Q
doVthcScan  = 0

doTW        = 1
doTWscan    = 0
doPS        = 0 # TW with thres. scan

doTOA       = 0
doClockTree = 0 # TOA with at least Q=63 and maybe larger N
doDNL       = 0 # TOA step=1
doXtalk     = 0 # TOA Channels should be ON

#ch list
chList=None
#chList=[4,9,14,19,24]
#chList=[15]#,23,1,8,17]
#chList=range(0,25)
#chList=range(25)

delayList=[]
delayList=range(2300,2500+1,50)

#cd list 
cdZeroForASICAlone=True #overwritten to 0 for sensor boards
cdList=[4]
#cdList=range(0,4+1)

QTOAList=[5]#6,7,16,63]#default
#QTOAList=[3,4,5,6,9,13,26,63]#v2
#QTOAList=[4,5,6,8,12,16,24,32,63]#v3
QThresList=[3]#default
#QThresList=[4]


#special settings
Rin_Vpa=0
ON_rtest=0
#toa_busy=0



prefix=None
#prefix="Cp7WithProbePA"
#prefix="Cp7"

dacOffset=5
