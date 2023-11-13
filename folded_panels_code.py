# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:31:59 2023

@author: admin
"""

# import numpy as np
# import csv
import math
import reader

lcell, wcell, powcell = reader.read_cell_inp()

print("lcell: ", lcell)
print("wcell: ", wcell)
print("powcell: ", powcell)

rho, tf, clf, clmside, clhi, clho, clmcen, clcell = reader.read_frame_inp()

print("rho: ", rho)
print("tf: ", tf)
print("clf: ", clf)
print("clmside: ", clmside)
print("clhi: ", clhi)
print("clho: ", clho)
print("clmcen: ", clmcen)
print("clcell: ", clcell)

L, W, H = reader.read_body_inp()

print("L: ", L)
print("W: ", W)
print("H: ", H)

# equations for folded calculations

dhinge = round(2*(tf-clhi),2)
lframe = round(wcell + 2*(clf +clhi +dhinge +clho),2)
h2hdist = round(lframe - 2*clho - dhinge,2)
wframe = round(lcell + 2*clf,2)
nstack = math.floor((W-clmcen-dhinge)/(2*tf))
numassembs = math.floor(L/(wframe +clmside))

print("dhinge: ", dhinge)
print("lframe: ", lframe)
print("h2hdist: ", h2hdist)
print("wframe: ", wframe)
print("nstack: ", nstack)
print("numassembs: ", numassembs)

# Writing in the intermediate file

Odat = open("intermediate vals.txt", "w")
Odat.write(str(dhinge))
Odat.write("\t: (dhinge) \t Diameter of the hinge in mm\n")
Odat.write(str(h2hdist))
Odat.write("\t: (h2hdist) \t Hinge to hinge distance in mm\n")
Odat.write(str(lframe))
Odat.write("\t: (lframe) \t Length of frame in mm\n")
Odat.write(str(wframe))
Odat.write("\t: (wframe) \t Width of frame in mm\n")
Odat.write(str(nstack))
Odat.write("\t: (nstack) \t Number of panels per stack\n")
Odat.write(str(numassembs))
Odat.write("\t: (numassmbs) \t Number of stacks / assemblies\n")
Odat.close()

# calculating output values

ncells = 2*nstack*numassembs
lenopen = round(clmcen+dhinge+2*nstack*h2hdist,2)
widopen = round(numassembs*(wframe+clmside),2)
ptot = round(powcell*ncells,2)
vtot = round(lframe*widopen*(2*nstack*tf + clmcen),2)
mtot = round(lenopen*widopen*tf*rho,2)

print("ncells: ", ncells)
print("ptot (W): ", ptot)
print("vtot (mm^3): ", vtot)
print("mtot (mg): ", mtot)
print("lenopen (mm): ", lenopen)
print("widopen (mm): ", widopen)

# convert values to cgs to make them 3-4 digits
vtot = round(vtot/1000.0,2)  # in cc
mtot = round(mtot/10**6,2)  # in kg

# give lengths in m for MOI calculation later

lenopen = round(lenopen/1000.0,2)  # in m
widopen = round(widopen/1000.0,2)  # in m

# writing output values

Odat = open("output vals.txt", "w")
Odat.write(str(ncells))
Odat.write("\t\t: (ncells) \t Total number of cells\n")
Odat.write(str(ptot))
Odat.write("\t\t: (ptot) \t Total available power in W\n")
Odat.write(str(vtot))
Odat.write("\t\t: (vtot) \t Volume occupied by full assembly in cm^3\n")
Odat.write(str(mtot))
Odat.write("\t\t: (mtot) \t Total mass of panels in kg\n")
Odat.write(str(lenopen))
Odat.write("\t\t: (lenopen) \t Length of deployed assembly in m\n")
Odat.write(str(widopen))
Odat.write("\t\t: (widopen) \t Width of deployed assembly in m\n")
Odat.close()



