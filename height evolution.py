import random

class Organism:
    def __init__(self, height):
        self.height = height  # Initialize the organism with a height attribute
        
    def reproduce(self, average_height):
        # Calculate the probability of reproduction based on height relative to the average height
        if self.height < average_height:
            # If height is below average, lower chance of reproduction
            probability = 0.7
        else:
            # If height is above average, higher chance of reproduction
            probability = 0.999
        # Check if reproduction occurs based on the probability
        if random.random() < probability:
            # Mutation can occur during reproduction
            mutation = random.choice([-1, 0, 1])  # Small mutation in height, either -1, 0, or 1
            return Organism(max(0, self.height + mutation))  # New organism with mutated height (non-negative)
        else:
            return None  # No reproduction

def generate_population(population_height, initial_height_range):
    # Create a population of organisms with random heights within the specified range
    return [Organism(random.randint(*initial_height_range)) for _ in range(population_height)]

def evolve(population, generations):
    for _ in range(generations):
        next_generation = []
        # Calculate the average height of the population
        average_height = sum(organism.height for organism in population) / len(population)
        # Reproduce each organism in the population
        for organism in population:
            new_organism = organism.reproduce(average_height)
            if new_organism:
                next_generation.append(new_organism)
        population = next_generation  # Update the population with the next generation
    return population

if __name__ == "__main__":
    population_height = 100
    initial_height_range = (1, 10)  # Initial height range for organisms
    generations = 100
    
    population = generate_population(population_height, initial_height_range)
    
    final_population = evolve(population, generations)
    
    # Print final heights of the population
    print("Final heights of the population:")
    for organism in final_population:
        print(organism.height)
