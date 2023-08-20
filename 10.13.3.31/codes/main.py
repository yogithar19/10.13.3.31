count_divisible_by_7 = 0

for number in range(1, 101):
    if number % 7 == 0:
        count_divisible_by_7 += 1

total_numbers = 100
probability = count_divisible_by_7 / total_numbers

print("Probability that chosen number divisible by 7=", probability)

print("Probablity that chosen number is not divisible by 7=", (1-probability))
