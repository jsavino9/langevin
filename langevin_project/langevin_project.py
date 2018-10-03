
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt
import argparse

def euler(function,t0,tf,ts,f0,T,gamma,wallsize=5):
    n = int((tf-t0)/ts)+1 #gets number of time entries
    t = np.linspace(t0,tf,n) #defines the time array using initial time, final time, and time step
    holding = np.zeros((2, n)) #creates the array to hold the variables in
    holding[:, 0] = f0 #initializes the holding array
    hitwall = 0
    fi = np.zeros((2)) #initializes array to hold x and v in so they can be put into evaluated function
    for i in range(len(t) - 1): #loop to iterate euler method over all times
        if holding[0][i] >= wallsize or holding[0][i] <= -wallsize: #checks to see if particle hits a wall
            holding = holding[:, :i] #fills holding array up to current time if the wall is hit
            t = t[:i] #fills time array up to current time if wall is hit
            hitwall = 1
            break
        fi = holding[:, i] #defines fi according to current value of holding
        ti = t[i] #defines time as current time
        holding[:, i + 1] = ts*np.array(function(ti,fi,T,ts,gamma)) + fi #increments the function
    return t, holding, hitwall #return time and the holding array

def langevin(t,val,T,ts,gamma):
    m = 1    #defines m = 1
    v = val[1] #defines velocity as the second element of array val
    stdv = np.sqrt(2*gamma*T*ts) #find the standard deviation of the random force
    dxdt = v #defines velocity as a derivative of position
    dvdt = -v*gamma/m + np.random.normal(0,stdv) #defines acceleration as a function of drag and random force

    return dxdt, dvdt

def plotdata(t,f):
    plt.plot(t,f[0]) #plots the position
    plt.plot(t,f[1]) #plots the velocity
    plt.savefig("trajectory.png") #saves figure to trajectory.png
    plt.clf() #clears the figure from matplotlib's cache

def plothistogram(T,tf,ts,x0,v0,gamma,wallsize=5):
    runs = 100 #defines the number of runs for the histogram
    times = [] #creates array to hold times
    for i in range(runs): #loop to run euler function "runs" number of times
        t,f,hitwall = euler(langevin,0,tf,ts,[x0,v0],T,gamma) #run the euler function on the langevin function
        if hitwall == 1: #if it hits wall, then add the times
            times.append(t[-1])
    plt.hist(times) #plot the histogram
    plt.savefig("histogram.png") #save the figure to histogram.png
    plt.clf()


def fileprint(t,f):
    ind = np.arange(len(t)) #make array for the indexes
    full = np.vstack((ind,t,f)) #stack index, time, and function arrays on vertically (as rows)
    full = np.transpose(full) #transpose the stacked array into column form
    #saves to output.txt in comma delimited format.  Adds headers and formats numbers so they're not excessively long
    np.savetxt('output.txt',full, header="Index,Time,Position,Velocity", delimiter = ',', fmt = '%1d,%f,%f,%f')

def getargs():
    parser = argparse.ArgumentParser() #define parser
    #get command line arguments.  includes default values and help text
    parser.add_argument("--temperature", help="Temperature of the system", default=300, type=float)
    parser.add_argument("--total_time", help="Temperature of the system", default=10, type=float)
    parser.add_argument("--time_step", help="Temperature of the system", default=0.1, type=float)
    parser.add_argument("--initial_position", help="Temperature of the system", default=0, type=float)
    parser.add_argument("--initial_velocity", help="Temperature of the system", default=0, type=float)
    parser.add_argument("--damping_coefficient", help="Temperature of the system", default=0.1, type=float)
    args = parser.parse_args() #put command line arguments into args variable
    T = args.temperature #define temperature
    tf = args.total_time #define total time
    ts = args.time_step #define time step
    x0 = args.initial_position #define initial position
    v0 = args.initial_velocity #define initial velocity
    gamma = args.damping_coefficient #define damping coefficient
    return T,tf,ts,x0,v0,gamma #return variables

def main():
    T,tf,ts,x0,v0,gamma = getargs() #get command line arguments for variables
    t,f,hitwall = euler(langevin,0,tf,ts,[x0,v0],T,gamma) #get time, position, and velocity from euler function
    fileprint(t,f) #print data to text file
    plotdata(t,f) #plot and save trajectory
    plothistogram(T,tf,ts,x0,v0,gamma) #plot and save histogram

if __name__ == '__main__':
	main() #run main
