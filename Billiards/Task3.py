import random
import math
import numpy as np


def simulate_stadium_billiard(L):
    radius = 1
    xc_left = 0
    xc_right = L
 
    x = random.uniform(-radius, radius)
    y = random.uniform(-radius, radius)
    p_magnitude = 1
    theta = random.uniform(0, 2*math.pi)
    momentum_x = p_magnitude * math.cos(theta)
    momentum_y = p_magnitude * math.sin(theta)
    reflection_points = [(x, y)]

    while len(reflection_points) < reflections:
        if y < -radius:  
            intersection_x = x + (y + radius) * momentum_x / momentum_y
            intersection_y = -radius
            new_momentum_x = momentum_x
            new_momentum_y = -momentum_y

        elif y > radius:
            intersection_x = x + (y - radius) * momentum_x / momentum_y
            intersection_y = radius
            new_momentum_x = momentum_x
            new_momentum_y = -momentum_y

        elif x < xc_left: 
            intersection_x = -math.sqrt(radius**2 - y**2)
            intersection_y = y

            new_momentum_x = (intersection_y**2 - (intersection_x - xc_left)**2) * momentum_x - 2 * (intersection_x - xc_left) * intersection_y * momentum_y
            new_momentum_y = -2 * (intersection_x - xc_left) * intersection_y * momentum_x + ((intersection_x - xc_left)**2 - intersection_y**2) * momentum_y

        elif x > xc_right:  
            intersection_x = math.sqrt(radius**2 - y**2)
            intersection_y = y
            new_momentum_x = (intersection_y**2 - (intersection_x - xc_right)**2) * momentum_x - 2 * (intersection_x - xc_right) * intersection_y * momentum_y
            new_momentum_y = -2 * (intersection_x - xc_right) * intersection_y * momentum_x + ((intersection_x - xc_right)**2 - intersection_y**2) * momentum_y

        else:
            break
        
        reflection_points.append((intersection_x, intersection_y))
        x = intersection_x
        y = intersection_y
        momentum_x = new_momentum_x
        momentum_y = new_momentum_y

    return reflection_points


def test_stadium_billiard_generator(M, num_samples, L):
    radius = 1
    bins = [0] * M

    x_values = [random.uniform(0, 1) for _ in range(num_samples)]
    y_values = [random.uniform(0, 1) for _ in range(num_samples)]

    for x, y in zip(x_values, y_values):
        momentum_x = 1
        momentum_y = 0
        while True:
            if momentum_y < 0:
                intersection_x = x + radius * momentum_x / abs(momentum_y)
                bin_index = int(intersection_x * M)
                bins[bin_index] += 1
                break
            x += momentum_x
            y += momentum_y
            if abs(x) <= L and abs(y) <= radius:
                break
    return bins

reflections = 5
L_values = [1, 2]
M = 5
num_samples = 15

for L in L_values:
    reflection_points = simulate_stadium_billiard(L)
    print(f"Reflection points for L = {L}:")
    for i, point in enumerate(reflection_points):
        print(f"Reflection point {i+1}: {point}")

    bins = test_stadium_billiard_generator(M, num_samples, L)
    mean_entries = np.mean(bins)
    variance_entries = np.var(bins)

    print(f"\# of entries in each bin for L = {L}:")
    print(bins)
    print("entries Mean:", mean_entries)
    print("entries Variance :", variance_entries)
    print("--------------------")
