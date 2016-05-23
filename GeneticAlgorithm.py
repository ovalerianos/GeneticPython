from Population import *
from Individual import *
import random as r

class GeneticAlgorithm:
  
 population_size = -1
 mutationrate    = 0.0
 crossover_rate  = 0.0
 elitism_count   = 1
 chromosome_length = 0

 def __init__(self,populationSize,mutationRate,crossoverRate,elitismCount):
   self.population_size = populationSize
   self.mutationrate    = mutationRate
   self.crossover_rate  = crossoverRate
   self.elitism_count   = elitismCount
 
 def init_population(self,cromosomeLength):
        self.chromosome_length=cromosomeLength
        population = Population(self.population_size,self.chromosome_length)
        return population
 
 def calc_fitness(self,individual):
        correctGene = 0
        for geneIndex in range(individual.get_chromosome_len()):
            if individual.get_gene(geneIndex) == 1:
                correctGene = correctGene + 1
        
        fitness = round(float(correctGene)/float(individual.get_chromosome_len()),14)
        individual.set_fitness(fitness)
        
        return fitness

 def eval_population(self,population):
     populationFitness = 0
     for index in range(population.size()):
        populationFitness = populationFitness + self.calc_fitness(population.get_individual(index))
     
     population.set_population_fitness(populationFitness)
     print "populationFitness ",populationFitness
     return population
 
 
 def isTerminationConditionMet(self,population):
    for index in range(population.size()):
        if population.get_individual(index).get_fitness() == 1:
            return True
    
    return False

 def select_parent(self,population):
     
    populationFitness    = population.get_population_fitness()
    rouleteWheelPosition = r.random() * populationFitness
    
    spinWheel = 0.0
    for index in range(population.size()):
        individual = population.get_individual(index)
        spinWheel = spinWheel + individual.get_fitness()
        if spinWheel >= rouleteWheelPosition:
            return individual
    return population.get_individual(population.size()-1)

 def crossover_population(self,population):
    #Crear nueva poblacion
    print "Crossover"
    new_population = Population(population.size(),self.chromosome_length)

    for populationIndex in range(population.size()):
        parent_1 = population.get_fittest(populationIndex)

        if self.crossover_rate > r.random() and populationIndex > self.elitism_count:
            #Inicia Offspring
            individualOffSpring = Individual(parent_1.get_chromosome_len())
            #Encontrar segundo padre
            parent_2 = self.select_parent(population)

            #Loop para todos los genome
            for geneIndex in range(parent_1.get_chromosome_len()):
                if 0.5 > r.random():
                    individualOffSpring.set_gene(geneIndex,parent_1.get_gene(geneIndex))
                else:
                    individualOffSpring.set_gene(geneIndex,parent_2.get_gene(geneIndex))
            new_population.set_individual(populationIndex,individualOffSpring)
        else:
            new_population.set_individual(populationIndex,parent_1)
        print new_population.get_individual(populationIndex).chromosome

    return new_population

 def mutate_population(self,population):
    new_population = Population(self.population_size,self.chromosome_length)

    for populationIndex in range(population.size()):

        individual = population.get_fittest(populationIndex)

        for geneIndex in range(individual.get_chromosome_len()):
            if populationIndex >= self.elitism_count:
                #El gene necesita mutation?
                if self.mutationrate > r.random():
                    newGene = -1
                    if individual.get_gene(geneIndex) == 1:
                        newGene = 0
                    else:
                        newGene = 1
                    
                    individual.set_gene(geneIndex,newGene)

        new_population.set_individual(populationIndex,individual)

    return new_population




    
    