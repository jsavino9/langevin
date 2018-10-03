
# coding: utf-8


import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse

def euler(function,t0,tf,ts,f0,T,gamma,wallsize=5):
    '''Description: euler takes inputs and a function, and then performs the euler method to evaluate
       the solution to the differential equation numerically.
       
       Arguments
       function: takes function to perform euler method on.  this needs to be a function that returns velocity and position
       t0: the initial time.  float or int.  This is usually 0.
       tf: the total time of the simulation.  float or int
       ts: the time step for the simulation.  float or int
       f0: initial values for v and x.  array of floats or ints
       T: temperature of the system.  float or int.
       gamma: damping coefficient.  can be float or int.
       wallsize: the "wall".  When the particle reaches this position, the simulation ends.
       
       returns
       t: the time array (of ints or floats)
       holding: array of velocity and position (float)
       hitwall: whether or not the particle hit the wall.  boolean.
    '''
    n = int((tf-t0)/ts)+1 #gets number of time entries
    t = np.linspace(t0,tf,n) #defines the time array using initial time, final time, and time step
    holding = np.zeros((2, n)) #creates the array to hold the variables in
    holding[:, 0] = f0 #initializes the holding array
    hitwall = False
    fi = np.zeros((2)) #initializes array to hold x and v in so they can be put into evaluated function
    for i in range(len(t) - 1): #loop to iterate euler method over all times
        if (holding[0][i] >= wallsize or holding[0][i] <0) and t[i] > 0: #checks to see if particle hits a wall
       # if (holding[0][i] >= wallsize or holding[0][i] <=-wallsize): #option to use -wallsize instead of 0 as the back wall
            holding = holding[:, :i] #fills holding array up to current time if the wall is hit
            t = t[:i] #fills time array up to current time if wall is hit
            hitwall = True #set hit wall value to true if it hits the wall
            break
        fi = holding[:, i] #defines fi according to current value of holding
        ti = t[i] #defines time as current time
        holding[:, i + 1] = ts*np.array(function(ti,fi,T,ts,gamma)) + fi #increments the function
    return t, holding, hitwall #return time and the holding array

def langevin(t,val,T,ts,gamma):
    '''
       Description: takes current values of x and v, and then calculates dxdt and dvdt

       arguments
       t: the current time, float or int
       val: the values of x and v
       T: the temperature of the system.  float or int
       ts: the time step.  float or int.
       gamma: the damping coefficient.  float or int.

       returns
       dxdt: the velocity.  float or int.
       dvdt: the acceleration.  float or int
       
    '''
    m = 1    #defines m = 1
    v = val[1] #defines velocity as the second element of array val
    stdv = np.sqrt(2*gamma*T*ts) #calc the standard deviation of the random force
    dxdt = v #defines velocity as a derivative of position
    dvdt = -v*gamma/m + np.random.normal(0,stdv) #defines acceleration as a function of drag and random force

    return dxdt, dvdt

def plotdata(t,f):
    '''
    Description: Plots the trajectory of the particle.
    
    arguments
    t: the time array. array of ints or floats.
    f: the position and velocity array.

    saves figure as trajectory.png in run directory 
    '''
    plt.plot(t,f[0]) #plots the position
    plt.xlabel('time') #x label
    plt.ylabel('position') #y label
    plt.title('trajectory of particle')
    #plt.plot(t,f[1]) #plots the velocity
    plt.savefig("trajectory.png") #saves figure to trajectory.png
    plt.clf() #clears the figure from matplotlib's cache

def plothistogram(T,tf,ts,x0,v0,gamma,wallsize=5):
    '''
    Description: plots histogram detailing the the amount of time it takes a particle to hit a wall over a given
    number of runs.  also saves data from last trial that hit wall and passes it into plotdata() and fileprint()
    so that these can display data that hit a wall.

    arguments
    T: the temperature of the system.  float or int.
    tf: total time of the simulation.  float or int.
    ts: time step for the simulation.  float or int.
    x0: initial value for x.  float or int.
    v0: initial value for v.  float or int.
    gamma: dampening coefficient.  float or int.
    wallsize: the "wall"  when the particle reaches this position, the simulation ends.  default is 5.


    saves figure as histogram.png
    '''
    runs = 100 #defines the number of runs for the histogram
    times = [] #creates array to hold times
    for i in range(runs): #loop to run euler function "runs" number of times
        t,f,hitwall = euler(langevin,0,tf,ts,[x0,v0],T,gamma) #run the euler function on the langevin function
        if hitwall: #if it hits wall, then add the times
            times.append(t[-1])
            t_r = t #get time for latest successful run
            f_r = f #get position and velocity for latest successful run
    plt.hist(times, bins = 'auto') #plot the histogram
    plt.xlabel('time to hit wall') #x label
    plt.ylabel('frequency') #y label
    plt.title('histogram of run times to hit wall')
    plt.savefig("histogram.png") #save the figure to histogram.png
    plt.clf() #clears matplotlib figure so images don't overlap
    fileprint(t,f) #prints successful run to 
    plotdata(t,f) #plots data to graph

def fileprint(t,f):
    '''
    Description: Saves index, time, position, and velocity in a text file
    
    arguments
    t: array containing the times.  array of float or ints.
    f: array containing velocity and position.  array of float or ints.

    saves comma delimited text file named output.txt with headers
     #index,time, position, velocity containing the aforementioned data
    '''
    ind = np.arange(len(t)) #make array for the indexes
    full = np.vstack((ind,t,f)) #stack index, time, and function arrays on vertically (as rows)
    full = np.transpose(full) #transpose the stacked array into column form
    #saves to output.txt in comma delimited format.  Adds headers and formats numbers so they're not excessively long
    np.savetxt('output.txt',full, header="Index,Time,Position,Velocity", delimiter = ',', fmt = '%1d,%f,%f,%f')

def getargs():
    '''
    Description: This pulls command line arguments and parses them using argparser

    arguments
    the arguments passed in the command line

    returns
    T: the temperature, float or int.  default 300.
    tf: total time, float or int.  default 10.
    ts: time step, float or int.  default 0.1.
    x0: initial position, float or int.  default 0.
    v0: initial velocity, float or int.  default 0.
    gamma: damping coefficient, float or int.  default 0.1.
    '''
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
    '''
    Description: Main function that gets the command line arguments
    then saves the histogram and trajectories as png, and the output arrays as a comma delimited txt file.
    '''
    T,tf,ts,x0,v0,gamma = getargs() #get command line arguments for variables
    t,f,hitwall = euler(langevin,0,tf,ts,[x0,v0],T,gamma) #get time, position, and velocity from euler function
    plothistogram(T,tf,ts,x0,v0,gamma) #plot and save histogram

if __name__ == '__main__':
	main() #run main
