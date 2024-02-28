import statistics
import math
from Repair_System import RepairSystem
import random


def recursive_mean_variance(X, j, current_mean, current_variance):
    new_mean = current_mean + (X - current_mean)/(j)
    new_variance = ((1 - 1/(j-1)) * current_variance) + \
        (j * (new_mean - current_mean)**2)
    return new_mean, new_variance


def run_simulation(n, s, acceptability_threshold, min_iterations=100):
    iterations = min_iterations
    failure_time = []

    for _ in range(iterations):
        system_simulator = RepairSystem(n, s)
        result = system_simulator.simulate_system()
        failure_time.append(result)

    current_mean = statistics.mean(failure_time)
    current_variance = statistics.variance(failure_time)
    current_stdev = statistics.stdev(failure_time)

    x = current_stdev / math.sqrt(iterations)

    while x > acceptability_threshold:
        iterations += 1
        system_simulator = RepairSystem(n, s)
        result = system_simulator.simulate_system()
        failure_time.append(result)
        current_mean, current_variance = recursive_mean_variance(
            result, iterations, current_mean, current_stdev)
        current_stdev = math.sqrt(current_variance)
        x = current_stdev / math.sqrt(iterations)

    return iterations, current_mean, current_stdev


def save_logs(i, n, s, mean, stdev, log_file='results.txt'):
    with open(log_file, 'a') as f:
        print(f'n: {n}, s: {s}, Numero de iteraciones: {i}, Tiempo estimado de falla: {mean}, Desviacion estandar de los tiempos de falla: {stdev}', file=f)


for i in range(1000):
    n = int(random.uniform(1, 1000))
    s = int(random.uniform(1, 1000))
    acceptability_threshold = 0.02
    iterations, mean, stdev = run_simulation(n, s, acceptability_threshold)
    save_logs(iterations, n, s, mean, stdev)
