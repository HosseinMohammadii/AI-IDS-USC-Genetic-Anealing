import random
import math

class Chromosome:

    def __init__(self):
        self.chromosome = {}
        self.fitness = 0.0

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


# IRAN_PROVINCES = ["Alborz", "Ardabil", "East Azerbaijan", "West Azerbaijan", "Bushehr", "Chaharmahal and Bakhtiari", "Fars", "Gilan", "Golestan", "Hamedan", "Hormozgan", "Ilam", "Isfahan",
#                 "Kerman", "Kermanshah", "North Khorasan", "Razavi Khorasan", "South Khorasan", "Khuzestan", "Kohgiluyeh and Boyer-Ahmad", "Kurdistan", "Lorestan", "Markazi", "Mazandaran",
#                 "Qazvin", "Qom", "Semnan", "Sistan and Baluchestan", "Tehran", "Yazd", "Zanjan"]

IRAN_PROVINCES = ["A", "B", "C", "D", "E"]
IRAN_MAP = {
    "A": ["D", "C", "B", "E"],
    "B": ["A", "C"],
    "C": ["B", "A", "D"],
    "D": ["C", "A", "E"],
    "E": ["A", "D"]
}




def tempr1():
    # print(a**k)
    u = float()
    u = math.pow(a, k)
    u = T0 * u
    return u


def tempr2():
    return T0/(1 + a * (math.log10(1+k)))


def tempr3():
    return T0/(1 + a*k)


def tempr4():
    return T0/(1 + a * math.pow(k, 2))


blue = 1
red = 2
green = 3
white = 4
colors = [1, 2, 3, 4]

population = []
newPopulation = []

chromosome = Chromosome()
chromosome2 = chromosome
genomeSize = 5

T0 = 700.0
k = 1.0
a = 0.004
T = 0.0
flag = True
maxCF = 0.0000001
chromosome.generaterandom()
p = 1.0
rep = 200
stan = 20
mut_rate = 1
while flag:

    chromosome.calfitness()
    cf1 = chromosome.fitness

    # rr = random.randint(0, int(rep/100))
    rr = mut_rate
    chromosome2.chromosome = chromosome.chromosome.copy()

    for t in range(0, rr):
        city = IRAN_PROVINCES[random.randint(0, genomeSize - 1)]
        color = random.choice(colors)
        if chromosome.chromosome[city] == color:
            continue
        chromosome2.chromosome[city] = color
        # rep = rep - stan/4 * (1 - maxCF)

    chromosome2.calfitness()
    cf2 = chromosome2.fitness

    if cf2 > cf1:
        chromosome.chromosome = chromosome2.chromosome.copy()
    if cf2 == 1.0:
        print('found!')
        print(chromosome2.chromosome)
        break

    if cf2 < cf1:
        T = tempr4()
        T = T / 500
        p = math.pow(math.e, ((cf2 - cf1) / T))
        r = random.random()
        if r < p:
            chromosome.chromosome = chromosome2.chromosome.copy()

    T0 -= 1
    print(cf1)

