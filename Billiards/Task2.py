import numpy as np
import matplotlib.pyplot as plt


def next_position(x, y, momentum_x, momentum_y):
    next_x = x + momentum_x
    next_y = y + momentum_y - 0.5 * 10 * momentum_x**2
    return next_x, next_y


def next_momentum(x, y, momentum_x, momentum_y):
    momentum_norm = np.hypot(momentum_x, momentum_y)
    if momentum_norm > 0:
        momentum_x /= momentum_norm
        momentum_y /= momentum_norm

    new_momentum_x = (y**2 - x**2) * momentum_x - 2 * x * y * momentum_y
    new_momentum_y = -2 * x * y * momentum_x + (x**2 - y**2) * momentum_y

    return new_momentum_x, new_momentum_y



def simulate_billiard(reflections, deviation_threshold):
    trajectory_x, trajectory_y, reverse_trajectory_x, reverse_trajectory_y = [], [], [], []
    x, y, momentum_x, momentum_y = np.random.uniform(-1, 1, 4)

    for _ in range(reflections):
        trajectory_x.append(x)
        trajectory_y.append(y)
        reverse_trajectory_x.append(x)
        reverse_trajectory_y.append(y)
        x, y = next_position(x, y, momentum_x, momentum_y)
        momentum_x, momentum_y = next_momentum(x, y, momentum_x, momentum_y)

    momentum_x = -momentum_x
    momentum_y = -momentum_y

    for _ in range(reflections):
        reverse_trajectory_x.append(x)
        reverse_trajectory_y.append(y)
        x, y = next_position(x, y, momentum_x, momentum_y)
        momentum_x, momentum_y = next_momentum(x, y, momentum_x, momentum_y)

    deviation = max(
        np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        for x1, y1, x2, y2 in zip(trajectory_x, trajectory_y, reverse_trajectory_x, reverse_trajectory_y)
    )

    return deviation, trajectory_x, trajectory_y, reverse_trajectory_x, reverse_trajectory_y


def plot_billiard(trajectory_x, trajectory_y, reverse_trajectory_x, reverse_trajectory_y):
    plt.figure(figsize=(8, 8))
    plt.plot(trajectory_x, trajectory_y, color='blue', label='Regular Motion')
    plt.plot(reverse_trajectory_x, reverse_trajectory_y, color='red', label='Reversed Motion')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Vertical Circular Billiard')
    plt.legend()
    plt.grid(True)
    plt.show()


reflections = 5
deviation_threshold = 1e-1

deviation, trajectory_x, trajectory_y, reverse_trajectory_x, reverse_trajectory_y = simulate_billiard(
    reflections, deviation_threshold
)
print(f"The paths deviate after {reflections} reflections." if deviation > deviation_threshold else "The paths coincide.")
