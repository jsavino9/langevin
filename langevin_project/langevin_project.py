
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt
import argparse

def euler(function,t0,tf,ts,f0,T,gamma,wallsize=5):
    n = int((tf-t0)/ts)+1
    t = np.linspace(t0,tf,n)
    holding = np.zeros((2, n))
    holding[:, 0] = f0
    fi = np.zeros((2))
    tr = []
    for i in range(len(t) - 1):
        if holding[0][i] >= wallsize or holding[0][i] <= -wallsize:
            holding = holding[:, :i+1]
            t = t[:i+1]
            break
        fi = holding[:, i]
        ti = t[i]
        holding[:, i + 1] = ts*np.array(function(ti,fi,T,ts,gamma)) + fi #increments the function
        tr.append(ti)
    return t, holding

def langevin(t,val,T,ts,gamma):
    m = 1    
    #x = val[0]
    v = val[1]
    stdv = np.sqrt(2*gamma*T*ts)
    dxdt = v
    dvdt = -v*gamma/m + np.random.normal(0,stdv)

    return dxdt, dvdt

def plotdata(t,f):
    plt.plot(t,f[0])
    plt.plot(t,f[1])
    plt.savefig("trajectory.png")
    plt.clf()

def plothistogram(T,tf,ts,x0,v0,gamma,wallsize=5):
    runs = 100
    times = []
    for i in range(runs):
        t,f = euler(langevin,0,tf,ts,[x0,v0],T,gamma)
        if f[0][-1] >= wallsize or f[0][-1] <= -wallsize:
            times.append(t[-1])
    plt.hist(times)
    plt.savefig("histogram.png")


def fileprint(t,f):
    ind = np.arange(len(t))
    full = np.vstack((ind,t,f))
    full = np.transpose(full)
    np.savetxt('output.txt',full, header="Index,Time,Position,Velocity", delimiter = ',', fmt = '%1d,%f,%f,%f')

def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--temperature", help="Temperature of the system", default=300, type=float)
    parser.add_argument("--total_time", help="Temperature of the system", default=10, type=float)
    parser.add_argument("--time_step", help="Temperature of the system", default=0.1, type=float)
    parser.add_argument("--initial_position", help="Temperature of the system", default=0, type=float)
    parser.add_argument("--initial_velocity", help="Temperature of the system", default=0, type=float)
    parser.add_argument("--damping_coefficient", help="Temperature of the system", default=0.1, type=float)
    args = parser.parse_args()
    T = args.temperature
    tf = args.total_time
    ts = args.time_step
    x0 = args.initial_position
    v0 = args.initial_velocity
    gamma = args.damping_coefficient
    return T,tf,ts,x0,v0,gamma

def main():
    T,tf,ts,x0,v0,gamma = getargs()
    t,f = euler(langevin,0,tf,ts,[x0,v0],T,gamma)
    fileprint(t,f)
    plotdata(t,f)
    plothistogram(T,tf,ts,x0,v0,gamma)

if __name__ == '__main__':
	main()
