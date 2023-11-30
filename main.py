import random
import matplotlib.pyplot as plt

def initialize_population(population_size):
    population = {}
    for person_id in range(1, population_size + 1):
        # Each person starts uninfected with no time infected and alive
        population[person_id] = {'infected': False, 'time_infected': 0, 'dead': False}
    return population

def spread_infection(population, contagion_rate, num_interactions_per_day):
    for person_id, attributes in population.items():
        if not attributes['infected'] or attributes['dead']:
            continue
        for interaction in range(num_interactions_per_day):
            # Simulate interactions and infect others randomly
            if random.random() < contagion_rate:
                random_person = random.choice(list(population.keys()))
                # Don't infect already infected or dead individuals
                if not population[random_person]['infected'] and not population[random_person]['dead']:
                    population[random_person]['infected'] = True
    return population

def evolve_virus(day, contagion_rate, mortality_rate):
    # Example: Contagion and mortality rates increase gradually over time
    if day % 10 == 0:  # Increase rates every 10 days (you can adjust this)
        contagion_rate *= 1.2  # Increase contagion rate by 20%
        mortality_rate *= 1.1  # Increase mortality rate by 10%
    return contagion_rate, mortality_rate

def simulate_disease():
    population_size = int(input("Enter the total population size: "))
    total_duration = int(input("Enter the total duration of simulation (days): "))
    initial_infected_percentage = float(input("Enter the initial percentage of infected individuals (0-100): "))
    contagion_rate = float(input("Enter the initial contagion rate (0-1): "))
    mortality_rate = float(input("Enter the initial mortality rate (0-1): "))
    num_interactions_per_day = int(input("Enter the number of interactions per day: "))

    population = initialize_population(population_size)
    infected_count_list = []  # To store infected counts for each day
    contagion_rate_list = []  # To store contagion rates for each day
    mortality_rate_list = []  # To store mortality rates for each day
    
    # Infect initial percentage of population
    initial_infected = int(population_size * (initial_infected_percentage / 100))
    random_infected_people = random.sample(range(1, population_size + 1), initial_infected)
    for person_id in random_infected_people:
        population[person_id]['infected'] = True

    for day in range(1, total_duration + 1):
        # Evolve virus over time
        contagion_rate, mortality_rate = evolve_virus(day, contagion_rate, mortality_rate)
        contagion_rate_list.append(contagion_rate)
        mortality_rate_list.append(mortality_rate)
        
        # Simulate spread of infection
        population = spread_infection(population, contagion_rate, num_interactions_per_day)
        
        # Add events like special days (e.g., Olympics)
        if day == 50:  # Example: Olympics after 50 days
            # Perform specific actions/events
            pass
        
        # Calculate and store infected count for each day
        infected_count = sum(1 for person in population.values() if person['infected'])
        infected_count_list.append(infected_count)
        
    # Plotting the results
    plt.figure(figsize=(10, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(range(1, total_duration + 1), infected_count_list, marker='o', linestyle='-')
    plt.xlabel('Days')
    plt.ylabel('Infected Count')
    plt.title('Number of Infected Individuals Over Time')
    
    plt.subplot(2, 1, 2)
    plt.plot(range(1, total_duration + 1), contagion_rate_list, label='Contagion Rate', marker='o', linestyle='-')
    plt.plot(range(1, total_duration + 1), mortality_rate_list, label='Mortality Rate', marker='o', linestyle='-')
    plt.xlabel('Days')
    plt.ylabel('Rate')
    plt.title('Evolution of Contagion and Mortality Rates')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

simulate_disease()

