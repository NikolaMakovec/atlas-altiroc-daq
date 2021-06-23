def getDACList(board):
    dacList={}
    if board==2:
        dacList[(2,5,0)]=350
        dacList[(2,6,0)]=360
        dacList[(2,7,0)]=350
        dacList[(2,8,0)]=330
        dacList[(2,10,0)]=380
        dacList[(2,12,0)]=320
        dacList[(2,13,0)]=340
        dacList[(2,14,0)]=330
    elif board==3:

        # ###dacList[(3,0,0)]=99#3,0.00,ok 
        # dacList[(3,10,0)]=312#3,0.96,ok 
        # dacList[(3,11,0)]=348#3,0.98,ok 
        # dacList[(3,12,0)]=334#3,0.98,ok 
        # dacList[(3,13,0)]=352#3,0.98,ok 
        # ####dacList[(3,14,0)]=99#3,0.00,ok 
        # dacList[(3,1,0)]=382#3,0.99,ok 
        # dacList[(3,2,0)]=286#3,1.00,ok 
        # dacList[(3,3,0)]=322#3,0.97,ok 
        # dacList[(3,4,0)]=296#3,0.95,ok 
        # dacList[(3,5,0)]=350#3,0.95,ok 
        # dacList[(3,6,0)]=336#3,0.95,ok 
        # dacList[(3,7,0)]=314#3,0.65,PRB!!!!!!!!! 
        # dacList[(3,8,0)]=330#3,0.96,ok 
        # ###dacList[(3,9,0)]=422#3,0.53,PRB!!!!!!!!! 
        # dacList[(3,15,0)]=358#3,0.99,ok 
        # #dacList[(3,16,0)]=338#3,0.95,ok prb TDC???
        # dacList[(3,17,0)]=348#3,0.99,ok
        # dacList[(3,18,0)]=352#3,0.99,ok
        # ###dacList[(3,19,0)]= essayer larger Q
        # dacList[(3,20,0)]=378#3,0.96,ok 
        # dacList[(3,21,0)]=414#4,0.95,ok
        # dacList[(3,22,0)]=348#3,0.96,ok
        # dacList[(3,23,0)]=356#3,0.97,ok 
        # ####dacList[(3,24,0)]=99#4,0.00,ok  essayer larger Q
        
        #dacList[(3,0,0)]=127#thres2 3,1.00,0,ok      FlatPlot
        dacList[(3,10,0)]=318#thres2 3,0.02,0,ok 
        dacList[(3,11,0)]=352#thres2 3,0.00,0,ok 
        dacList[(3,12,0)]=340#thres2 3,0.02,0,ok 
        dacList[(3,13,0)]=358#thres2 3,0.02,0,ok 
        #dacList[(3,14,0)]=127#thres2 3,0.96,343,diff. thres
        dacList[(3,14,0)]=482#thres2 9,0.00,0,ok
        dacList[(3,15,0)]=356#thres2 3,0.04,0,ok 
        dacList[(3,16,0)]=334#thres2 3,0.04,0,ok 
        dacList[(3,17,0)]=344#thres2 3,0.06,4,ok 
        dacList[(3,18,0)]=350#thres2 3,0.04,0,ok 
        #dacList[(3,19,0)]=127#thres2 3,1.00,253,diff. thres
        dacList[(3,19,0)]=390#thres2 7,0.00,0,ok 
        dacList[(3,1,0)]=390#thres2 3,0.04,0,ok 
        #dacList[(3,20,0)]=127#thres2 3,0.16,249,diff. thres
        dacList[(3,20,0)]=384#thres1 5,0.02,0,ok 
        #dacList[(3,21,0)]=127#thres2 3,0.82,281,diff. thres
        dacList[(3,21,0)]=422#thres1 5,0.04,0,ok 
        dacList[(3,22,0)]=346#thres2 3,0.10,2,ok 
        #dacList[(3,23,0)]=127#thres2 3,0.32,225,diff. thres
        dacList[(3,23,0)]=366#thres1 5,0.02,0,ok 
        #dacList[(3,24,0)]=127#thres2 3,1.00,185,diff. thres
        dacList[(3,24,0)]=324#thres1 7,0.04,0,ok
        dacList[(3,2,0)]=288#thres2 3,0.00,0,ok 
        dacList[(3,3,0)]=326#thres2 3,0.02,0,ok 
        dacList[(3,4,0)]=302#thres2 3,0.04,0,ok 
        dacList[(3,5,0)]=352#thres2 3,0.00,0,ok 
        dacList[(3,6,0)]=340#thres2 3,0.10,2,ok 
        dacList[(3,7,0)]=318#thres2 3,0.02,0,ok 
        dacList[(3,8,0)]=334#thres2 3,0.02,0,ok 
        #dacList[(3,9,0)]=127#thres2 3,1.00,671,diff. thres    ALWAYS TRIGGERTING

        
    elif board==8:




        dacList[(8,0,4)]=410#thres2 3,0.02,0,ok 
        dacList[(8,10,4)]=424#thres2 3,0.04,0,ok 
        dacList[(8,11,4)]=416#thres2 3,0.02,0,ok 
        dacList[(8,12,4)]=386#thres2 3,0.00,0,ok 
        #dacList[(8,13,4)]=127#thres2 3,0.80,309,diff. thres BAD TDC?
        #dacList[(8,14,4)]=127#thres2 3,1.00,161,diff. thres
        dacList[(8,14,4)]=292#thres2 4,0.08,2,ok 
        dacList[(8,15,4)]=360#thres2 3,0.02,0,ok 
        dacList[(8,16,4)]=396#thres2 3,0.00,0,ok 
        dacList[(8,17,4)]=372#thres2 3,0.00,0,ok 
        #dacList[(8,18,4)]=794#thres2 3,0.04,0,ok BAD TDC?
        #dacList[(8,19,4)]=127#thres2 3,1.00,195,diff. thres
        dacList[(8,19,4)]=328+5#thres2 6,0.04,0,ok 
        dacList[(8,1,4)]=404#thres2 3,0.00,0,ok 
        dacList[(8,20,4)]=340#thres2 3,0.02,0,ok 
        dacList[(8,21,4)]=370#thres2 3,0.02,0,ok 
        dacList[(8,22,4)]=330#thres2 3,0.00,0,ok 
        dacList[(8,23,4)]=334#thres2 3,0.00,0,ok 
        dacList[(8,24,4)]=332+15#thres2 3,1.00,4,ok 
        dacList[(8,2,4)]=338#thres2 3,0.14,2,ok 
        dacList[(8,3,4)]=410#thres2 3,0.00,0,ok 
        dacList[(8,4,4)]=348#thres2 3,0.02,0,ok 
        dacList[(8,5,4)]=406#thres2 3,0.02,0,ok 
        #dacList[(8,6,4)]=368#thres2 3,0.22,18,diff. thres BAD TDC?
        dacList[(8,7,4)]=352#thres2 3,0.06,2,ok 
        dacList[(8,8,4)]=402#thres2 3,0.00,0,ok 
        dacList[(8,9,4)]=294#thres2 3,0.02,0,ok 
        
    

    elif board==9:
        dacList[(9,0,4)]=416#B9,3,1.00,ok 
        dacList[(9,10,4)]=420#B9,3,0.99,ok 
        dacList[(9,1,4)]=408#B9,3,0.97,ok 
        dacList[(9,2,4)]=410#B9,3,0.99,ok 
        dacList[(9,3,4)]=446#B9,3,0.99,ok 
        dacList[(9,4,4)]=306#B9,3,0.96,ok 
        dacList[(9,5,4)]=420#B9,3,0.96,ok 
        dacList[(9,6,4)]=396#B9,3,0.96,ok 
        dacList[(9,7,4)]=482#B9,3,0.98,ok 
        dacList[(9,8,4)]=420#B9,3,0.98,ok 
        dacList[(9,9,4)]=348#B9,3,1.00,ok
        #dacList[(9,11,4)]=1020#B9,3,0.99,ok AMWAYS TRIGGERING
        dacList[(9,12,4)]=456#B9,3,1.00,ok 
        dacList[(9,13,4)]=382#B9,3,0.99,ok 
        dacList[(9,14,4)]=348#B9,5,0.97,ok 
        pass
    elif board==10:
        dacList[(10,0,4)]=458#3,0.97,ok 
        dacList[(10,1,4)]=396#3,0.98,ok 
        dacList[(10,2,4)]=428#3,0.99,ok 
        dacList[(10,3,4)]=402#3,1.00,ok 
        dacList[(10,4,4)]=322#3,0.99,ok 
        dacList[(10,5,4)]=354#3,1.00,ok 
        dacList[(10,6,4)]=412#3,0.95,ok 
        dacList[(10,7,4)]=352#3,1.00,ok 
        dacList[(10,8,4)]=402#3,1.00,ok 
        dacList[(10,9,4)]=330#3,0.96,ok
        dacList[(10,10,4)]=384#3,1.00,ok 
        #dacList[(10,11,4)]=1022#3,1.00,ok
        dacList[(10,12,4)]=358#3,0.99,ok 
        dacList[(10,13,4)]=408#3,0.96,ok 
        dacList[(10,14,4)]=326#5,0.89,ok

        dacList[(10,19,4)]=318#5,0.93,ok 
        dacList[(10,24,4)]=314#5,0.80,PRB!!!!!!!!! 
        
        pass
    elif board==11:
        dacList[(11,0,4)]=390#3,1.00,ok 
        dacList[(11,1,4)]=406#3,1.00,ok 
        #dacList[(11,2,4)]=1022#3,0.12,PRB!!!!!!!!! 
        dacList[(11,3,4)]=442#3,0.97,ok 
        dacList[(11,4,4)]=374#3,0.99,ok 
        dacList[(11,5,4)]=514#3,0.96,ok 
        dacList[(11,6,4)]=408#3,0.95,ok 
        dacList[(11,7,4)]=398#3,0.97,ok 
        dacList[(11,8,4)]=426#3,1.00,ok 
        dacList[(11,9,4)]=368#3,1.00,ok 
        dacList[(11,10,4)]=410#3,0.97,ok
        dacList[(11,11,4)]=428#3,0.99,ok 
        dacList[(11,12,4)]=412#3,0.96,ok
        dacList[(11,13,4)]=410#3,0.99,ok 
        dacList[(11,14,4)]=342#5,0.97,ok 
        pass
        
    elif board==12:#cd4
        # dacList[(12,0,4)]=400#3,0.97,ok 
        # dacList[(12,1,4)]=380#3,0.99,ok 
        # dacList[(12,2,4)]=348#3,0.97,ok 
        dacList[(12,3,4)]=402#3,0.97,ok 
        # dacList[(12,4,4)]=326#3,1.00,ok 
        # dacList[(12,5,4)]=426#3,0.97,ok 
        # dacList[(12,6,4)]=396#3,0.98,ok 
        # dacList[(12,7,4)]=400#3,0.99,ok 
        # dacList[(12,8,4)]=380#3,1.00,ok 
        # dacList[(12,9,4)]=346#3,0.97,ok
        # dacList[(12,10,4)]=394#3,0.98,ok 
        # dacList[(12,11,4)]=380#3,0.99,ok 
        # #dacList[(12,12,4)]=1022#3,1.00,ok 
        # dacList[(12,13,4)]=416#3,0.97,ok 
        # dacList[(12,14,4)]=360#5,0.98,ok 

        dacList[(12,4,4)]=328#3,0.98,ok 
        dacList[(12,9,4)]=346#3,0.99,ok 
        dacList[(12,14,4)]=360#5,1.00,ok 
        dacList[(12,19,4)]=338#5,0.99,ok
        dacList[(12,24,4)]=366#5,1.00,ok 

        pass
    elif board==13:

        # dacList[(13,0,0)]=322#3,0.98,ok 
        # dacList[(13,10,0)]=316#3,1.00,ok 
        # dacList[(13,11,0)]=338#3,0.95,ok 
        # dacList[(13,12,0)]=358#3,0.95,ok 
        # dacList[(13,13,0)]=344#3,0.97,ok 
        # #dacList[(13,14,0)]=99#3,0.00,ok 
        # dacList[(13,15,0)]=366#3,0.99,ok 
        # dacList[(13,16,0)]=316#3,0.96,ok 
        # dacList[(13,17,0)]=370#3,0.99,ok 
        # #dacList[(13,18,0)]=354#3,0.96,ok 
        # #dacList[(13,19,0)]=99#3,0.00,ok 
        # dacList[(13,1,0)]=304#3,0.99,ok 
        # dacList[(13,20,0)]=336#3,0.99,ok 
        # dacList[(13,21,0)]=334#3,0.98,ok 
        # dacList[(13,22,0)]=406#3,0.95,ok 
        # dacList[(13,23,0)]=376#3,0.88,ok 
        # #dacList[(13,24,0)]=99#3,0.00,ok 
        # dacList[(13,2,0)]=326#3,0.99,ok 
        # dacList[(13,3,0)]=316#3,0.98,ok 
        # dacList[(13,4,0)]=296#3,0.98,ok 
        # dacList[(13,5,0)]=384#3,1.00,ok 
        # #dacList[(13,6,0)]=598#3,0.99,ok 
        # dacList[(13,7,0)]=306#3,1.00,ok 
        # dacList[(13,8,0)]=336#3,0.97,ok 
        # dacList[(13,9,0)]=314#3,0.97,ok 


        dacList[(13,0,0)]=316#thres2 3,0.06,2,ok 
        dacList[(13,10,0)]=310#thres2 3,0.24,6,diff. thres 
        dacList[(13,11,0)]=334#thres2 3,0.00,0,ok 
        dacList[(13,12,0)]=356#thres2 3,0.02,0,ok 
        dacList[(13,13,0)]=340#thres2 3,0.02,0,ok 
        #dacList[(13,14,0)]=127#thres2 3,1.00,203,diff. thres
        dacList[(13,14,0)]=334+5#thres2 5,0.28,2,ok 
        dacList[(13,15,0)]=360+5#thres2 3,0.02,0,ok 
        dacList[(13,16,0)]=310+5#thres2 3,0.02,0,ok 
        #dacList[(13,17,0)]=127#thres2 3,0.06,239,diff. thres
        dacList[(13,17,0)]=366+5#thres1 3,0.06,239,diff. thres 
        #dacList[(13,18,0)]=350#thres2 3,0.00,0,ok               BAD TDC
        #dacList[(13,19,0)]=127#thres2 3,1.00,211,diff. thres    BAD TDC
        dacList[(13,1,0)]=294#thres2 3,0.40,6,diff. thres 
        dacList[(13,20,0)]=332+5#thres2 3,0.00,0,ok
        #dacList[(13,21,0)]=127#thres2 3,0.06,201,diff. thres
        dacList[(13,21,0)]=328+5#thres1 3,0.06,201,diff. thres
        #dacList[(13,22,0)]=127#thres2 3,0.34,273,diff. thres
        dacList[(13,22,0)]=400+5#thres1 3,0.34,273,diff. thres
        #dacList[(13,23,0)]=127#thres2 3,0.08,245,diff. thres        
        dacList[(13,23,0)]=372+5#thres1 3,0.08,245,diff. thres
        #dacList[(13,24,0)]=127#thres2 3,1.00,201,diff. thres
        dacList[(13,24,0)]=328+10#thres1 3,1.00,201,diff. thres
        #dacList[(13,2,0)]=127#thres2 3,0.36,195,diff. thres
        dacList[(13,2,0)]=322#thres1 3,0.36,195,diff. thres
        #dacList[(13,3,0)]=127#thres2 3,0.58,187,diff. thres        
        dacList[(13,3,0)]=314#thres1 3,0.58,187,diff. thres 
        dacList[(13,4,0)]=292#thres2 3,0.26,2,ok 
        dacList[(13,5,0)]=378#thres2 3,0.24,2,ok 
        #dacList[(13,6,0)]=798#thres2 3,0.02,0,ok  BAD TDC
        dacList[(13,7,0)]=302#thres2 3,0.00,0,ok 
        dacList[(13,8,0)]=332#thres2 3,0.20,2,ok 
        dacList[(13,9,0)]=310#thres2 3,0.24,2,ok 



        
    elif board==14:
        #dacList[(14,0,4)]=1022#3,1.00,ok 
        dacList[(14,1,4)]=728#3,0.95,ok 
        #dacList[(14,2,4)]=1022#3,1.00,ok 
        dacList[(14,3,4)]=912#3,0.91,ok 
        dacList[(14,4,4)]=636#3,0.96,ok 
        #dacList[(14,5,4)]=1022#3,1.00,ok 
        dacList[(14,6,4)]=622#3,0.99,ok 
        #dacList[(14,7,4)]=1022#3,1.00,ok 
        dacList[(14,8,4)]=478#3,0.94,ok 
        dacList[(14,9,4)]=678#3,0.89,ok 
        #dacList[(14,10,4)]=1022#3,1.00,ok 
        #dacList[(14,11,4)]=1022#3,1.00,ok 
        dacList[(14,12,4)]=660#3,0.97,ok 
        dacList[(14,13,4)]=732#3,0.91,ok 
        #dacList[(14,14,4)]=592#3,0.65,PRB!!!!!!!!!    
        dacList[(14,14,4)]=676#5,0.02,PRB!!!!!!!!! 
        pass
    elif board==15:
        pass
    elif board==18:
        pass
    elif board==21:

        # dacList[(21,0,4)]=314#4,0.95,ok 
        # dacList[(21,0,5)]=310#4,0.92,ok 
        # dacList[(21,0,6)]=308#4,0.91,ok 
        # dacList[(21,0,7)]=306#4,0.87,ok 
        # dacList[(21,10,4)]=296#4,0.87,ok 
        # dacList[(21,10,5)]=292#4,0.87,ok 
        # dacList[(21,10,6)]=290#4,0.67,PRB!!!!!!!!! 
        # dacList[(21,10,7)]=288#4,0.79,PRB!!!!!!!!! 
        # # dacList[(21,11,4)]=336#4,0.67,PRB!!!!!!!!! 
        # # dacList[(21,11,5)]=332#4,0.55,PRB!!!!!!!!! 
        # # dacList[(21,11,6)]=330#4,0.55,PRB!!!!!!!!! 
        # # dacList[(21,11,7)]=326#4,0.68,PRB!!!!!!!!! 
        # dacList[(21,12,4)]=304#4,1.00,ok 
        # dacList[(21,12,5)]=300#4,0.99,ok 
        # dacList[(21,12,6)]=298#4,0.89,ok 
        # dacList[(21,12,7)]=296#4,0.84,ok 
        # dacList[(21,13,4)]=314#4,0.96,ok 
        # dacList[(21,13,5)]=308#4,0.94,ok 
        # dacList[(21,13,6)]=304#4,0.89,ok 
        # dacList[(21,13,7)]=300#4,1.00,ok 
        # dacList[(21,14,4)]=314#4,1.00,ok 
        # dacList[(21,14,5)]=310#4,0.98,ok 
        # dacList[(21,14,6)]=306#4,0.98,ok 
        # dacList[(21,14,7)]=304#4,0.98,ok 
        # dacList[(21,15,4)]=324#4,0.89,ok 
        # dacList[(21,15,5)]=320#4,0.90,ok 
        # dacList[(21,15,6)]=316#4,0.87,ok 
        # dacList[(21,15,7)]=314#4,0.83,ok 
        # # dacList[(21,16,4)]=598#4,0.99,ok 
        # # dacList[(21,16,5)]=598#4,1.00,ok 
        # # dacList[(21,16,6)]=598#4,1.00,ok 
        # # dacList[(21,16,7)]=598#4,0.99,ok 
        # dacList[(21,17,4)]=358#4,1.00,ok 
        # dacList[(21,17,5)]=354#4,0.92,ok 
        # dacList[(21,17,6)]=350#4,0.79,PRB!!!!!!!!! 
        # dacList[(21,17,7)]=348#4,0.55,PRB!!!!!!!!! 
        # dacList[(21,18,4)]=338#4,0.98,ok 
        # dacList[(21,18,5)]=332#4,0.98,ok 
        # dacList[(21,18,6)]=330#4,0.84,ok 
        # dacList[(21,18,7)]=326#4,0.98,ok 
        # dacList[(21,19,4)]=328#4,0.95,ok 
        # dacList[(21,19,5)]=322#4,0.96,ok 
        # dacList[(21,19,6)]=318#4,0.97,ok 
        # dacList[(21,19,7)]=316#4,0.93,ok 
        # dacList[(21,1,4)]=336#4,0.90,ok 
        # dacList[(21,1,5)]=332#4,0.89,ok 
        # dacList[(21,1,6)]=330#4,0.71,PRB!!!!!!!!! 
        # dacList[(21,1,7)]=326#4,0.99,ok 
        # dacList[(21,24,4)]=320#4,1.00,ok 
        # dacList[(21,24,5)]=316#4,1.00,ok 
        # dacList[(21,24,6)]=314#4,0.98,ok 
        # dacList[(21,24,7)]=314#4,0.97,ok 
        # dacList[(21,2,4)]=324#4,0.98,ok 
        # dacList[(21,2,5)]=320#4,0.97,ok 
        # dacList[(21,2,6)]=316#4,0.89,ok 
        # dacList[(21,2,7)]=314#4,0.81,ok 
        # dacList[(21,3,4)]=332#4,0.99,ok 
        # dacList[(21,3,5)]=328#4,0.97,ok 
        # dacList[(21,3,6)]=326#4,0.95,ok 
        # dacList[(21,3,7)]=324#4,0.88,ok 
        # dacList[(21,4,4)]=324#4,0.98,ok 
        # dacList[(21,4,5)]=316#4,0.98,ok 
        # dacList[(21,4,6)]=310#4,0.99,ok 
        # dacList[(21,4,7)]=308#4,0.93,ok 
        # dacList[(21,5,4)]=306#4,1.00,ok 
        # dacList[(21,5,5)]=304#4,0.89,ok 
        # dacList[(21,5,6)]=300#4,0.87,ok 
        # dacList[(21,5,7)]=298#4,0.95,ok 
        # dacList[(21,6,4)]=320#4,0.98,ok 
        # dacList[(21,6,5)]=316#4,0.96,ok 
        # dacList[(21,6,6)]=364#4,0.96,ok 
        # dacList[(21,6,7)]=312#4,0.95,ok 
        # dacList[(21,7,4)]=330#4,0.91,ok 
        # dacList[(21,7,5)]=326#4,0.90,ok 
        # dacList[(21,7,6)]=324#4,0.84,ok 
        # dacList[(21,7,7)]=322#4,0.82,ok 
        # dacList[(21,8,4)]=326#4,0.96,ok 
        # dacList[(21,8,5)]=322#4,0.97,ok 
        # dacList[(21,8,6)]=316#4,0.98,ok 
        # dacList[(21,8,7)]=314#4,0.93,ok 
        # dacList[(21,9,4)]=324#4,0.97,ok 
        # dacList[(21,9,5)]=312#4,1.00,ok 
        # dacList[(21,9,6)]=308#4,1.00,ok 
        # dacList[(21,9,7)]=304#4,1.00,ok 

        dacList[(21,0,4)]=310#thres2 4,0.12,2,ok 
        dacList[(21,10,4)]=292#thres2 4,0.78,4,ok 
        #dacList[(21,11,4)]=326#thres2 4,0.90,12,diff. thres 
        dacList[(21,12,4)]=302#thres2 4,0.56,4,ok 
        dacList[(21,13,4)]=312#thres2 4,0.12,2,ok 
        dacList[(21,14,4)]=314#thres2 4,0.04,0,ok 
        dacList[(21,15,4)]=320#thres2 4,0.26,2,ok 
        #dacList[(21,16,4)]=798#thres2 4,0.00,0,ok 
        dacList[(21,17,4)]=356#thres2 4,0.44,4,ok 
        dacList[(21,18,4)]=334#thres2 4,0.32,4,ok 
        dacList[(21,19,4)]=324#thres2 4,0.12,2,ok 
        dacList[(21,1,4)]=332#thres2 4,0.88,4,ok 
        dacList[(21,20,4)]=380#thres2 4,0.00,0,ok 
        #dacList[(21,21,4)]=798#thres2 4,0.00,0,ok 
        dacList[(21,22,4)]=422#thres2 4,0.08,2,ok 
        dacList[(21,23,4)]=364#thres2 4,0.00,0,ok 
        dacList[(21,24,4)]=318#thres2 4,0.00,0,ok 
        dacList[(21,2,4)]=320#thres2 4,0.68,4,ok 
        dacList[(21,3,4)]=330#thres2 4,0.26,2,ok 
        dacList[(21,4,4)]=322#thres2 4,0.16,2,ok 
        dacList[(21,5,4)]=304#thres2 4,0.58,4,ok 
        #dacList[(21,6,4)]=314#thres2 4,0.16,8,diff. thres 
        dacList[(21,7,4)]=324#thres2 4,0.78,4,ok 
        dacList[(21,8,4)]=324#thres2 4,0.32,2,ok 
        dacList[(21,9,4)]=322#thres2 4,0.04,0,ok 
        pass
        



    elif board==24:
        dacList[(24,0,4)]=296#3,0.98,ok 
        dacList[(24,10,4)]=278#3,0.94,ok 
        dacList[(24,11,4)]=330#3,0.98,ok 
        dacList[(24,12,4)]=326#3,0.94,ok 
        dacList[(24,13,4)]=304#3,0.94,ok 
        #dacList[(24,14,4)]=270#3,0.99,ok 
        dacList[(24,15,4)]=268#3,0.99,ok 
        dacList[(24,16,4)]=302#3,0.96,ok 
        dacList[(24,17,4)]=292#3,1.00,ok 
        dacList[(24,18,4)]=302#3,1.00,ok 
        dacList[(24,19,4)]=254#3,1.00,ok 
        dacList[(24,1,4)]=312#3,1.00,ok 
        # dacList[(24,20,4)]=282#3,0.97,ok 
        # dacList[(24,21,4)]=332#3,0.98,ok 
        # dacList[(24,22,4)]=320#3,0.99,ok 
        # dacList[(24,23,4)]=334#3,0.96,ok 
        dacList[(24,24,4)]=254#3,0.99,ok 
        dacList[(24,2,4)]=292#3,1.00,ok 
        dacList[(24,3,4)]=302#3,0.99,ok 
        dacList[(24,4,4)]=278#3,0.96,ok 
        dacList[(24,5,4)]=290#3,0.98,ok 
        dacList[(24,6,4)]=272#3,1.00,ok 
        #dacList[(24,7,4)]=999#3,0.00,ok 
        dacList[(24,8,4)]=300#3,0.95,ok 
        dacList[(24,9,4)]=304#3,0.98,ok

        # dacList[(24,0,6)]=294#3,0.85,ok 
        # dacList[(24,10,6)]=272#3,0.96,ok 
        # dacList[(24,11,6)]=324#3,0.81,ok 
        # dacList[(24,12,6)]=320#3,0.90,ok 
        # dacList[(24,13,6)]=300#3,0.89,ok 
        # dacList[(24,15,6)]=264#3,0.98,ok 
        # dacList[(24,16,6)]=300#3,0.95,ok 
        # dacList[(24,17,6)]=288#3,0.88,ok 
        # dacList[(24,18,6)]=300#3,0.84,ok 
        # dacList[(24,19,6)]=252#3,0.95,ok 
        # dacList[(24,1,6)]=308#3,0.98,ok 
        # dacList[(24,24,6)]=254#3,0.98,ok 
        # dacList[(24,2,6)]=288#3,0.92,ok 
        # dacList[(24,3,6)]=298#3,0.93,ok 
        # dacList[(24,4,6)]=268#3,0.93,ok 
        # dacList[(24,5,6)]=288#3,0.83,ok 
        # dacList[(24,6,6)]=270#3,0.86,ok 
        # dacList[(24,8,6)]=294#3,0.95,ok 
        # dacList[(24,9,6)]=294#3,0.98,ok 
        
        dacList[(24,0,6)]=300#4,0.60,PRB!!!!!!!!! 
        dacList[(24,10,6)]=280#4,0.86,ok 
        dacList[(24,11,6)]=330#4,0.97,ok 
        dacList[(24,12,6)]=328#4,0.89,ok 
        dacList[(24,13,6)]=306#4,0.96,ok 
        dacList[(24,15,6)]=272#4,0.82,ok 
        dacList[(24,16,6)]=306#4,0.80,PRB!!!!!!!!! 
        dacList[(24,17,6)]=294#4,0.95,ok 
        dacList[(24,18,6)]=306#4,0.94,ok 
        dacList[(24,19,6)]=256#4,0.99,ok 
        dacList[(24,1,6)]=314#4,0.99,ok 
        dacList[(24,24,6)]=260#4,0.96,ok 
        dacList[(24,2,6)]=294#4,0.99,ok 
        dacList[(24,3,6)]=306#4,0.97,ok 
        dacList[(24,4,6)]=274#4,1.00,ok 
        dacList[(24,5,6)]=292#4,1.00,ok 
        dacList[(24,6,6)]=276#4,0.88,ok 
        dacList[(24,8,6)]=302#4,0.92,ok 
        dacList[(24,9,6)]=302#4,0.99,ok 
        
        
        # dacList[(24,0,7)]=292#3,0.94,ok 
        # dacList[(24,10,7)]=272#3,0.71,PRB!!!!!!!!! 
        # dacList[(24,11,7)]=322#3,0.79,PRB!!!!!!!!! 
        # dacList[(24,12,7)]=316#3,0.86,ok 
        # dacList[(24,13,7)]=298#3,0.88,ok 
        # dacList[(24,15,7)]=264#3,0.83,ok 
        # dacList[(24,16,7)]=300#3,0.55,PRB!!!!!!!!! 
        # dacList[(24,17,7)]=286#3,0.94,ok 
        # dacList[(24,18,7)]=298#3,0.81,ok 
        # dacList[(24,19,7)]=252#3,0.85,ok 
        # dacList[(24,1,7)]=308#3,0.87,ok 
        # dacList[(24,24,7)]=254#3,0.99,ok 
        # dacList[(24,2,7)]=286#3,0.99,ok 
        # dacList[(24,3,7)]=296#3,0.95,ok 
        # dacList[(24,4,7)]=264#3,1.00,ok 
        # dacList[(24,5,7)]=286#3,0.93,ok 
        # dacList[(24,6,7)]=268#3,0.83,ok 
        # dacList[(24,8,7)]=292#3,0.99,ok 
        # dacList[(24,9,7)]=292#3,0.93,ok 
        
        
        
        dacList[(24,0,7)]=298#4,0.94,ok 
        dacList[(24,10,7)]=278#4,0.82,ok 
        dacList[(24,11,7)]=328#4,0.93,ok 
        dacList[(24,12,7)]=324#4,0.98,ok 
        dacList[(24,13,7)]=304#4,0.95,ok 
        dacList[(24,15,7)]=270#4,0.85,ok 
        dacList[(24,16,7)]=304#4,0.84,ok 
        dacList[(24,17,7)]=292#4,0.99,ok 
        dacList[(24,18,7)]=304#4,0.89,ok 
        dacList[(24,19,7)]=254#4,0.99,ok 
        dacList[(24,1,7)]=314#4,0.91,ok 
        dacList[(24,24,7)]=258#4,0.97,ok 
        dacList[(24,2,7)]=292#4,0.98,ok 
        dacList[(24,3,7)]=302#4,0.99,ok 
        dacList[(24,4,7)]=272#4,0.98,ok 
        dacList[(24,5,7)]=292#4,0.88,ok 
        dacList[(24,6,7)]=274#4,0.87,ok 
        dacList[(24,8,7)]=300#4,0.95,ok 
        dacList[(24,9,7)]=298#4,1.00,ok
        



    elif board==27:
        # dacList[(27,20,0)]=266#3,0.82,ok 
        # dacList[(27,21,0)]=276#3,0.96,ok 
        # dacList[(27,22,0)]=264#3,0.56,PRB!!!!!!!!! 
        # dacList[(27,23,0)]=266#3,0.58,PRB!!!!!!!!! 
        # dacList[(27,24,0)]=238#3,0.71,PRB!!!!!!!!!

        #HV on -100V
        dacList[(27,20,0)]=272#4,0.99,ok 
        dacList[(27,21,0)]=282#4,0.98,ok 
        dacList[(27,22,0)]=272#4,0.93,ok 
        dacList[(27,23,0)]=274#4,0.95,ok 
        dacList[(27,24,0)]=244#4,0.98,ok


        #HV off
        # dacList[(27,20,0)]=272#5,0.99,ok 
        # dacList[(27,21,0)]=280#4,0.97,ok 
        # dacList[(27,22,0)]=284#4,0.97,ok 
        # dacList[(27,23,0)]=270#4,0.98,ok 
        # dacList[(27,24,0)]=242#4,0.96,ok

        dacList[(27,20,0)]=272#5,0.99,ok 
        dacList[(27,21,0)]=284#5,0.97,ok 
        dacList[(27,22,0)]=272#5,0.99,ok 
        dacList[(27,23,0)]=274#5,0.99,ok 
        dacList[(27,24,0)]=248#5,0.97,ok 
        pass

    elif board==28:

        #thres. without HV due a mistake
        # #dacList[(28,0,0)]=598#5,0.75,PRB!!!!!!!!! 
        # dacList[(28,10,0)]=308#5,0.56,PRB!!!!!!!!! 
        # dacList[(28,11,0)]=296#5,0.77,PRB!!!!!!!!! 
        # dacList[(28,12,0)]=310#5,0.85,ok 
        # dacList[(28,13,0)]=240#5,0.89,ok 
        # dacList[(28,14,0)]=240#5,1.00,ok 
        # dacList[(28,15,0)]=270#5,0.77,PRB!!!!!!!!! 
        # dacList[(28,16,0)]=300#5,0.80,PRB!!!!!!!!! 
        # #dacList[(28,17,0)]=99#5,0.00,ok 
        # dacList[(28,18,0)]=272#5,0.95,ok 
        # dacList[(28,19,0)]=266#5,0.98,ok 
        # dacList[(28,1,0)]=262#5,0.82,ok 
        # dacList[(28,20,0)]=296#5,0.95,ok 
        # #dacList[(28,21,0)]=594#5,0.59,PRB!!!!!!!!! 
        # #dacList[(28,22,0)]=598#5,0.97,ok 
        # dacList[(28,23,0)]=302#5,0.98,ok 
        # #dacList[(28,24,0)]=99#5,0.00,ok 
        # #dacList[(28,2,0)]=338#5,0.98,ok LOW EFF
        # dacList[(28,3,0)]=256#5,0.97,ok 
        # #dacList[(28,4,0)]=414#5,0.98,ok #NOT CONNECTED?
        # dacList[(28,5,0)]=306#5,0.85,ok 
        # dacList[(28,6,0)]=262#5,0.92,ok 
        # dacList[(28,7,0)]=298#5,0.82,ok 
        # dacList[(28,8,0)]=262#5,0.93,ok 
        # dacList[(28,9,0)]=266#5,0.70,PRB!!!!!!!!!


        #thres. with HV
        dacList[(28,10,0)]=310#5,0.57,PRB!!!!!!!!! 
        dacList[(28,11,0)]=296#5,0.84,ok 
        dacList[(28,12,0)]=312#5,0.77,PRB!!!!!!!!! 
        dacList[(28,13,0)]=242#5,0.71,PRB!!!!!!!!! 
        dacList[(28,14,0)]=244#5,0.75,PRB!!!!!!!!! 
        dacList[(28,15,0)]=272#5,0.73,PRB!!!!!!!!! 
        dacList[(28,16,0)]=302#5,0.98,ok 
        dacList[(28,18,0)]=276#5,0.59,PRB!!!!!!!!! 
        dacList[(28,19,0)]=270#5,0.94,ok 
        dacList[(28,1,0)]=264#5,0.62,PRB!!!!!!!!! 
        dacList[(28,20,0)]=298#5,0.92,ok 
        dacList[(28,23,0)]=306#5,0.98,ok 
        dacList[(28,3,0)]=260#5,0.52,PRB!!!!!!!!! 
        dacList[(28,5,0)]=308#5,0.64,PRB!!!!!!!!! 
        dacList[(28,6,0)]=264#5,0.82,ok 
        dacList[(28,7,0)]=300#5,0.69,PRB!!!!!!!!! 
        dacList[(28,8,0)]=264#5,0.76,PRB!!!!!!!!! 
        dacList[(28,9,0)]=268#5,0.60,PRB!!!!!!!!! 


        
    elif board==29: #13 is not bump-bonded
        # dacList[(29,0,0)]=330#4,0.91,ok 
        # dacList[(29,10,0)]=268#4,0.76,PRB!!!!!!!!! 
        # #dacList[(29,11,0)]=302#4,0.89,ok 
        # #dacList[(29,12,0)]=288#4,0.54,PRB!!!!!!!!! 
        # dacList[(29,15,0)]=302#4,0.69,PRB!!!!!!!!! 
        # #dacList[(29,16,0)]=304#4,0.60,PRB!!!!!!!!! 
        # #dacList[(29,17,0)]=286#4,0.59,PRB!!!!!!!!! 
        # dacList[(29,18,0)]=290#4,0.91,ok 
        # dacList[(29,20,0)]=322#4,0.96,ok 
        # dacList[(29,21,0)]=278#4,0.95,ok 
        # dacList[(29,22,0)]=312#4,0.97,ok 
        # dacList[(29,24,0)]=304#4,0.98,ok 
        # dacList[(29,2,0)]=320#4,0.86,ok 
        # #dacList[(29,3,0)]=296#4,0.93,ok 
        # dacList[(29,4,0)]=288#4,0.53,PRB!!!!!!!!! 
        # dacList[(29,6,0)]=306#4,0.80,PRB!!!!!!!!! 
        # #dacList[(29,7,0)]=278#4,0.99,ok 
        # #dacList[(29,8,0)]=314#4,0.88,ok 
        # dacList[(29,9,0)]=300#4,0.67,PRB!!!!!!!!!


        #Not connected
        # dacList[(29,3,0)]=372#thres2 4,0.06,2,ok
        # dacList[(29,7,0)]=336#thres2 4,0.00,0,ok 
        # dacList[(29,8,0)]=398#thres2 4,0.00,0,ok
        # dacList[(29,11,0)]=376#thres2 4,0.02,0,ok 
        # dacList[(29,12,0)]=350#thres2 4,0.00,0,ok
        # dacList[(29,13,0)]=358#thres2 4,0.04,0,ok
        # dacList[(29,16,0)]=368#thres2 4,0.22,2,ok
        # dacList[(29,17,0)]=332#thres2 4,0.06,2,ok 
        # dacList[(29,22,0)]=362#thres2 4,0.04,0,ok
                
        dacList[(29,0,0)]=324#thres2 4,0.46,6,diff. thres 
        #dacList[(29,10,0)]=127#thres2 4,0.88,147,diff. thres
        dacList[(29,10,0)]=274#thres1 4,0.88,147,diff. thres 
        #dacList[(29,14,0)]=394#thres2 4,1.00,404,diff. thres BAD TDC?
        dacList[(29,15,0)]=300#thres2 4,0.62,4,ok 
        dacList[(29,18,0)]=288#thres2 4,0.64,4,ok 
        #dacList[(29,19,0)]=798#thres2 4,0.02,0,ok BAD TDC? 
        #dacList[(29,1,0)]=798#thres2 4,0.02,0,ok  BAD TDC?
        dacList[(29,20,0)]=322#thres2 4,0.00,0,ok 
        dacList[(29,21,0)]=276#thres2 4,0.00,0,ok 
        #dacList[(29,23,0)]=BQD TDC
        dacList[(29,24,0)]=302#thres2 4,0.02,0,ok 
        dacList[(29,2,0)]=316#thres2 4,0.58,6,diff. thres 
        dacList[(29,4,0)]=282#thres2 4,0.92,6,diff. thres 
        #dacList[(29,5,0)]=127#thres2 4,1.00,671,diff. thres BQD TDC?
        dacList[(29,6,0)]=300#thres2 4,0.16,2,ok 
        dacList[(29,9,0)]=298#thres2 4,0.94,8,diff. thres 




         
    elif board==31:
        #dacList[(31,0,4)]=312#3,0.87,ok 
        dacList[(31,10,4)]=314#3,0.97,ok 
        dacList[(31,11,4)]=308#3,0.99,ok 
        dacList[(31,12,4)]=304#3,1.00,ok 
        dacList[(31,13,4)]=296#3,1.00,ok 
        #dacList[(31,14,4)]=999#3,0.00,ok 
        dacList[(31,15,4)]=284#3,0.99,ok 
        #dacList[(31,16,4)]=598#3,0.99,ok 
        dacList[(31,17,4)]=356#3,0.97,ok 
        dacList[(31,18,4)]=296#3,1.00,ok 
        dacList[(31,19,4)]=308#3,0.97,ok 
        #dacList[(31,1,4)]=598#3,0.98,ok 
        #dacList[(31,20,4)]=320#3,0.99,ok 
        #dacList[(31,21,4)]=414#3,0.70,PRB!!!!!!!!! 
        #dacList[(31,22,4)]=346#3,1.00,ok 
        #dacList[(31,23,4)]=598#3,0.98,ok 
        dacList[(31,24,4)]=296#3,0.99,ok 
        dacList[(31,2,4)]=284#3,0.98,ok 
        dacList[(31,3,4)]=282#3,0.98,ok 
        dacList[(31,4,4)]=290#3,0.99,ok 
        dacList[(31,5,4)]=312#3,0.97,ok 
        dacList[(31,6,4)]=286#3,1.00,ok 
        dacList[(31,7,4)]=292#3,0.99,ok 
        dacList[(31,8,4)]=312#3,0.99,ok 
        dacList[(31,9,4)]=268#3,1.00,ok

        


        # dacList[(31,10,7)]=308#3,0.93,ok 
        # dacList[(31,11,7)]=302#3,0.94,ok 
        # dacList[(31,12,7)]=298#3,0.93,ok 
        # dacList[(31,13,7)]=292#3,0.83,ok 
        # dacList[(31,15,7)]=280#3,0.84,ok 
        # dacList[(31,17,7)]=348#3,0.97,ok 
        # dacList[(31,18,7)]=290#3,0.89,ok 
        # dacList[(31,19,7)]=300#3,0.94,ok 
        # dacList[(31,24,7)]=292#3,0.99,ok 
        # dacList[(31,2,7)]=278#3,0.88,ok 
        # dacList[(31,3,7)]=276#3,0.99,ok 
        # dacList[(31,4,7)]=278#3,1.00,ok 
        # dacList[(31,5,7)]=306#3,0.93,ok 
        # dacList[(31,6,7)]=282#3,0.93,ok 
        # dacList[(31,7,7)]=286#3,0.96,ok 
        # dacList[(31,8,7)]=306#3,0.98,ok 
        # dacList[(31,9,7)]=258#3,0.96,ok 



        dacList[(31,10,7)]=314#4,0.99,ok 
        dacList[(31,11,7)]=308#4,0.98,ok 
        dacList[(31,12,7)]=304#4,1.00,ok 
        dacList[(31,13,7)]=296#4,0.99,ok 
        dacList[(31,15,7)]=286#4,0.91,ok 
        dacList[(31,17,7)]=356#4,0.94,ok 
        dacList[(31,18,7)]=296#4,1.00,ok 
        dacList[(31,19,7)]=306#4,1.00,ok 
        dacList[(31,24,7)]=300#4,1.00,ok 
        dacList[(31,2,7)]=284#4,0.98,ok 
        dacList[(31,3,7)]=284#4,0.94,ok 
        dacList[(31,4,7)]=286#4,0.98,ok 
        dacList[(31,5,7)]=312#4,0.96,ok 
        dacList[(31,6,7)]=288#4,0.96,ok 
        dacList[(31,7,7)]=292#4,1.00,ok 
        dacList[(31,8,7)]=314#4,0.94,ok 
        dacList[(31,9,7)]=264#4,0.99,ok 


        # dacList[(31,10,6)]=310#3,0.90,ok 
        # dacList[(31,11,6)]=304#3,0.84,ok 
        # dacList[(31,12,6)]=300#3,0.94,ok 
        # dacList[(31,13,6)]=292#3,0.99,ok 
        # dacList[(31,15,6)]=280#3,1.00,ok 
        # dacList[(31,17,6)]=350#3,0.92,ok 
        # dacList[(31,18,6)]=292#3,0.93,ok 
        # dacList[(31,19,6)]=300#3,0.98,ok 
        # dacList[(31,24,6)]=292#3,1.00,ok 
        # dacList[(31,2,6)]=278#3,0.99,ok 
        # dacList[(31,3,6)]=278#3,0.96,ok 
        # dacList[(31,4,6)]=282#3,0.99,ok 
        # dacList[(31,5,6)]=306#3,0.98,ok 
        # dacList[(31,6,6)]=282#3,1.00,ok 
        # dacList[(31,7,6)]=286#3,0.99,ok 
        # dacList[(31,8,6)]=308#3,0.98,ok 
        # dacList[(31,9,6)]=260#3,0.99,ok 

        dacList[(31,10,6)]=320#4,0.89,ok 
        dacList[(31,11,6)]=310#4,0.99,ok 
        dacList[(31,12,6)]=308#4,0.95,ok 
        dacList[(31,13,6)]=300#4,0.95,ok 
        dacList[(31,15,6)]=286#4,1.00,ok 
        dacList[(31,17,6)]=358#4,0.93,ok 
        dacList[(31,18,6)]=298#4,0.98,ok 
        dacList[(31,19,6)]=310#4,0.95,ok 
        dacList[(31,24,6)]=302#4,0.98,ok 
        dacList[(31,2,6)]=286#4,0.98,ok 
        dacList[(31,3,6)]=284#4,0.99,ok 
        dacList[(31,4,6)]=288#4,0.99,ok 
        dacList[(31,5,6)]=314#4,0.92,ok 
        dacList[(31,6,6)]=290#4,0.99,ok 
        dacList[(31,7,6)]=296#4,0.95,ok 
        dacList[(31,8,6)]=316#4,1.00,ok 
        dacList[(31,9,6)]=268#4,0.99,ok 
        pass
    
    elif board==44:

        # #dacList[(44,0,0)]=127#thres2 18,0.48,471,diff. thres 
        # dacList[(44,10,0)]=396#thres2 18,0.92,12,diff. thres 
        # #dacList[(44,11,0)]=127#thres2 18,0.96,311,diff. thres
        # dacList[(44,11,0)]=440#thres2 20,0.88,8,diff. thres 
        # dacList[(44,12,0)]=440#thres2 18,0.96,56,diff. thres 
        # dacList[(44,13,0)]=506#thres2 18,0.04,0,ok 
        # dacList[(44,14,0)]=390#thres2 18,0.70,4,ok 
        # dacList[(44,15,0)]=462#thres2 18,0.90,22,diff. thres 
        # dacList[(44,16,0)]=380#thres2 18,0.86,20,diff. thres 
        # dacList[(44,17,0)]=434#thres2 18,0.88,28,diff. thres 
        # dacList[(44,18,0)]=488#thres2 18,0.02,0,ok 
        # dacList[(44,19,0)]=342#thres2 18,0.84,24,diff. thres 
        # dacList[(44,1,0)]=382#thres2 18,0.94,22,diff. thres 
        # #dacList[(44,20,0)]=598#thres2 18,0.02,0,ok 
        # dacList[(44,21,0)]=422#thres2 18,0.86,2,ok 
        # #dacList[(44,22,0)]=127#thres2 18,0.94,247,diff. thres
        # dacList[(44,22,0)]=346#thres2 20,0.96,36,diff. thres
        # dacList[(44,23,0)]=404#thres2 18,0.98,12,diff. thres 
        # dacList[(44,24,0)]=338#thres2 18,0.66,8,diff. thres 
        # #dacList[(44,2,0)]=127#thres2 18,0.96,265,diff. thres 
        # dacList[(44,3,0)]=382#thres2 18,0.92,8,diff. thres 
        # #dacList[(44,4,0)]=127#thres2 18,0.98,471,diff. thres 
        # #dacList[(44,5,0)]=127#thres2 18,0.50,293,diff. thres 
        # dacList[(44,6,0)]=430#thres2 18,0.90,12,diff. thres 
        # #dacList[(44,7,0)]=598#thres2 18,0.02,0,ok 
        # dacList[(44,8,0)]=476#thres2 18,0.90,2,ok 
        # dacList[(44,9,0)]=416#thres2 18,0.96,2,ok 
       
        #dacList[(44,0,0)]=500 very noisy
        dacList[(44,10,0)]=380
        dacList[(44,11,0)]=380
        dacList[(44,12,0)]=440
        dacList[(44,13,0)]=410
        dacList[(44,14,0)]=350
        dacList[(44,15,0)]=440
        dacList[(44,16,0)]=380
        dacList[(44,17,0)]=410
        dacList[(44,18,0)]=450
        dacList[(44,19,0)]=340
        dacList[(44,1,0)]=360
        dacList[(44,2,0)]=340
        dacList[(44,21,0)]=400
        dacList[(44,22,0)]=350
        dacList[(44,23,0)]=380
        dacList[(44,24,0)]=340
        dacList[(44,3,0)]=360
        dacList[(44,4,0)]=340
        dacList[(44,6,0)]=390
        dacList[(44,8,0)]=420
        dacList[(44,9,0)]=380

    elif board==45:



        #channels not connected (really?)
        dacList[(45,0,0)]=346#4,0.94,ok 
        #dacList[(45,1,0)]=384#4,0.97,ok
        dacList[(45,2,0)]=348#4,1.00,ok
        dacList[(45,6,0)]=406#4,0.96,ok 
        dacList[(45,8,0)]=380#4,0.98,ok
        dacList[(45,12,0)]=390#4,0.82,ok
        dacList[(45,16,0)]=376#4,1.00,ok 
        dacList[(45,17,0)]=354#4,0.84,ok
        dacList[(45,14,0)]=388#thres2 4,0.04,0,ok 
        dacList[(45,1,0)]=328#thres2 4,0.04,0,ok 
        dacList[(45,4,0)]=344#thres2 4,0.14,2,ok 

 

        dacList[(45,11,0)]=312#4,0.83,6,diff. thres 
        #dacList[(45,14,0)]=314#4,0.14,2,ok 
        dacList[(45,15,0)]=256#4,0.74,4,large saturated frac. 
        dacList[(45,19,0)]=268#4,0.34,2,ok 
        dacList[(45,20,0)]=294#4,0.00,0,ok 
        dacList[(45,21,0)]=302#4,0.04,0,ok 
        dacList[(45,22,0)]=276#4,0.18,2,ok 
        dacList[(45,23,0)]=288#4,0.10,2,ok 
        dacList[(45,24,0)]=290#4,0.08,2,ok 
        #dacList[(45,4,0)]=242#4,0.88,6,diff. thres 
        dacList[(45,5,0)]=290#4,0.52,4,large saturated frac. 


        

        pass
    return dacList                       
