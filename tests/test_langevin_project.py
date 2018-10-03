#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `example2` package."""

import pytest
import os
import numpy as np
from langevin_project import langevin_project
import argparse
import sys
import subprocess


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

def test_euler():
	t,f,hitwall = langevin_project.euler(langevin_project.langevin,0,10,0.1,[0,0],300,0.1,wallsize=5)
	assert len(t) == len(f[0]) #tests that the length of the time array is the same as the position array

def test_langevin():
	np.random.seed(42)
	dxdt,dvdt = langevin_project.langevin(0,[0.0,1.0],300,0.1,0.1)
	#makes sure the values are type float, as passed into the function
	assert type(dxdt) == float
	assert type(dvdt) == float
	#asserts that acceleration is not equal to the negative of velocity (due to random force)
	bool = (dvdt != -dxdt*0.1)
	assert bool


def test_plot():
	if os.path.exists('trajectory.png'):
		os.remove('trajectory.png')
	t,f,hitwall = langevin_project.euler(langevin_project.langevin,0,10,0.1,[0,0],300,0.1,wallsize=5)
	langevin_project.plotdata(t,f)
	assert os.path.exists('trajectory.png') #makes sure the file is created

def test_trials():
	if os.path.exists('trajectory.png') and os.path.exists('histogram.png') and os.path.exists('output.txt'):
		os.remove('trajectory.png')
		os.remove('histogram.png')
		os.remove('output.txt')
	langevin_project.runtrials(300,10,0.1,0,0,0.1,wallsize=5,runs=100)
        #makes sure all files are created
	assert os.path.exists('histogram.png')
	assert os.path.exists('trajectory.png')
	assert os.path.exists('output.txt')

def test_write():
	if os.path.exists('output.png'):
		os.remove('output.txt')
	t,f,hitwall = langevin_project.euler(langevin_project.langevin,0,10,0.1,[0,0],300,0.1,wallsize=5)
	langevin_project.fileprint(t,f)	
	a = np.loadtxt('output.txt', delimiter=',')
	assert os.path.exists('output.txt')
	assert a[-1][0] == len(t)-1 #makes sure the output.txt is the same length as the time array

def test_args():
	T,tf,ts,x0,v0,gamma = langevin_project.getargs()
	#checks to see if default arguments are passed correctly
	assert T == 300
	assert ts == 0.1

def test_main():
	if os.path.exists('trajectory.png') and os.path.exists('histogram.png') and os.path.exists('output.txt'):
		os.remove('trajectory.png')
		os.remove('histogram.png')
		os.remove('output.txt')
	langevin_project.main()
	#makes sure files are created
	assert os.path.exists('trajectory.png')
	assert os.path.exists('output.txt')
	assert os.path.exists('histogram.png')
