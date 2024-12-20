import random
import time
import matplotlib.pyplot as plt

# untuk generate array
def generate_array(n, max_value, seed):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

# check element unique
def is_unique(array):
    return len(array) == len(set(array))

# Function to measure execution time for uniqueness check
def measure_execution_time(array):
    start_time = time.perf_counter()
    is_unique(array)
    end_time = time.perf_counter()
    return end_time - start_time

# Constants for the experiment
stambuk_last_3_digits = 15  # NIM F55123015
max_value = 250 - stambuk_last_3_digits
n_values = [100, 150, 200, 250, 300, 350, 400, 500]
seed = 42

# Penyimpanan hasil
worst_case_times = []
average_case_times = []

# Run the experiments
for n in n_values:
    # Generate array and shuffle to simulate average and worst cases
    array = generate_array(n, max_value, seed)
    shuffled_array = array[:]
    random.shuffle(shuffled_array)

    # Measure average case time
    avg_case_time = measure_execution_time(array)
    average_case_times.append(avg_case_time)

    # Measure worst case time (already sorted array)
    sorted_array = sorted(array)
    worst_case_time = measure_execution_time(sorted_array)
    worst_case_times.append(worst_case_time)

# Save results to a text file
with open("worst_avg.txt", "w") as file:
    file.write("n_values,average_case_times,worst_case_times\n")
    for n, avg_time, worst_time in zip(n_values, average_case_times, worst_case_times):
        file.write(f"{n},{avg_time:.6f},{worst_time:.6f}\n")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(n_values, average_case_times, label="Average Case", marker="o")
plt.plot(n_values, worst_case_times, label="Worst Case", marker="s")
plt.xlabel("Array Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time Analysis for Uniqueness Check")
plt.legend()
plt.grid()
plt.savefig("execution_time_analysis.jpg")
plt.show()