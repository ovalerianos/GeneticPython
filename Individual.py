
#Clase que determina el Gen de un objecto Individual
#Omar Valeriano
import random
import numpy as np
class Individual:

  fitness    = -1
  chromosomeLength=0
  chromosome = range(chromosomeLength)

  def __init__(self,chromosomeLength):
        self.chromosomeLength = chromosomeLength
        self.chromosome = range(self.chromosomeLength)
        self.randx()
  
#Metodo que genera un Gen aleatorio      
  def randx(self):
     genex = 0
     while genex < self.chromosomeLength:
      if 0.5 > random.random():
       self.set_gene(genex,1)
      else:
       self.set_gene(genex,0)          
      genex = genex + 1
    

  def set_gene(self,offset, gene):
      self.chromosome[offset] = gene

  def get_chromosome_len(self):
      return len(self.chromosome)
    
  def get_gene(self,offset):
      return self.chromosome[offset]

  def set_fitness(self,fitness):
        self.fitness=fitness

  def get_fitness(self):
      return self.fitness      

  def to_string(self):
      return self.chromosome
              
      
