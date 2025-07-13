import random 
import matplotlib.pyplot as plt
import pandas as pd
montetrialnum = 10,000

currentstate = random.randint(0,2)
numtrials = random.randint(1,100)

historicreturns = { "portvalue": [] ,
    "deltaportvalue": [] }

def marketstates(value,currentstate,numtrials):
    states = [[0.7,0.2,0.1], 
    [0.3,0.6,0.1] , 
    [0.4,0.3,0.3] ]
    bull = 0
    bear = 1
    crash = 2
    statereturns = {0: 1.08 ,1: 0.8 ,2: 0.2}
    for i in range(0,numtrials):
        transitionprobs = states[currentstate]
        nextstate = random.choices([0,1,2], weights = transitionprobs)[0]
        returnfactor = statereturns[nextstate]
        newvalue = value * returnfactor
        deltavalue = ((newvalue - value) / value) * 100
        historicreturns["portvalue"].append(newvalue)
        historicreturns["deltaportvalue"].append(deltavalue)
        currentstate = nextstate
        value = newvalue

def montetrialnum(marketstates):
    for i in range(0,montetrialnum):
        marketstates(value,currentstate,numtrials)
        

def display():
    df = pd.DataFrame(historicreturns)
    df.plot(title = "Portfolio Simulation Via Markov Chain")
    plt.xlabel("Time Step")
    plt.ylabel("Value/ΔValue")
    plt.show()






