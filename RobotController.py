
from libGenetic import Individual
from libGenetic import Population
from robot import Maze
from robot import Robot
from robot import GeneticAlgorithm

maxGenerations = 1000

ruta = (
    [0, 0, 0, 0, 1, 0, 1, 3, 2],
    [1, 0, 1, 1, 1, 0, 1, 3, 1],
    [1, 0, 0, 1, 3, 3, 3, 3, 1],
    [3, 3, 3, 1, 3, 1, 1, 0, 1],
    [3, 1, 3, 3, 3, 1, 1, 0, 0],
    [3, 3, 1, 1, 1, 1, 0, 1, 1],
    [1, 3, 0, 1, 3, 3, 3, 3, 3],
    [0, 3, 1, 1, 3, 1, 0, 1, 3],
    [1, 3, 3, 3, 3, 1, 1, 1, 4])

maze = Maze(ruta)

ga = GeneticAlgorithm(200,0.05,0.9,2,10)
population = ga.init_population(50)

ga.eval_population(population,maze)

generation = 1
print("Iniciando RobotController....")
while ga.isTerminationConditionMet(generation,maxGenerations) == False:
    fittest = population.get_fittest(0)
    chromosome = fittest.chromosome
    robot = Robot(chromosome,maze,100)
    robot.run_final()
    print("Genearion ",generation)

    population = ga.crossover_population(population)
    population = ga.mutate_population(population)

    ga.eval_population(population,maze)
    generation = generation + 1

print("Best Solution")
