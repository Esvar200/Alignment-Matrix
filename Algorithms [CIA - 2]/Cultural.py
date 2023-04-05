import pandas as pd
from sklearn.model_selection import train_test_split
import random
df=pd.read_csv(r"C:\Users\DELL\Downloads\Bank_Personal_Loan_Modelling.csv")
df.drop(['ID','ZIP Code'],axis=1,inplace=True)
x=df.drop('Personal Loan',axis=1).values
y=df['Personal Loan'].values.reshape(-1,1)

problem_size = 10
population_size = 50
num_iterations = 100
belief_space = [x.values() for i in range(problem_size)]
population = [[y.values() for i in range(problem_size)] for j in range(population_size)]
def fitness(individual):
    return sum([(individual[i] - belief_space[i])**2 for i in range(problem_size)])

def learning(population):
    for i in range(len(population)):
        for j in range(problem_size):
            if random.random() < 0.1:
                population[i][j] += random.uniform(-0.1, 0.1)

def cultural_algorithm(population, belief_space, fitness, learning, num_iterations):
    for iteration in range(num_iterations):
        for individual in population:
            individual_fitness = fitness(individual)
            if individual_fitness < fitness(belief_space):
                belief_space = individual
        learning(population)
    return belief_space

best_individual = cultural_algorithm(population, belief_space, fitness, learning, num_iterations)
print('Fitness:', fitness(best_individual))
