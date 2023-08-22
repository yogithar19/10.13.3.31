import numpy as np

numbers = np.arange(1, 101)
np.random.shuffle(numbers)

# Counting the occurrences of numbers divisible by 100
divisible_by_7 = numbers[numbers % 7 == 0]
count = len(divisible_by_7)

# Total number of simulations
total_simulations = len(numbers)

# Probability calculation
probability = count / total_simulations

print(f"The probability of selecting a number divisible by 7 is {probability:.4f}")
print(f"The probability of selecting a number not divisible by 7 is {1-(probability):.4f}")
print(f"Simulation results (first 100 numbers): {numbers[:100]}")

