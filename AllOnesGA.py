

import numpy as np
from Individual import *
from Population import *
from GeneticAlgorithm import *
x=Population(50,10)
import operator
import random as r


 def test_genetic():

 	ga = GeneticAlgorithm(100,0.01,0.95,10)

 	#Inicia poblacion
 	population = ga.init_population(50)

 	population = ga.eval_population(population)

 	generation = 1

 	while ga.isTerminationConditionMet(population) == False:

 		population = ga.crossover_population(population)

 		population = ga.mutate_population(population)

 		population = ga.eval_population(population)

 		generation = generation + 1

 	print "Best Solution",population.get_fittest(0)


