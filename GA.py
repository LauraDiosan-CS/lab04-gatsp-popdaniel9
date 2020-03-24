from random import randint

from Chromosome import Chromosome


class GA:
    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param['popSize']):
            crom = Chromosome(self.__problParam)
            self.__population.append(crom)

    def evaluation(self):
        net = self.__problParam['net']
        for crom in self.__population:
            crom.fitness = self.__problParam['function'](net, crom.repres)

    def worstChromosome(self):
        worst = self.__population[0]
        for crom in self.__population:
            if (crom.fitness > worst.fitness):
                best = crom
        return worst

    def bestChromosome(self):
        best = self.__population[0]
        for crom in self.__population:
            if (crom.fitness < best.fitness):
                best = crom
        return best


    def selection(self):
        p1 = randint(0, self.__param['popSize'] - 1)
        p2 = randint(0, self.__param['popSize'] - 1)
        if (self.__population[p1].fitness < self.__population[p2].fitness):
            return p1
        else:
            return p2

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param['popSize']):
            pop1 = self.__population[self.selection()]
            pop2 = self.__population[self.selection()]
            off = pop1.crossover(pop2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['popSize'] - 1):
            pop1 = self.__population[self.selection()]
            pop2 = self.__population[self.selection()]
            off = pop1.crossover(pop2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationSteadyState(self):
        for _ in range(self.__param['popSize']):
            pop1 = self.__population[self.selection()]
            pop2 = self.__population[self.selection()]
            off = pop1.crossover(pop2)
            off.mutation()
            off.fitness = self.__problParam['function'](off.repres)
            worst = self.worstChromosome()
            if (off.fitness < worst.fitness):
                worst = off