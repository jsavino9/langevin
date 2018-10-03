================
Langevin Project
================


.. image:: https://img.shields.io/pypi/v/langevin_project.svg
        :target: https://pypi.python.org/pypi/langevin_project

.. image:: https://img.shields.io/travis/jsavino9/langevin_project.svg
        :target: https://travis-ci.org/jsavino9/langevin_project

.. image:: https://readthedocs.org/projects/langevin-project/badge/?version=latest
        :target: https://langevin-project.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/jsavino9/langevin_project/shield.svg
     :target: https://pyup.io/repos/github/jsavino9/langevin_project/
     :alt: Updates

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

It is also possible to run the program by using the bash script provided.  Use sh run.sh.  Arguments can be edited via a text editor.

Available Arguments
------------------------

--Temperature: The temperature of the system, unitless.  *Type:* Float; *Default:* 300

--total_time: The total time that the simulation runs.  *Type:* Float; *Default:* 1000

--time_step: The time step to increment the integrator at.  *Type:* Float *Default:* 0.1

--initial_position: The starting position for the particle. *Type:* Float *Default:* 0.0

--initial_velocity: The starting velocity for the particle.  *Type:* Float *Default:* 0.0

--damping_coefficient: The coefficient for the drag force.  *Type:* Float *Default:* 0.1


Outputs
---------------------------

Credits
-------
Author: James Savino

Projected completed for CHE 477 at University of Rochester under Professor Andrew White.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
