from Spring import Spring
from typing import List

class Body:
    def __init__(self, m: float, spring: Spring):
        self.m = m
        self.spring = spring

    def move(self, t: float, dt: float, x0: float, vo: float) -> List[float]:
        xs = [x0]
        x, v = x0, vo
        for _ in range(int(t / dt)):
            a = -self.spring.get_force(x) / self.m
            v, x = v + a * dt, x + v * dt
            xs.append(x)
        return xs
