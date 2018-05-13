'''
！python
这是求函数f(u) = u sin(1/(0.01 + u^2)) + u^3 sin (1/(0.001+u^4)) 的模拟退火算法
未经允许不得转载，使用
作者 孔繁超
'''


import math 
import random
# this is the intial tempreture
T = 10000
# each time the tempreture decrease T * 0.99
decreaseRate = 0.99 
# when the tempreture lower than the lowest tempreture it will stop
lowestT = 0.1

def getRandomValue(value):
    highest = value + 0.5
    lowest = value - 0.5
    if highest > 1:
        highest = 1
        lowest = 0.5
       
    if lowest < -1:
        highest = -0.5
        lowest = -1
        
    result = random.uniform(lowest, highest)
    return result

#this is 2a f(u) function 
def qu2a(u):
    result = u * (math.sin(1/(0.01 + u**2))) + (u**3) * math.sin(1/(0.001 + u**4))
    return result 

#this method use for get the value of dE
def getdE2a(newState, currentState):
    result = qu2a(newState) - qu2a(currentState)
    return result

#this function use for move point u, quite like hill climbing
def howToMove2a(state):
    while True:
        if (qu2a(state) < qu2a(state + 0.00001)):
            state += 0.00001
        elif (qu2a(state) < qu2a(state - 0.00001)):
            state -= 0.00001
        else:
            break
    if state > 1:
        state =1
    elif state < -1:
        state =-1
    return state
        
#this the mian function of 2a
def SAStart2a(valueU):
    currentState = valueU
    currentFunctionValue = qu2a(currentState)
    t = T
    print("----------------------------------------------Initial---------------------------------------------------")
    print("the tempreture: %f \t the value of u: %f \t the value of function f(u): %f" % (t,currentState,qu2a(currentState)))
    print("--------------------------------------------------------------------------------------------------------")
    while t > lowestT:        
        newState = getRandomValue(currentState)
        dE = getdE2a(newState, currentState)
        if (dE) >= 0:
            currentState = newState
            currentState = howToMove2a(currentState)
        else:
            e = math.exp(dE/t)
            if e >= random.uniform(0,1):
                currentState = newState
                currentState = howToMove2a(currentState)
            t *= decreaseRate
        print("the tempreture: %f \t the value of u: %f \t the value of function f(u): %f" % (t,currentState,qu2a(currentState)))
    print("when u = %f , the function u has max value = %f" % (currentState, qu2a(currentState)))
