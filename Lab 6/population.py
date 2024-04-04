#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 6.3 Population Data
 # Due: 3/14/2022
 # author Kimora Bailey
 # version 1.0
 #
 # By turning in this code, I Pledge:
 #  1. That I have completed the programming assignment independently.
 #  2. I have not copied the code from a student or any source.
 #  3. I have not given my code to any student.
 #
 #---------------------------------------------------------------------

try:
    year = 1950

    filep = open("USPopulation.txt")

    population = []

    for line in filep.readlines():

        population.append(int(line.strip()))

    filep.close()

    average = sum(population)/len(population)

    high = low = 0

    for i in range(1, len(population)):

        if population[high]<population[i]:

            high = i

        if population[low]>population[i]:

            low = i

    print("The average annual change in population during the time period:", average)

    print("The year with the greatest increase in population during the time period is", high+year,"with",population[high])

    print("The year with the smallest increase in population during the time period is", low+year,"with",population[low])

except FileNotFoundError:

    print("Unable to open file")
