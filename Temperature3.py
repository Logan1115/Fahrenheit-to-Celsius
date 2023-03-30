#!/usr/bin/env python3
 
#...initialize looping variable, assume 'yes' as the first answer
continueYN = "y"
 
while continueYN == "y":
   #...get name from the user
   Name = input("Enter first name here, then press Enter: ")

   Name = Name
   
   #...get temperature input from the user
   sDegreeF = input("Enter next temperature in degrees Fahrenheit (F):")

   #...convert text entry to number value that can be used in equations
   nDegreeF = int(sDegreeF)
       
   #...convert temperature from F to Celsius
   nDegreeC = (nDegreeF - 32) * 5 / 9
 
   print ("Temperature in degrees Celcius is:", nDegreeC)
 
   #...check for temperature below freezing...
   if nDegreeF < 32 and nDegreeF > -60:
      print ("Pack long underwear and wear winter coat", Name,"!")

 #...check for temperature below freezing..
   if nDegreeF < -60:
      print ("You'd better be in the artic with that weather", Name, "!")
 
   #...check for it being a hot day...
   if nDegreeF > 100 and nDegreeF > 120:
      print ("Take a fan", Name, "!")

  #...check for it being a boiling day...
   if nDegreeF > 120:
      print ("Don't go outside! Turn up the AC to Max", Name, "!")
      
   continueYN = input("Input another?")
 
#exit the program
