boardASICAlone=[4,8,9,10,11,12,14,15,21,24,31]
boardASICV2=[3,4,8,9,10,11,12,13,14,15,44,100]
boardASICV3=[21,24,27,28,29,31,45,102]
boardASICV3b=[]

def getASICVersion(board):
    version=3
    if board in boardASICV2: version=2
    return version


def Qconv(board):
    board=int(board)
    qconvV2=10/13.
    qconvV3=0.61
    qconv=0
    if getASICVersion(board)==3:
        qconv=qconvV3
    elif getASICVersion(board)==2:
        qconv=qconvV2
        
    return qconv
    
def isTZ(board,channel):
    if  getASICVersion(int(board))==2 and int(channel)>=15:
        return True
    else: return False