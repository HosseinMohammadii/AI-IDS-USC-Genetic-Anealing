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


IRAN_PROVINCES = ["Alborz", "Ardabil", "East Azerbaijan", "West Azerbaijan", "Bushehr", "Chaharmahal and Bakhtiari", "Fars", "Gilan", "Golestan", "Hamedan", "Hormozgan", "Ilam", "Isfahan",
                "Kerman", "Kermanshah", "North Khorasan", "Razavi Khorasan", "South Khorasan", "Khuzestan", "Kohgiluyeh and Boyer-Ahmad", "Kurdistan", "Lorestan", "Markazi", "Mazandaran",
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
    "Semnan": ["Razavi Khorasan", "North Khorasan", "Golestan", "Mazandaran", "Tehran", "Qom", "Isfahan", "South Khorasan"],
    "Tehran": ["Alborz", "Mazandaran", "Semnan", "Qom", "Markazi"],
    "Alborz": ["Qazvin", "Mazandaran", "Tehran", "Qom", "Markazi"],
    "Qazvin": ["Gilan", "Mazandaran", "Alborz", "Markazi", "Hamedan", "Zanjan"],
    "Zanjan": ["Kurdistan", "West Azerbaijan", "East Azerbaijan", "Ardabil", "Gilan", "Qazvin", "Hamedan"],
    "Kurdistan": ["West Azerbaijan", "Zanjan", "Hamedan", "Kermanshah"],
    "Kermanshah": ["Kurdistan", "Hamedan", "Lorestan", "Ilam"],
    "Hamedan": ["Kermanshah", "Kurdistan", "Zanjan", "Qazvin", "Markazi", "Lorestan", "Kermanshah"],
    "Markazi": ["Hamedan", "Qazvin", "Alborz", "Tehran", "Qom", "Isfahan", "Lorestan"],
    "Qom": ["Markazi", "Tehran", "Semnan", "Isfahan"],
    "Isfahan": ["Qom", "Semnan", "South Khorasan", "Yazd", "Fars", "Kohgiluyeh and Boyer-Ahmad", "Chaharmahal and Bakhtiari", "Lorestan", "Markazi"],
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
genomeSize = 31

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
while flag:

    chromosome.calfitness()
    cf1 = chromosome.fitness

    rr = random.randint(0, int(rep/100))

    chromosome2.chromosome = chromosome.chromosome

    for t in range(0, rr):
    # for t in range(0, 2):
        city = IRAN_PROVINCES[random.randint(0, genomeSize - 1)]
        color = random.choice(colors)
        if chromosome.chromosome[city] == color:
            continue
        chromosome2.chromosome[city] = color
        # rep = rep - stan/4 * (1 - maxCF)

    chromosome2.calfitness()
    cf2 = chromosome2.fitness
    # rep = rep + 3/maxCF
    rep = rep + stan*(1-maxCF)
    if maxCF > 0.94:
        rep = 100

    if cf2 > maxCF:
        maxCF = cf2
        if rep > 100:
            rep = 100
    # print(cf1)
    if cf2 == 1.0:
        print('found!')
        break

    # print("%d  %s " % (cf1, cf2))
    if cf2 > cf1:
        chromosome = chromosome2
        rep = rep - stan*4*(1-maxCF)
        # if rep > 2:
        #     rep = rep - 1
        # print("bozorggggggggggg")
    elif cf2 < cf1:
        k = k + 1
        rep = rep + stan/20*(1-maxCF)
        # print("koochikk")
        T = tempr4()
        T = T / 1000
        p = math.pow(math.e, ((cf2 - cf1)/T))
        # p = T/20
        # r = random.random()
        r = random.uniform(0, 1)
        # print("%a  %s  %s  %f  %g %s" % (cf2, cf1, T, p, r, maxCF))
        if r < p:
            chromosome = chromosome2
            print("yesss")


    print(maxCF)

