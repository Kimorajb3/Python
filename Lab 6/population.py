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
