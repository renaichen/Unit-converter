#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:17:22 2017

This python script is used to covert between different energy units, 
especially one encounters in physical chemistry, like electron volts, centimeter inverse etc.
This doesn't mean to be in high precision, some website do the same: http://halas.rice.edu/conversions
but it doesn't have temperature conversion.

@author: Renai Chen 
"""
kB = 8.617e-5 # the Boltzmann constant in unit of eV/K
h = 4.1357e-15 # the Planck constant in unit of eV*s
hbar =  6.5821e-16 # the reduced planck constant, h/2pi in unit of eV*s

# 1 eV = 1.6e-19 J
# 1 kJ/mol = 1000 J/mol, which means 1000 J energy for 1 mol amount of particles.
# So for each particle, this number should be divided by NA (Avogadro constant) 6.02e+23
# Therefore, 1 KJ/mol transfer to energy of one particle in eV, will be 
# (1000/6.02e+23/1.6e-19) = 0.0103 eV, and 1 eV = 96.487 kJ/mol
# 1 kcal = 4184 J = 4.184 kJ, therefore 1 kcal/mol = 0.04336 eV for one particle, and 1 eV = 23.06 kcal/mol

# For the unit cm^-1, it is usually referring to spectroscopy, E = h\nu = hc/lambda
# Therefore, 1/lambda = hc/E, so 1 cm^-1 = 100 m^-1, equal to 4.1357e-15*3e8*100 = 1.24e-4 eV
# For the unit ps, it refers to spectroscopy too, E = h\nu = hbar\omega = h/T
# Therefore, 1/ps = 1e12 s^-1, equal to 4.1357e-15*1e12 = 4.135e-3 eV
# Similarly, 1/fs = 1e15 s^-1, equal to 4.1347e-15*1e15 = 4.135 eV


print "Which (energy) unit do you have?"
unitIn = raw_input("Input(upper and lower cases distinguished and no commas...): eV, cm^-1, kJ/mol, T(in Kelvin), fs^-1, ps^-1  (end with ENTER) :")
amountIn = float(raw_input("What is the amount?:"))
#print "Your unit is", unitIn
unitOut = raw_input("which unit you want as output?(thermal unit is kT):")

if unitIn == "eV":
    if unitOut == "kJ/mol":
        amountOut = amountIn * 96.487
        print amountIn, "eV = ", amountOut, "kJ/mol"
    elif unitOut == "cm^-1":
        amountOut = amountIn / 1.24e-4
        print amountIn, "eV is equivalent to ", amountOut, "cm^-1"
    elif unitOut == "ps^-1":
        amountOut = amountIn / 4.135e-3
        print amountIn, "eV is equivalent to ", amountOut, "ps^-1"
    elif unitOut == "ps":
        amountOut = 1 / (amountIn / 4.135e-3)
        print amountIn, "eV is equivalent to ", amountOut, "ps"
    elif unitOut == "fs^-1":
        amountOut = amountIn / 4.135
        print amountIn, "eV is equivalent to ", amountOut, "fs^-1"
    elif unitOut == "fs":
        amountOut = 1 / (amountIn / 4.135)
        print amountIn, "eV is equivalent to ", amountOut, "fs"
    elif unitOut == "kT":
        temperature = float(raw_input("What is the temperature?(in unit of Kelvin)"))
        amountOut = amountIn / (kB * temperature)
        print amountIn, "eV = ", amountOut, "kT"
    elif unitOut == "eV":
        print "No conversion needed"
    else:
        print "Sorry, I have no idea what unit you want output..."
        
if unitIn == "kJ/mol":
    ToeV = amountIn * 0.0103 # We want everything first convert to eV
    if unitOut == "eV":
        print amountIn, "kJ/mol = ", ToeV, "eV"
    elif unitOut == "cm^-1":
        amountOut = ToeV / 1.24e-4
        print amountIn, "kJ/mol is equivalent to ", amountOut, "cm^-1"
    elif unitOut == "ps^-1":
        amountOut = ToeV / 4.135e-3 
        print amountIn, "kJ/mol is equivalent to ", amountOut, "ps^-1"
    elif unitOut == "ps":
        amountOut = 1 / (ToeV / 4.135e-3) 
        print amountIn, "kJ/mol is equivalent to ", amountOut, "ps"
    elif unitOut == "fs^-1":
        amountOut = ToeV / 4.135
        print amountIn, "kJ/mol is equivalent to ", amountOut, "fs^-1"
    elif unitOut == "fs":
        amountOut = 1 / (ToeV / 4.135)
        print amountIn, "kJ/mol is equivalent to ", amountOut, "fs"
    elif unitOut == "kT":
        temperature = float(raw_input("What is the temperature?(in unit of Kelvin)"))
        amountOut = ToeV / (kB * temperature)
        print amountIn, "kJ/mol = ", amountOut, "kT"
    elif unitOut == "kJ/mol":
        print "No conversion needed"
    else:
        print "Sorry, I have no idea what unit you want output..." 
        
if unitIn == "cm^-1":
    ToeV = amountIn * 1.24e-4 # We want everything first convert to eV
    if unitOut == "eV":
        print amountIn, "cm^-1 = ", ToeV, "eV"
    elif unitOut == "kJ/mol":
        amountOut = ToeV * 96.487
        print amountIn, "cm^-1 is equivalent to ", amountOut, "kJ/mol"
    elif unitOut == "ps^-1":
        amountOut = ToeV / 4.135e-3
        print amountIn, "cm^-1 is equivalent to ", amountOut, "ps^-1" 
    elif unitOut == "ps":
        amountOut = 1 / (ToeV / 4.135e-3)
        print amountIn, "cm^-1 is equivalent to ", amountOut, "ps"                      
    elif unitOut == "fs^-1":
        amountOut = ToeV / 4.135
        print amountIn, "cm^-1 is equivalent to ", amountOut, "fs^-1"
    elif unitOut == "fs":
        amountOut = 1 / (ToeV / 4.135)
        print amountIn, "cm^-1 is equivalent to ", amountOut, "fs"
    elif unitOut == "kT":
        temperature = float(raw_input("What is the temperature?(in unit of Kelvin)"))
        amountOut = ToeV / (kB * temperature)
        print amountIn, "cm^-1 = ", amountOut, "kT"
    elif unitOut == "cm^-1":
        print "No conversion needed"
    else:
        print "Sorry, I have no idea what unit you want output..."   
        
        
if unitIn == "ps":
    amountIn = 1/amountIn
    unitIn = "ps^-1"
    print "you must mean", amountIn, "ps^-1"
if unitIn == "ps^-1":
    ToeV = amountIn * 4.135e-3 # We want everything first convert to eV
    if unitOut == "eV":
        print amountIn, "ps^-1 = ", ToeV, "eV"
    elif unitOut == "kJ/mol":
        amountOut = ToeV * 96.487
        print amountIn, "ps^-1 is equivalent to ", amountOut, "kJ/mol"
    elif unitOut == "cm^-1":
        amountOut = ToeV / 1.24e-4
        print amountIn, "ps^-1 is equivalent to ", amountOut, "cm^-1"
    elif unitOut == "fs^-1":
        amountOut = ToeV / 4.135
        print amountIn, "ps^-1 is equivalent to ", amountOut, "fs^-1"
    elif unitOut == "fs":
        amountOut = 1 / (ToeV / 4.135)
        print amountIn, "ps^-1 is equivalent to ", amountOut, "fs"
    elif unitOut == "kT":
        temperature = float(raw_input("What is the temperature?(in unit of Kelvin)"))
        amountOut = ToeV / (kB * temperature)
        print amountIn, "ps^-1 = ", amountOut, "kT"
    elif unitOut == "ps^-1" or unitOut == "ps":
        print "No conversion needed"
    else:
        print "Sorry, I have no idea what unit you want output..." 
        
if unitIn == "fs":
    amountIn = 1/amountIn
    unitIn = "fs^-1"
    print "you must mean", amountIn, "fs^-1"
if unitIn == "fs^-1":
    ToeV = amountIn * 4.135 # We want everything first convert to eV
    if unitOut == "eV":
        print amountIn, "fs^-1 = ", ToeV, "eV"
    elif unitOut == "kJ/mol":
        amountOut = ToeV * 96.487
        print amountIn, "fs^-1 is equivalent to ", amountOut, "kJ/mol"
    elif unitOut == "cm^-1":
        amountOut = ToeV / 1.24e-4
        print amountIn, "fs^-1 is equivalent to ", amountOut, "cm^-1"
    elif unitOut == "ps^-1":
        amountOut = ToeV / 4.135e-3
        print amountIn, "fs^-1 is equivalent to ", amountOut, "ps^-1"
    elif unitOut == "ps":
        amountOut = 1 / (ToeV / 4.135e-3)
        print amountIn, "fs^-1 is equivalent to ", amountOut, "ps"
    elif unitOut == "kT":
        temperature = float(raw_input("What is the temperature?(in unit of Kelvin)"))
        amountOut = ToeV / (kB * temperature)
        print amountIn, "fs^-1 = ", amountOut, "kT"
    elif unitOut == "fs^-1" or unitOut == "fs":
        print "No conversion needed"
    else:
        print "Sorry, I have no idea what unit you want output..."         
        
if unitIn == "T":
    ToeV = amountIn * 8.62e-5 # We want everything first convert to eV
    if unitOut == "eV":
        print amountIn, "1kBT = ", ToeV, "eV"
    elif unitOut == "cm^-1":
        amountOut = ToeV / 1.24e-4
        print amountIn, "1kBT is equivalent to ", amountOut, "cm^-1"
    elif unitOut == "ps^-1":
        amountOut = ToeV / 4.135e-3 
        print amountIn, "1kBT is equivalent to ", amountOut, "ps^-1"
    elif unitOut == "ps":
        amountOut = 1 / (ToeV / 4.135e-3) 
        print amountIn, "1kBT is equivalent to ", amountOut, "ps"
    elif unitOut == "fs^-1":
        amountOut = ToeV / 4.135
        print amountIn, "1kBT is equivalent to ", amountOut, "fs^-1"
    elif unitOut == "fs":
        amountOut = 1 / (ToeV / 4.135)
        print amountIn, "1kBT is equivalent to ", amountOut, "fs"
    elif unitOut == "kJ/mol":
        amountOut = ToeV * 96.487
        print amountIn, "1kBT is equivalent to ", amountOut, "kJ/mol"
    elif unitOut == "kT":
        print "No conversion needed"
    else:
        print "Sorry, I have no idea what unit you want output..."    
