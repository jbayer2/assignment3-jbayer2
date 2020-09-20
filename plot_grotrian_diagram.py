# -*- coding: utf-8 -*-
"""
Created on Tue May 15 18:00:40 2018

@author: jbayer
"""

import numpy as np
from processTransitions import extract
from pylab import plot,show,xlabel,ylabel,title,legend,ylim,xticks,scatter,savefig,gca,annotate
from collections import  Counter
#for testing purposes only
data=extract("Atoms/ca1.atom")

#store the data so it can be seen in the variable explorer    
Element = data[0] + data[1]
ionization_energy = data[2]
number_of_energy_levels = data[3]
number_of_lines = data[4]
association_numbers_data_1 = data[5]
statistical_weights = data[6]
energies = data[7]
lower_energy = data[8]
higher_energy = data[9]
oscillator_strength = data[10] 
orbital_information = data[11]



#let's first set up the graph that will be used to show the diagram
#*****************************************************************************#

##Set Up##
# letting the range: {0,1}, and the domain: {0,ionization_energy}, set up orbitals shown on 

spacingArray=np.linspace(0.05,0.95,5)#for S -> G orbitals
#spacingArray=np.linspace(0.05,0.95,6)#for S -> G and unknown X orbitals

#label orbitals along the axis
xticks(spacingArray,['S','P','D','F','G'])
#xticks(spacingArray,['S','P','D','F','G','X'])

#label axis of diagram
ylabel("energy [1/cm]")
xlabel("orbital")

#*****************************************************************************#



#look and plot all e levels and transitions between them
#*****************************************************************************#

#store x and y values for specific transitions
xHigh = []
yHigh = []
xLow = []
yLow = []
orbitalHigh = 0# holds the position along the x axis (hence level)
orbitalLow = 0# holds the position along the x axis (hence level)
count = 0# counts the number of transitions between S, P, D, F, and G oribtals
#temp
store = []
#storeH = []
#storeL = []
#the following code is to map all transitions, even between undefined (X) orbitals
"""
for n in range(0,(len(higher_energy)),1):
    
        criterionMetHigh=False# wether is belongs to the S, P, D, F, or G orbitals
        criterionMetLow=False# wether is belongs to the S, P, D, F, or G orbitals
        
        highANum=higher_energy[n]# this gives an association number
        lowANum=lower_energy[n]# this gives an association number

        higherEnergyLvl = association_numbers_data_1.index(highANum)# finds corresponding energy level via association number
        lowerEnergyLvl = association_numbers_data_1.index(lowANum)# finds corresponding energy level via association number

        higherInformation = orbital_information[higherEnergyLvl]# get the information on the orbitals in the transtion
        lowerInformation = orbital_information[lowerEnergyLvl]# get the information on the orbitals in the transtion

        
        #check and see which orbital the level belongs to, and put plot it
        if (higherInformation.find('S')!=-1):
            criterionMetHigh=True
            xHigh.append(spacingArray[0])
            yHigh.append(energies[higherEnergyLvl])

            
        elif (higherInformation.find('P')!=-1):
            criterionMetHigh=True
            xHigh.append(spacingArray[1])
            yHigh.append(energies[higherEnergyLvl])

            
        elif (higherInformation.find('D')!=-1):
            criterionMetHigh=True
            xHigh.append(spacingArray[2])
            yHigh.append(energies[higherEnergyLvl])

            
        elif (higherInformation.find('F')!=-1):
            criterionMetHigh=True
            xHigh.append(spacingArray[3])
            yHigh.append(energies[higherEnergyLvl])

            
        elif (higherInformation.find('G')!=-1):
            criterionMetHigh=True
            xHigh.append(spacingArray[4])
            yHigh.append(energies[higherEnergyLvl])

            
        else:
            xHigh.append(spacingArray[5])
            yHigh.append(energies[higherEnergyLvl])
            
        #check and see which orbital the level belongs to, and put plot it
        if (lowerInformation.find('S')!=-1):
            criterionMetLow=True
            xLow.append(spacingArray[0])
            yLow.append(energies[lowerEnergyLvl])

            
        elif (lowerInformation.find('P')!=-1):
            criterionMetLow=True
            xLow.append(spacingArray[1])
            yLow.append(energies[lowerEnergyLvl])

            
        elif (lowerInformation.find('D')!=-1):
            criterionMetLow=True
            xLow.append(spacingArray[2])
            yLow.append(energies[lowerEnergyLvl])

            
        elif (lowerInformation.find('F')!=-1):
            criterionMetLow=True
            xLow.append(spacingArray[3])
            yLow.append(energies[lowerEnergyLvl])

            
        elif (lowerInformation.find('G')!=-1):
            criterionMetLow=True
            xLow.append(spacingArray[4])
            yLow.append(energies[lowerEnergyLvl])

            
        else:
            xLow.append(spacingArray[5])
            yLow.append(energies[lowerEnergyLvl])
        
        
        plot([xLow[n],xHigh[n]],
             [yLow[n],yHigh[n]],
             linewidth=0.25)
"""

#the following plots only the S, P, D, F, and G orbitals and their transitions
for n in range(0,(len(higher_energy)),1):
    
        criterionMetHigh=False# wether is belongs to the S, P, D, F, or G orbitals
        criterionMetLow=False# wether is belongs to the S, P, D, F, or G orbitals
        
        highANum=higher_energy[n]# this gives an association number
        lowANum=lower_energy[n]# this gives an association number

        higherEnergyLvl = association_numbers_data_1.index(highANum)# finds corresponding energy level via association number
        lowerEnergyLvl = association_numbers_data_1.index(lowANum)# finds corresponding energy level via association number

        higherInformation = orbital_information[higherEnergyLvl]# get the information on the orbitals in the transtion
        lowerInformation = orbital_information[lowerEnergyLvl]# get the information on the orbitals in the transtion

        #store.append([("H:" + str(higherEnergyLvl) + "," + str(higherInformation)),("L:" + str(lowerEnergyLvl) + "," + str(lowerInformation))])
        
        #check and see which orbital the level belongs to, and put plot it
        if (higherInformation.find('S')!=-1):# and energies[higherEnergyLvl] <= 40000):
            criterionMetHigh=True
            orbitalHigh=0
            #xHigh.append(spacingArray[orbitalHigh])
            #yHigh.append(energies[higherEnergyLvl])
            
        elif (higherInformation.find('P')!=-1):# and energies[higherEnergyLvl] <= 40000):
            criterionMetHigh=True
            orbitalHigh=1
            #xHigh.append(spacingArray[orbitalHigh])
            #yHigh.append(energies[higherEnergyLvl])
            
        elif (higherInformation.find('D')!=-1):# and energies[higherEnergyLvl] <= 40000):
            criterionMetHigh=True

            orbitalHigh=2
            #xHigh.append(spacingArray[orbitalHigh])
            #yHigh.append(energies[higherEnergyLvl])
            
        elif (higherInformation.find('F')!=-1):# and energies[higherEnergyLvl] <= 40000):
            criterionMetHigh=True
            orbitalHigh=3
            #xHigh.append(spacingArray[orbitalHigh])
            #yHigh.append(energies[higherEnergyLvl])
            
        elif (higherInformation.find('G')!=-1):# and energies[higherEnergyLvl] <= 40000):
            criterionMetHigh=True
            orbitalHigh=4
            #xHigh.append(spacingArray[orbitalHigh])
            #yHigh.append(energies[higherEnergyLvl])
            
            
            
        #check and see which orbital the level belongs to, and put plot it
        if (lowerInformation.find('S')!=-1):# and energies[higherEnergyLvl] <= 40000):
            criterionMetLow=True
            orbitalLow=0
            #xLow.append(spacingArray[orbitalLow])
            #yLow.append(energies[lowerEnergyLvl])
            
        elif (lowerInformation.find('P')!=-1):# and energies[higherEnergyLvl] <= 40000):        
            criterionMetLow=True
            orbitalLow=1
            #xLow.append(spacingArray[orbitalLow])
            #yLow.append(energies[lowerEnergyLvl])
            
        elif (lowerInformation.find('D')!=-1):# and energies[higherEnergyLvl] <= 40000):
            criterionMetLow=True
            orbitalLow=2
            #xLow.append(spacingArray[orbitalLow])
            #yLow.append(energies[lowerEnergyLvl])
            
        elif (lowerInformation.find('F')!=-1):# and energies[higherEnergyLvl] <= 40000):
            criterionMetLow=True
            orbitalLow=3
            #xLow.append(spacingArray[orbitalLow])
            #yLow.append(energies[lowerEnergyLvl])
            
            
        elif (lowerInformation.find('G')!=-1):# and energies[higherEnergyLvl] <= 40000):
            criterionMetLow=True
            orbitalLow=4
            #xLow.append(spacingArray[orbitalLow])
            #yLow.append(energies[lowerEnergyLvl])

        # only plot if both the higher and lower orbitals in a transition are S, P , D, F, or G
        if(criterionMetHigh== True and criterionMetLow==True):# and energies[higherEnergyLvl] <= 40000):
            xLow.append(spacingArray[orbitalLow])
            yLow.append(energies[lowerEnergyLvl])

            xHigh.append(spacingArray[orbitalHigh])
            yHigh.append(energies[higherEnergyLvl])

            plot([xLow[-1],xHigh[-1]],
                 [yLow[-1],yHigh[-1]],
                 linewidth=0.25)
            if (orbital_information[lowerEnergyLvl] not in store):

    
                store.append(orbital_information[lowerEnergyLvl])
    
                #annotate(orbital_information[higherEnergyLvl],
                #        xy=(xHigh[-1] + 0.035, energies[higherEnergyLvl]))
                
                #annotate(orbital_information[lowerEnergyLvl],
                #     xy=(xLow[-1] + 0.035, energies[lowerEnergyLvl]))
            
            #count+=1


#plot the e levels

#see how many transitions are in each energy levels (testing)
#print(Counter(xLow))
#print(Counter(xHigh))
            
#gca().invert_yaxis()

# look through each shell and only label shells 
for shell in store:
    indicies = [i for i, currentShell in enumerate(orbital_information)
    if currentShell == shell]# get the indicies of all of all lower orbitals shells
    energy = 1e16# place holder for lowest energy that will help place a annotated label for a shell
    spacing = 0# holds the spacing index in the spacing array for the shell label
    
    #summ += len(indicies)
    
    if(shell.find('S')!=-1):
        spacing = 0
    elif(shell.find('P')!=-1):
        spacing = 1
    elif(shell.find('D')!=-1):
        spacing = 2
    elif(shell.find('F')!=-1):
        spacing = 3
    elif(shell.find('G')!=-1):
            spacing = 4
    
    for someShell in indicies:


        currentEnergy = energies[someShell]
        
        if (currentEnergy <= energy):
            energy = currentEnergy
        

            
    annotate(shell, xy=(spacingArray[spacing] + 0.055, energy))
            


title(Element + " Grotrian Diagram")
scatter(xLow,yLow,marker="_",s=900,c='#000000')
scatter(xHigh,yHigh,marker="_",s=900,c='#000000')
savefig("GrotrianDiagramCaI.png",dpi=1200)
show()

#*****************************************************************************#

