#Clase que determina el una poblacion en comun con la clase Individual
#Omar Valeriano
import random
from Individual import *
import operator
class Population:
 populationSize = 1    
 population = range(populationSize)
 populationFitness = -1
                       
 def initX(self,populationSize):
  self.population = range(populationSize)
  self.populationFitness = -1

 def __init__(self,populationSize,chromosomeLenght):
  self.population = range(populationSize)
  count=0
  while count < populationSize:
   individual = Individual(chromosomeLenght)
   self.population[count] = individual
   count = count + 1
 
 def get_fittest(self,offset):
   self.population.sort(key=operator.attrgetter('fitness'))
   individual = self.population[offset]
   return individual
 
 def set_population_fitness(self,populationFitness):
  self.populationFitness = populationFitness

 def get_population_fitness(self):
  return self.populationFitness
 
 def size(self):
  return len(self.population)
 
 def set_individual(self,offset,individual):
  self.population[offset]=individual
  return self.population[offset]
  
 def get_individual(self,offset):
  return self.population[offset]

 def get_population(self):
  return self.population
 
 def shuffle(self):
   
   for index in range(len(self.population)):
      indexTemp   = random.randint(1,len(self.population)-1)
      individualA = self.population[indexTemp]

      self.population[indexTemp] = self.population[index]
      self.population[index]     = individualA







