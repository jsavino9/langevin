================
Langevin Project
================

This application applies the langevin dynamics model to a single particle in one dimension and bounded by a wall on both sides. It utilizes the Euler method to numerically solve for the velocity and position, and reports the data in a graph of position vs. time and in a text file that includes the index, time, position, and velocity.  Additionally, the program completes 100 runs and plots a histogram detailing the number of runs that required a range of times to hit a wall.

.. image:: https://coveralls.io/repos/github/jsavino9/langevin/badge.svg?branch=master
	:target: https://coveralls.io/github/jsavino9/langevin?branch=master

* Free software: MIT license

===============================
Installation Instructions
===============================


This program is intended to be run on Python 3.

Required packages: argparse, matplotlib, numpy

*packages can be installed using "!pip install [package]"*

After downloading the required packages, go to the repository home page https://github.com/jsavino9/langevin. Click clone/download, and click "download as zip".  An alternative option is to clone the repository.

==========================
Running the program
==========================


Navigate to the source directory at ../langevin_project/langevin_project/

Run the program by typing python langevin_project.py --arguments

It is also possible to run the program by using the bash script provided.  Use sh run.sh.  Arguments in run.sh can be edited via a text editor.


Available Arguments
------------------------

--Temperature: The temperature of the system, unitless.  *Type:* Float; *Default:* 300

--total_time: The total time that the simulation runs.  *Type:* Float; *Default:* 1000

--time_step: The time step to increment the integrator at.  *Type:* Float *Default:* 0.1

--initial_position: The starting position for the particle. *Type:* Float *Default:* 0.0

--initial_velocity: The starting velocity for the particle.  *Type:* Float *Default:* 0.0

--damping_coefficient: The coefficient for the drag force.  *Type:* Float *Default:* 0.1

note: The starting position defaults to 0.0, but this is not recommended because half of the trajectories will have no useful data, and the histogram will be skewed, since 50% of the runs hit the wall on the second time step.  Wall size can be adjusted in the code.

note 2: All inputs are in reduced units.


Outputs
---------------------------

trajectory.png: This is a single trajectory of when the particle hit a wall.  It graphs position vs. time.

histogram.png: This is a histogram that details how many runs required a specific amount of time to hit the wall.

output.txt: This output file contains the index, time, position, and velocity for a run where the particle hit the wall.

results: The function will print the final position, velocity, and time for a run where the particle hit the wall.


Credits
-------
Author: James Savino

Projected completed for CHE 477 at University of Rochester under Professor Andrew White.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
