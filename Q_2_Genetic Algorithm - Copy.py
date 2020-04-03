import random
import matplotlib.pyplot as plt
import numpy as np


class Chromosome:

    def __init__(self):
        self.chromosome = {}
        self.fitness = 0

    def generaterandom(self):
        # print('Generate random called ')
        for city in IRAN_PROVINCES:
            self.chromosome[city] = random.choice(colors)

    def calfitness(self):
        sorat = 0.0
        makhraj = 0.0
        for city in IRAN_PROVINCES:
            color_base = self.chromosome[city]
            for city2 in IRAN_MAP[city]:
                if color_base != self.chromosome[city2]:
                    sorat = sorat + 1
                makhraj = makhraj + 1
        self.fitness = sorat / makhraj


IRAN_PROVINCES = ["Alborz", "Ardabil", "East Azerbaijan", "West Azerbaijan", "Bushehr", "Chaharmahal and Bakhtiari",
                  "Fars", "Gilan", "Golestan", "Hamedan", "Hormozgan", "Ilam", "Isfahan",
                  "Kerman", "Kermanshah", "North Khorasan", "Razavi Khorasan", "South Khorasan", "Khuzestan",
                  "Kohgiluyeh and Boyer-Ahmad", "Kurdistan", "Lorestan", "Markazi", "Mazandaran",
                  "Qazvin", "Qom", "Semnan", "Sistan and Baluchestan", "Tehran", "Yazd", "Zanjan"]

IRAN_MAP = {
    "West Azerbaijan": ["East Azerbaijan", "Zanjan", "Kurdistan"],
    "East Azerbaijan": ["West Azerbaijan", "Ardabil", "Zanjan"],
    "Ardabil": ["East Azerbaijan", "Zanjan", "Gilan"],
    "Gilan": ["Ardabil", "Zanjan", "Qazvin", "Mazandaran"],
    "Mazandaran": ["Gilan", "Qazvin", "Alborz", "Tehran", "Semnan", "Golestan"],
    "Golestan": ["Mazandaran", "Semnan", "North Khorasan"],
    "North Khorasan": ["Golestan", "Semnan", "Razavi Khorasan"],
    "Razavi Khorasan": ["North Khorasan", "Semnan", "South Khorasan"],
    "Semnan": ["Razavi Khorasan", "North Khorasan", "Golestan", "Mazandaran", "Tehran", "Qom", "Isfahan",
               "South Khorasan"],
    "Tehran": ["Alborz", "Mazandaran", "Semnan", "Qom", "Markazi"],
    "Alborz": ["Qazvin", "Mazandaran", "Tehran", "Qom", "Markazi"],
    "Qazvin": ["Gilan", "Mazandaran", "Alborz", "Markazi", "Hamedan", "Zanjan"],
    "Zanjan": ["Kurdistan", "West Azerbaijan", "East Azerbaijan", "Ardabil", "Gilan", "Qazvin", "Hamedan"],
    "Kurdistan": ["West Azerbaijan", "Zanjan", "Hamedan", "Kermanshah"],
    "Kermanshah": ["Kurdistan", "Hamedan", "Lorestan", "Ilam"],
    "Hamedan": ["Kermanshah", "Kurdistan", "Zanjan", "Qazvin", "Markazi", "Lorestan", "Kermanshah"],
    "Markazi": ["Hamedan", "Qazvin", "Alborz", "Tehran", "Qom", "Isfahan", "Lorestan"],
    "Qom": ["Markazi", "Tehran", "Semnan", "Isfahan"],
    "Isfahan": ["Qom", "Semnan", "South Khorasan", "Yazd", "Fars", "Kohgiluyeh and Boyer-Ahmad",
                "Chaharmahal and Bakhtiari", "Lorestan", "Markazi"],
    "South Khorasan": ["Razavi Khorasan", "Semnan", "Isfahan", "Yazd", "Kerman", "Sistan and Baluchestan"],
    "Yazd": ["Isfahan", "South Khorasan", "Kerman", "Fars"],
    "Fars": ["Yazd", "Isfahan", "Kohgiluyeh and Boyer-Ahmad", "Bushehr", "Hormozgan", "Kerman"],
    "Kohgiluyeh and Boyer-Ahmad": ["Fars", "Isfahan", "Chaharmahal and Bakhtiari", "Khuzestan", "Bushehr"],
    "Chaharmahal and Bakhtiari": ["Isfahan", "Kohgiluyeh and Boyer-Ahmad", "Khuzestan", "Lorestan"],
    "Khuzestan": ["Bushehr", "Kohgiluyeh and Boyer-Ahmad", "Chaharmahal and Bakhtiari", "Lorestan", "Ilam"],
    "Ilam": ["Khuzestan", "Lorestan", "Kermanshah"],
    "Lorestan": ["Ilam", "Kermanshah", "Hamedan", "Markazi", "Isfahan", "Chaharmahal and Bakhtiari", "Khuzestan"],
    "Bushehr": ["Khuzestan", "Kohgiluyeh and Boyer-Ahmad", "Fars", "Hormozgan"],
    "Hormozgan": ["Bushehr", "Fars", "Kerman", "Sistan and Baluchestan"],
    "Kerman": ["Fars", "Yazd", "South Khorasan", "Sistan and Baluchestan", "Hormozgan"],
    "Sistan and Baluchestan": ["Hormozgan", "Kerman", "South Khorasan"]
}


def crossover(ch1, ch2):
    cities = ch1.chromosome.keys()
    cities = list(cities)
    random.shuffle(cities)
    r = random.randint(0, len(cities))
    cities1 = cities[:r]
    cities2 = cities[r:]
    childdict = {}
    for city in cities1:
        childdict[city] = ch1.chromosome[city]
    for city in cities2:
        childdict[city] = ch2.chromosome[city]
    childd = Chromosome()
    childd.chromosome = childdict
    return childd


blue = 1
red = 2
green = 3
white = 4
colors = [1, 2, 3, 4]

numberOfGenerations = 200
populationSize = 300
tornumentSize = 15
mutationRate = 0.04


population = []
newPopulation = []
selectNumber = populationSize / tornumentSize
genomeSize = 31
mutatedGenomes = populationSize * genomeSize * mutationRate
randomSelected = []
parents = []
worst = []
avg = []
best = []

for i in range(0, populationSize):
    population.append(Chromosome())
    population[i].generaterandom()

for n in range(0, numberOfGenerations):

    for p in range(0, populationSize):
        # print(' %d  %s' % (len(population), p))
        population[p].calfitness()

    ws = 10
    bs = 0
    av = 0
    for ch in population:
        rty = ch.fitness
        if rty < ws:
            ws = rty
        if rty > bs:
            bs = rty
        av += rty / len(population)

    best.append(bs)
    worst.append(ws)
    avg.append(av)

    parents.clear()
    for i in range(populationSize):
        randomSelected.clear()
        for j in range(tornumentSize):
            r = random.randint(0, populationSize - 1)
            randomSelected.append(population[r])
        randomSelected.sort(key=lambda xx: xx.fitness)
        randomSelected.reverse()
    parents.append(randomSelected[0])


    newPopulation.clear()
    for i in range(0, populationSize):
        r1 = random.randint(0, len(parents) - 1)
        r2 = random.randint(0, len(parents) - 1)
        child = crossover(parents[r1], parents[r2])
        newPopulation.append(child)

    for j in range(0, int(mutatedGenomes) - 1):
        r1 = random.randint(0, len(newPopulation) - 1)
        r2 = random.choice(IRAN_PROVINCES)
        r3 = random.choice(colors)
        newPopulation[r1].chromosome[r2] = r3

    population = newPopulation

for chromosome in population:
    chromosome.calfitness()

population.sort(key=lambda x: x.fitness)
population.reverse()

print('final population: ')
for chromosome in population:
    print(chromosome.fitness)

# plt.plot(best, color='green')
# # plt.title('BEST')
# # plt.show()
#
# plt.plot(avg, color='blue')
# plt.title('Average')
# plt.show()
#
# plt.plot(worst, color='red')
#
# plt.title('WORST')
# plt.show()

x = np.linspace(0, populationSize, populationSize)

plt.plot(best, label='Best')
plt.plot(avg, label='Average')
plt.plot(worst, label='Worst')
plt.plot(worst)

plt.xlabel('Generation')
plt.ylabel('fitness')

plt.title("Nemudar")

plt.legend()

plt.show()
