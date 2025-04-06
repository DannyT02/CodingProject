# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    radiation.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Danny Tay <dtay028@e.ntu.edu.sg>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/06 17:37:29 by Danny Tay         #+#    #+#              #
#    Updated: 2025/04/06 17:37:29 by Danny Tay        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
from math import e


# Part a
h = 6.626e-34 # planck's constant
c = 3.00e8 # speed of light 
kb = 1.38e-23 # Boltzmann's constant
T = 5775 # Temp of the sun as a perfect blackbody at 5775 Kelvin temp

WaveLength = [] #storing wave length
Energy = [] #storing Power

def radiation(lambdamn,T): #Planck's equation using Lambda in meters and Temperature in Kelvin
    numerator = 2 * np.pi * h * c**2 #Numerator part of Planck's equation
    denominator = lambdamn**5 * (e**((h*c)/(kb * T * lambdamn)) - 1) #Denominator of Planck's equation
    result = numerator / denominator
    return(result)
    

for lambdamn in range ( 100, 1000): #Calculating from wavelength 100nm to 1000nm
    lambda_m = lambdamn * 1e-9 #converting wavelength to nano meter by multiplying 10*-9
    radiation(lambda_m,T) #Callling Planck's equation function
    WaveLength.append(lambdamn) #Insert calculated wavelength into the list
    Energy.append(radiation(lambda_m,T)) #Insert calculated Spectral Radiance into list
    

plt.figure(figsize=(10, 6)) #Assigning size for the graph
plt.plot(WaveLength, Energy, 'b-', label=f"Black Body at T = {T} K") #Plotting Wave Length as X axsis and Spectral Radiance as Y axis
plt.xlabel("Wavelength (nm)") #Labeling X axis
plt.ylabel("Spectral Radiance (W/m³·sr)") #Labeling Y axsis
plt.title("Planck Spectral Radiance vs Wavelength") #Labeling title of the Axis
plt.grid(True) #Show grid
plt.axvline(x=501.8, color='r', linestyle='--', label="Highest spectral radiance") # show the peak spectral intensity at wavelength
plt.yscale('log')  # Log scale for better visualization
plt.legend() #Label the X and Y title as well as red line
plt.show()

#part b

#Wien displacement law to find peak spectral intensity

def Wien_displacementLaw(print_flag=True): #setting print_flag = False indicating it has not print the result yet
    #According to Wien displacement Law, Max Lambda * Temperature = 2.898*10^-3mK 
    #Thus to find Max Wave length, we just need to take the constant value 2.898*10^-3mK and divide by Temperature
    Max_waveLength =  2.898e-3 / T 
    Max_waveLength_nano = Max_waveLength *1e9 #Converting to meter
    Peak_Spectral = radiation(Max_waveLength,T) #Finding Peak spectral using Max wave length and Sun's temperature as parameter for Planck's equation
    if print_flag: 
        print("The peak spectral intensity of the curve",f"{Peak_Spectral}","W/m³·sr"," is at wave legnth:",f"{Max_waveLength_nano:.1f}","nm")
    return(Max_waveLength_nano) #Return Peak wave length for use in Part e)

Wien_displacementLaw() #Calling of the function 


# Part C to find total intensity emited by the sun in visble range between lambda 400nm to 700nm, we will use Planck equation and add them up from 400nm to 700nm

# Since integration is just adding all area under the graph, I used for loop to simplify the integrals
Current_intensity = 0 #Variable to calculate current lambda intensity
Total_intensity = 0 #Variable to store Current intensity
delta_x = 1e-9  # Step size in meters (1 nm)

for lambdamn in range ( 400, 700): #Looping from 400nm to 700nm in visible range
    lambda_m = lambdamn * 1e-9 #converting to meter
    Current_intensity = radiation(lambda_m,T) #Updating intensity with current calculated wavelength
    Total_intensity += Current_intensity * delta_x #Taking current intensity and add it to total intensity and keep adding until the loop ends at 700nm

print("The total intensity emited by the sun is",f"{Total_intensity}","W/m²")


# Part D 

sun_radius_meter = 696340e3 #sun radius in meter
earth_radius_meter = 6370e3 # earth radius in meter
distance = 1.496e8 #Distance between Sun and Earth 
StefanConstant = 5.670e-8 # Stefan-Boltzmannconstant

# To find power radiated per unit area we use I(T)=σT^4
# Since the sun is a sphere, the formula will be 4piR^2σT^4

def powerfraction():

    sun_power = 4 * np.pi * sun_radius_meter**2 * StefanConstant * T**4 #Total power radiated by the sun uniformly
    #since the sun radiate uniformly, the power will divide equally
    perArea = 4 * np.pi * distance**2
    Power = sun_power / perArea  #solar flux
    #since only one side of the earth is facing the sun, we assume the earth is a circle instead of full sphere
    
    Earth_face =  np.pi * earth_radius_meter**2 #Area of the earth on one side which is just a circle
    Earth_power = Power * Earth_face # Sunpower radiate over Earth area == Earth power from the sun that reaches the earth
    Powerfraction = Earth_power / sun_power #comparing the fraction of earth receiving sun's power
    print("The fraction of the sun's total power reaches earth and its athmosphere is:", f"{Powerfraction}")
    
powerfraction()

# # Part e)
# # By Wien Displacement Law as calculated from part b, the peak
# # wavelength to hit earth is 501.8nm which is Cyan in the visible light spectrum

def Visible_color():
    WaveLength = Wien_displacementLaw(print_flag=False) #Setting print_flag = False to avoid Wien displacement fucntion from printing the spectral intensity and nano wave length again
    if (WaveLength <= 625 and WaveLength >= 740):
        print("Red is the most intense")
    elif (WaveLength <625 and WaveLength >= 590):
        print("Orange is the most intense")
    elif (WaveLength <590 and WaveLength >= 565):
        print("Yellow is the most intense")
    elif (WaveLength <565 and WaveLength >= 520):
        print("Green is the most intense")
    elif (WaveLength <520 and WaveLength >= 500):
        print("Cyan is the most intense")
    elif (WaveLength <500 and WaveLength >= 435):
        print("Blue is the most intense")
    elif (WaveLength  <435 and WaveLength >= 380):
        print("Purple is the most intense")
    else:
        print("Not visible to human eye")

Visible_color()
