
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt
import argparse

def euler(function,t0,tf,ts,f0,T,gamma):
    n = int((tf-t0)/ts)+1
    t = np.linspace(t0,tf,n)
    holding = np.zeros((2, n))

    holding[:, 0] = f0
    fi = np.zeros((2))

    for i in range(len(t) - 1):
        fi = holding[:, i]
        ti = t[i]
        holding[:, i + 1] = ts*np.array(function(ti,fi,T,ts,gamma)) + fi #increments the function
    return t, holding

def langevin(t,val,T,ts,gamma):
    
    #x = val[0]
    v = val[1]
    stdv = np.sqrt(2*gamma*T*ts)
    dxdt = v
    dvdt = -v*gamma/m + np.random.normal(0,stdv)

    return dxdt, dvdt

def plotdata(t,f):
    plt.plot(t,f[0])
    plt.savefig("trajectory.png")

def fileprint(t,f):
    ind = np.arange(len(t))
    full = np.vstack((ind,t,f))
    full = np.transpose(full)
    np.savetxt('output.txt',full, header="Index,Time,Position,Velocity", delimiter = ',', fmt = '%1d,%f,%f,%f')

def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--temperature", help="Temperature of the system", type=float)
    parser.add_argument("--total_time", help="Temperature of the system", type=float)
    parser.add_argument("--time_step", help="Temperature of the system", type=float)
    parser.add_argument("--initial_position", help="Temperature of the system", type=float)
    parser.add_argument("--initial_velocity", help="Temperature of the system", type=float)
    parser.add_argument("--damping_coefficient", help="Temperature of the system", type=float)
    args = parser.parse_args()
    T = args.temperature
    tf = args.total_time
    ts = args.time_step
    x0 = args.initial_position
    v0 = args.initial_velocity
    gamma = args.damping_coefficient
    return T,tf,ts,x0,v0,gamma

T,tf,ts,x0,v0,gamma = getargs()
print(T,tf,ts,x0,v0,gamma)
t,f = euler(langevin,0,tf,ts,[x0,v0])
fileprint(t,f)
plotdata(t,f)
