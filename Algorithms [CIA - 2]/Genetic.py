import random
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
df=pd.read_csv(r"C:\Users\DELL\Downloads\Bank_Personal_Loan_Modelling.csv")
df.drop(['ID','ZIP Code'],axis=1,inplace=True)
x=df.drop('Personal Loan',axis=1).values
y=df['Personal Loan'].values.reshape(-1,1)
model = Sequential()
model.add(Dense(12, input_shape=(8,), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=150, batch_size=10)

def fitness(individual):
    score = ...
    return score

def genetic_algorithm(population_size, gene_length, mutation_rate, generations):
    
    population = []
    for i in range(population_size):
        individual = [random.randint(0, 1) for j in range(gene_length)]
        population.append(individual)

    for generation in range(generations):
        fitness_scores = [fitness(individual) for individual in population]

        parents = []
        for i in range(population_size):
            parent1 = population[roulette_wheel_selection(fitness_scores)]
            parent2 = population[roulette_wheel_selection(fitness_scores)]
            parents.append((parent1, parent2))

        population = []
        for parent1, parent2 in parents:
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            population.append(child)

    return max(population, key=fitness)

def roulette_wheel_selection(fitness_scores):
    total_fitness = sum(fitness_scores)
    r = random.uniform(0, total_fitness)
    current_fitness = 0
    for i in range(len(fitness_scores)):
        current_fitness += fitness_scores[i]
        if current_fitness > r:
            return i

def crossover(parent1, parent2):
    child = ...
    return child

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

best_individual = genetic_algorithm(population_size=100, gene_length=10, mutation_rate=0.01, generations=100)
model.fit(X, y, epochs=150, batch_size=10)
print("Best individual:", best_individual)
