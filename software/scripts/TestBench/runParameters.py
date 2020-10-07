
doSepDir = 1

doThres     = 1
doNoise     = 0 # Thres with high stat for few Q
doLinearity = 0 # Thres for many Q
doVthcScan  = 0


doTW        = 0
doPS        = 0 # TW with thres. scan

doTOA       = 0
doClockTree = 0 # TOA with at least Q=63 and maybe larger N
doDNL       = 0 # TOA step=1
doXtalk     = 0 # TOA Channels should be ON

#ch list
chList=None
#chList=range(25)
#chList=range(20,25)
#chList=range(22,25)


#cd list 
cdZeroForASICAlone=True #overwritten to 0 for sensor boards
cdList=[6,7]
#cdList=[1]
#cdList=range(0,4+1)

#special settings
Rin_Vpa=0
ON_rtest=0
