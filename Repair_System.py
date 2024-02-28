import random
from heap import Heap
import numpy as np


def exp(n):
    # Partimos de una tasa de ocurrencia de eventos de 1 por unidad de tiempo
    u = np.random.rand(n)
    # Función de distribución acumulativa: F(x;λ)=1−e^(−λx), x≥0

    # Método de la inversa -> generar variables aleatorias uniformes U y
    # aplicar la inversa de la FDA para obtener las variables aleatorias exponenciales.
    exponential_variables = -np.log(1 - u)

    return exponential_variables


class RepairSystem():
    def __init__(self, n, s):
        self.n = n
        self.s = s
        self.t = 0
        # Tiempo en la que la máquina actualmente en reparación estará operativa
        self.t_star = float('inf')
        self.r = 0  # Número de máquinas que están fuera de servicio en un momento dado
        times_to_failure = exp(self.n)
        self.times_to_ordered_failure = Heap(times_to_failure)

    def generate_failure_time(self):
        return random.expovariate(1)

    def generate_repair_time(self):
        return random.expovariate(1)

    def simulate_system(self):
        while True:
            t1 = self.times_to_ordered_failure.first()
            if t1 < self.t_star:
                self.t = t1
                self.r = self.r+1

                if self.r == self.s+1:
                    return self.t

                if self.r < self.s+1:
                    X = self.generate_failure_time()
                    self.times_to_ordered_failure.push(X + self.t)

                if self.r == 1:
                    Y = self.generate_repair_time()
                    self.t_star = self.t + Y

                self.times_to_ordered_failure.pop()

            elif self.t_star <= t1:
                self.t = self.t_star
                self.r = self.r-1

                if self.r > 0:
                    Y = self.generate_repair_time()
                    self.t_star = self.t + Y

                if self.r == 0:
                    self.t_star = float('inf')
