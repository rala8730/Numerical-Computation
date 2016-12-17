# CSCI-3656

## Coding Assignment (HW7)

It is common to use a howitzer or recoilless rifle for avalanche control at ski resorts and above highways.
The top of a 40-degree avalanche-prone slope is 3 km horizontal and 1 km vertical above your rifle.
The muzzle velocity is 300 m/s and the 10cm diameter projectile has a mass of 8 kg with a drag coefficient of 0.2.
You would like to find the firing angle (above horizontal) at which to aim so that your charge lands within 30 m of the top of the slope.
The problem setup and equations are [explained in the notebook](https://nbviewer.jupyter.org/github/jedbrown/numerical-computation/blob/master/DifferentialEquations.ipynb#Ballistics-(for-HW7)).

Write a program `hw7/hw7` that solves the differential equation for the free projectile and determines where it hits the slope.  Use the program to determine the angle theta in order to hit the slope within 30 meters of the top (without going over).  (You can either hand-optimize the angle or use a rootfinder.)
When run, your program should print the firing angle (theta) and the time of impact.

