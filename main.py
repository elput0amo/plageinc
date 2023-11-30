import random
import matplotlib.pyplot as plt

# Function to initialize the population
def initialize_population(population_size):
    population = {}
    for person_id in range(1, population_size + 1):
        # Each person starts uninfected with no time infected and alive
        population[person_id] = {'infected': False, 'time_infected': 0, 'dead': False}
    return population

# Function to simulate the spread of infection within the population
def spread_infection(population, contagion_rate, num_interactions_per_day, mortality_rate):
    for person_id, attributes in population.items():
        # Check if the person is infected or dead
        if not attributes['infected'] or attributes['dead']:
            continue
        # Simulate interactions to spread infection
        for interaction in range(num_interactions_per_day):
            if random.random() < contagion_rate:
                # Randomly select a person to infect
                random_person = random.choice(list(population.keys()))
                if not population[random_person]['infected'] and not population[random_person]['dead']:
                    # Infect the selected person
                    population[random_person]['infected'] = True
                    # Simulate mortality based on mortality rate
                    if random.random() < mortality_rate:
                        population[random_person]['dead'] = True
    return population

# Function to modify virus evolution parameters over time
def evolve_virus(day, contagion_rate, mortality_rate):
    if day % 10 == 0:
        # Increase contagion rate by 20% every 10 days
        contagion_rate *= 1.2
        # Increase mortality rate by 10% every 10 days
        mortality_rate *= 1.1
    return contagion_rate, mortality_rate

# Function to simulate the disease spread within the population
def simulate_disease():
    # Input parameters from the user
    population_size = int(input("Enter the total population size: "))
    total_duration = int(input("Enter the total duration of simulation (days): "))
    initial_infected_percentage = float(input("Enter the initial percentage of infected individuals (0-100): "))
    contagion_rate = float(input("Enter the initial contagion rate (0-1): "))
    mortality_rate = float(input("Enter the initial mortality rate (0-1): "))
    num_interactions_per_day = int(input("Enter the number of interactions per day: "))

    # Initialize lists to track data for plotting
    population = initialize_population(population_size)
    infected_count_list = []  
    deceased_count_list = [] 
    contagion_rate_list = [] 
    mortality_rate_list = []  

    # Infect initial percentage of the population
    initial_infected = int(population_size * (initial_infected_percentage / 100))
    random_infected_people = random.sample(range(1, population_size + 1), initial_infected)
    for person_id in random_infected_people:
        population[person_id]['infected'] = True

    # Run simulation for each day
    for day in range(1, total_duration + 1):
        # Modify contagion and mortality rates over time
        contagion_rate, mortality_rate = evolve_virus(day, contagion_rate, mortality_rate)
        contagion_rate_list.append(contagion_rate)
        mortality_rate_list.append(mortality_rate)
        
        # Simulate spread of infection and mortality
        population = spread_infection(population, contagion_rate, num_interactions_per_day, mortality_rate)
        
        # Calculate and store infected count for each day
        infected_count = sum(1 for person in population.values() if person['infected'])
        infected_count_list.append(infected_count)

        # Calculate and store deceased count for each day
        deceased_count = sum(1 for person in population.values() if person['dead'])
        deceased_count_list.append(deceased_count)

    # Plotting the results
    plt.figure(figsize=(10, 8))
    
    # Plot for infected count
    plt.subplot(3, 1, 1)
    plt.plot(range(1, total_duration + 1), infected_count_list, marker='o', linestyle='-', color='blue')
    plt.xlabel('Days')
    plt.ylabel('Infected Count')
    plt.title('Number of Infected Individuals Over Time')
    
    # Plot for deceased count
    plt.subplot(3, 1, 2)
    plt.plot(range(1, total_duration + 1), deceased_count_list, marker='o', linestyle='-', color='red')
    plt.xlabel('Days')
    plt.ylabel('Deceased Count')
    plt.title('Number of Deceased Individuals Over Time')

    # Plot for contagion and mortality rates
    plt.subplot(3, 1, 3)
    plt.plot(range(1, total_duration + 1), contagion_rate_list, label='Contagion Rate', marker='o', linestyle='-')
    plt.plot(range(1, total_duration + 1), mortality_rate_list, label='Mortality Rate', marker='o', linestyle='-')
    plt.xlabel('Days')
    plt.ylabel('Rate')
    plt.title('Evolution of Contagion and Mortality Rates')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Run the simulation
simulate_disease()
