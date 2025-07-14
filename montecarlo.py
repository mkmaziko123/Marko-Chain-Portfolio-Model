import pandas as pd
from markovportfolio import marketstates

montetrailnum = 10000

pathreturns = { "pathvalue": [] }

def montecarlo(marketstates):
    for i in range(0,montetrialnum):
        marketstates(value,currentstate,numtrials)
        
def plot(pathreturns):
    pd.DataFrame(pathreturns)
    df.plot(title = "Markov-MonteCarlo-Simulation of Portfolio")
    plt.xlabel("Time")
    plt.ylabel("Model Value")
    plt.show()

        