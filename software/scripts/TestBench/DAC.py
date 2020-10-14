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
        dacList[(3,1,0)]=408
        dacList[(3,2,0)]=310
        dacList[(3,3,0)]=348
        dacList[(3,4,0)]=334
        dacList[(3,5,0)]=374
        dacList[(3,6,0)]=362
        dacList[(3,7,0)]=344
        dacList[(3,8,0)]=356      
        dacList[(3,10,0)]=340
        dacList[(3,11,0)]=374
        dacList[(3,12,0)]=360
        dacList[(3,13,0)]=382
        dacList[(3,14,0)]=418        
    elif board==8:
        dacList[(8,0,4)]=412#B8,3,1.00,ok 
        dacList[(8,1,4)]=406#B8,3,0.96,ok 
        dacList[(8,2,4)]=340#B8,3,1.00,ok 
        dacList[(8,3,4)]=412#3,0.99,ok 
        dacList[(8,4,4)]=350#3,0.99,ok 
        dacList[(8,5,4)]=408#3,0.99,ok 
        dacList[(8,6,4)]=388#3,0.72,PRB!!!!!!!!! 
        dacList[(8,7,4)]=356#3,0.97,ok 
        dacList[(8,8,4)]=404#3,0.97,ok 
        dacList[(8,9,4)]=298#3,0.98,ok 
        dacList[(8,10,4)]=426#3,0.98,ok 
        dacList[(8,11,4)]=418#3,0.98,ok 
        dacList[(8,12,4)]=388#3,0.99,ok 
        dacList[(8,13,4)]=436#3,0.17,PRB!!!!!!!!! 
        dacList[(8,14,4)]=308#5,0.95,ok



        

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
        dacList[(12,0,4)]=400#3,0.97,ok 
        dacList[(12,1,4)]=380#3,0.99,ok 
        dacList[(12,2,4)]=348#3,0.97,ok 
        dacList[(12,3,4)]=402#3,0.97,ok 
        dacList[(12,4,4)]=326#3,1.00,ok 
        dacList[(12,5,4)]=426#3,0.97,ok 
        dacList[(12,6,4)]=396#3,0.98,ok 
        dacList[(12,7,4)]=400#3,0.99,ok 
        dacList[(12,8,4)]=380#3,1.00,ok 
        dacList[(12,9,4)]=346#3,0.97,ok
        dacList[(12,10,4)]=394#3,0.98,ok 
        dacList[(12,11,4)]=380#3,0.99,ok 
        #dacList[(12,12,4)]=1022#3,1.00,ok 
        dacList[(12,13,4)]=416#3,0.97,ok 
        dacList[(12,14,4)]=360#5,0.98,ok 

        pass
    elif board==13:
        dacList[(13,0,0)]=320#B13,3,0.96,ok 
        dacList[(13,1,0)]=302#B13,3,0.99,ok 
        dacList[(13,2,0)]=324#B13,3,0.96,ok 
        dacList[(13,3,0)]=312#B13,3,0.98,ok 
        dacList[(13,4,0)]=294#B13,3,0.96,ok 
        dacList[(13,5,0)]=380#B13,3,0.99,ok 
        dacList[(13,7,0)]=304#B13,3,1.00,ok 
        dacList[(13,8,0)]=334#B13,3,0.99,ok 
        dacList[(13,9,0)]=312#B13,3,0.99,ok
        dacList[(13,10,0)]=316#B13,3,0.98,ok 
        dacList[(13,11,0)]=336#B13,3,0.98,ok 
        dacList[(13,12,0)]=354#B13,3,0.99,ok 
        dacList[(13,13,0)]=342#B13,3,0.97,ok
        #dacList[(13,14,0)]=324#B13,3,0.01,PRB!!!!!!!!! 
        dacList[(13,14,0)]=338#B13,5,0.95,ok
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


        dacList[(21,10,4)]=284#3,1.00,ok 
        dacList[(21,12,4)]=294#3,1.00,ok 
        dacList[(21,13,4)]=302#3,1.00,ok 
        dacList[(21,14,4)]=302#3,0.99,ok 
        dacList[(21,15,4)]=312#3,0.99,ok 
        dacList[(21,17,4)]=346#3,0.98,ok 
        dacList[(21,18,4)]=326#3,0.99,ok 
        dacList[(21,19,4)]=314#3,0.98,ok 
        dacList[(21,1,4)]=326#3,0.99,ok 
        dacList[(21,24,4)]=310#3,0.98,ok 
        dacList[(21,2,4)]=312#3,1.00,ok 
        dacList[(21,3,4)]=322#3,1.00,ok 
        dacList[(21,4,4)]=312#3,0.98,ok 
        dacList[(21,5,4)]=298#3,0.96,ok 
        dacList[(21,7,4)]=320#3,0.99,ok 
        dacList[(21,8,4)]=314#3,0.98,ok 
        dacList[(21,9,4)]=310#3,0.99,ok

        dacList[(21,11,4)]=326#3,0.87,ok 
        #dacList[(21,16,4)]=598#3,1.00,ok 
        dacList[(21,21,4)]=500#3,0.78,PRB!!!!!!!!! 
        dacList[(21,6,4)]=308#3,0.99,ok 



#         dacList[(21,10,6)]=280#3,0.75,PRB!!!!!!!!! 
# dacList[(21,10,7)]=280#3,0.85,ok 
# dacList[(21,12,6)]=290#3,0.93,ok 
# dacList[(21,12,7)]=288#3,0.97,ok 
# dacList[(21,13,6)]=294#3,0.99,ok 
# dacList[(21,13,7)]=294#3,0.95,ok 
# dacList[(21,14,6)]=298#3,0.96,ok 
# dacList[(21,14,7)]=296#3,0.98,ok 
# dacList[(21,15,6)]=308#3,0.98,ok 
# dacList[(21,15,7)]=308#3,0.87,ok 
# dacList[(21,17,6)]=340#3,0.95,ok 
# dacList[(21,17,7)]=338#3,0.98,ok 
# dacList[(21,18,6)]=320#3,0.99,ok 
# dacList[(21,18,7)]=318#3,0.94,ok 
# dacList[(21,19,6)]=308#3,1.00,ok 
# dacList[(21,19,7)]=308#3,0.97,ok 
# dacList[(21,1,6)]=322#3,0.96,ok 
# dacList[(21,1,7)]=320#3,1.00,ok 
# dacList[(21,24,6)]=308#3,0.98,ok 
# dacList[(21,24,7)]=306#3,1.00,ok 
# dacList[(21,2,6)]=308#3,0.99,ok 
# dacList[(21,2,7)]=308#3,0.93,ok 
# dacList[(21,3,6)]=318#3,0.95,ok 
# dacList[(21,3,7)]=316#3,0.95,ok 
# dacList[(21,4,6)]=302#3,1.00,ok 
# dacList[(21,4,7)]=302#3,0.96,ok 
# dacList[(21,5,6)]=294#3,0.90,ok 
# dacList[(21,5,7)]=292#3,0.99,ok 
# dacList[(21,7,6)]=316#3,0.90,ok 
# dacList[(21,7,7)]=314#3,0.96,ok 
# dacList[(21,8,6)]=308#3,0.99,ok 
# dacList[(21,8,7)]=308#3,0.98,ok 
# dacList[(21,9,6)]=298#3,1.00,ok 
# dacList[(21,9,7)]=296#3,0.96,ok 



        dacList[(21,10,6)]=290#4,0.92,ok 
        dacList[(21,10,7)]=288#4,0.91,ok 
        dacList[(21,12,6)]=296#4,1.00,ok 
        dacList[(21,12,7)]=296#4,0.96,ok 
        dacList[(21,13,6)]=306#4,0.96,ok 
        dacList[(21,13,7)]=302#4,0.98,ok 
        dacList[(21,14,6)]=306#4,0.99,ok 
        dacList[(21,14,7)]=304#4,0.99,ok 
        dacList[(21,15,6)]=314#4,1.00,ok 
        dacList[(21,15,7)]=314#4,0.95,ok 
        dacList[(21,17,6)]=350#4,0.96,ok 
        dacList[(21,17,7)]=346#4,0.98,ok 
        dacList[(21,18,6)]=330#4,0.98,ok 
        dacList[(21,18,7)]=328#4,0.96,ok 
        dacList[(21,19,6)]=320#4,0.99,ok 
        dacList[(21,19,7)]=316#4,0.98,ok 
        dacList[(21,1,6)]=330#4,0.99,ok 
        dacList[(21,1,7)]=328#4,0.98,ok 
        dacList[(21,24,6)]=314#4,1.00,ok 
        dacList[(21,24,7)]=314#4,0.96,ok 
        dacList[(21,2,6)]=316#4,0.99,ok 
        dacList[(21,2,7)]=316#4,0.96,ok 
        dacList[(21,3,6)]=326#4,1.00,ok 
        dacList[(21,3,7)]=324#4,0.98,ok 
        dacList[(21,4,6)]=310#4,0.99,ok 
        dacList[(21,4,7)]=308#4,1.00,ok 
        dacList[(21,5,6)]=300#4,1.00,ok 
        dacList[(21,5,7)]=300#4,0.94,ok 
        dacList[(21,7,6)]=324#4,1.00,ok 
        dacList[(21,7,7)]=322#4,0.97,ok 
        dacList[(21,8,6)]=318#4,0.99,ok 
        dacList[(21,8,7)]=316#4,0.96,ok 
        dacList[(21,9,6)]=308#4,1.00,ok 
        dacList[(21,9,7)]=304#4,1.00,ok 

        


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
        dacList[(27,20,0)]=272#4,0.99,ok 
        dacList[(27,21,0)]=282#4,0.98,ok 
        dacList[(27,22,0)]=272#4,0.93,ok 
        dacList[(27,23,0)]=274#4,0.95,ok 
        dacList[(27,24,0)]=244#4,0.98,ok 
        pass


    elif board==29: #13 is not bump-bonded
        dacList[(29,0,0)]=330#4,0.91,ok 
        dacList[(29,10,0)]=268#4,0.76,PRB!!!!!!!!! 
        dacList[(29,11,0)]=302#4,0.89,ok 
        dacList[(29,12,0)]=288#4,0.54,PRB!!!!!!!!! 
        dacList[(29,15,0)]=302#4,0.69,PRB!!!!!!!!! 
        dacList[(29,16,0)]=304#4,0.60,PRB!!!!!!!!! 
        dacList[(29,17,0)]=286#4,0.59,PRB!!!!!!!!! 
        dacList[(29,18,0)]=290#4,0.91,ok 
        dacList[(29,20,0)]=322#4,0.96,ok 
        dacList[(29,21,0)]=278#4,0.95,ok 
        dacList[(29,22,0)]=312#4,0.97,ok 
        dacList[(29,24,0)]=304#4,0.98,ok 
        dacList[(29,2,0)]=320#4,0.86,ok 
        dacList[(29,3,0)]=296#4,0.93,ok 
        dacList[(29,4,0)]=288#4,0.53,PRB!!!!!!!!! 
        dacList[(29,6,0)]=306#4,0.80,PRB!!!!!!!!! 
        dacList[(29,7,0)]=278#4,0.99,ok 
        dacList[(29,8,0)]=314#4,0.88,ok 
        dacList[(29,9,0)]=300#4,0.67,PRB!!!!!!!!! 
        
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
    return dacList                       
