import random
import matplotlib.pyplot as plt

def initialize_population(population_size):
    population = {}
    for person_id in range(1, population_size + 1):
        # Each person starts uninfected with no time infected and alive
        population[person_id] = {'infected': False, 'time_infected': 0, 'dead': False}
    return population

def spread_infection(population, contagion_rate, num_interactions_per_day, mortality_rate):
    for person_id, attributes in population.items():
        if not attributes['infected'] or attributes['dead']:
            continue
        for interaction in range(num_interactions_per_day):
            if random.random() < contagion_rate:
                random_person = random.choice(list(population.keys()))
                if not population[random_person]['infected'] and not population[random_person]['dead']:
                    population[random_person]['infected'] = True
                    if random.random() < mortality_rate:
                        population[random_person]['dead'] = True
    return population

def evolve_virus(day, contagion_rate, mortality_rate):
    if day % 10 == 0:
        contagion_rate *= 1.2
        mortality_rate *= 1.1
    return contagion_rate, mortality_rate

def simulate_disease():
    population_size = int(input("Enter the total population size: "))
    total_duration = int(input("Enter the total duration of simulation (days): "))
    initial_infected_percentage = float(input("Enter the initial percentage of infected individuals (0-100): "))
    contagion_rate = float(input("Enter the initial contagion rate (0-1): "))
    mortality_rate = float(input("Enter the initial mortality rate (0-1): "))
    num_interactions_per_day = int(input("Enter the number of interactions per day: "))

    population = initialize_population(population_size)
    infected_count_list = []  
    deceased_count_list = [] 
    contagion_rate_list = [] 
    mortality_rate_list = []  

    initial_infected = int(population_size * (initial_infected_percentage / 100))
    random_infected_people = random.sample(range(1, population_size + 1), initial_infected)
    for person_id in random_infected_people:
        population[person_id]['infected'] = True

    for day in range(1, total_duration + 1):
        contagion_rate, mortality_rate = evolve_virus(day, contagion_rate, mortality_rate)
        contagion_rate_list.append(contagion_rate)
        mortality_rate_list.append(mortality_rate)
        
        population = spread_infection(population, contagion_rate, num_interactions_per_day, mortality_rate)
        
        infected_count = sum(1 for person in population.values() if person['infected'])
        infected_count_list.append(infected_count)

        deceased_count = sum(1 for person in population.values() if person['dead'])
        deceased_count_list.append(deceased_count)

    plt.figure(figsize=(10, 8))
    
    plt.subplot(3, 1, 1)
    plt.plot(range(1, total_duration + 1), infected_count_list, marker='o', linestyle='-', color='blue')
    plt.xlabel('Days')
    plt.ylabel('Infected Count')
    plt.title('Number of Infected Individuals Over Time')
    
    plt.subplot(3, 1, 2)
    plt.plot(range(1, total_duration + 1), deceased_count_list, marker='o', linestyle='-', color='red')
    plt.xlabel('Days')
    plt.ylabel('Deceased Count')
    plt.title('Number of Deceased Individuals Over Time')

    plt.subplot(3, 1, 3)
    plt.plot(range(1, total_duration + 1), contagion_rate_list, label='Contagion Rate', marker='o', linestyle='-')
    plt.plot(range(1, total_duration + 1), mortality_rate_list, label='Mortality Rate', marker='o', linestyle='-')
    plt.xlabel('Days')
    plt.ylabel('Rate')
    plt.title('Evolution of Contagion and Mortality Rates')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

simulate_disease()
