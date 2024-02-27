import random
from distributions import exp
from heap import Heap


class RepairSystem():
    def __init__(self, n, s, lambd_F, lambd_G):
        self.n = n
        self.s = s
        self.t = 0
        self.t_star = float('inf') # Tiempo en la que la máquina actualmente en reparación estará operativa
        self.r = 0  # Número de máquinas que están fuera de servicio en un momento dado
        self.lambd_F = lambd_F
        self.lambd_G = lambd_G
        times_to_failure = exp(self.n, self.lambd_F)
        self.times_to_ordered_failure = Heap(times_to_failure)

    def generate_failure_time(self):
        return random.expovariate(self.lambd_F)

    def generate_repair_time(self):
        return random.expovariate(self.lambd_G)

    def simulate_system(self):
        while True:
            t1 = self.times_to_ordered_failure.first()
            try:
                if t1 < self.t_star:
                    self.t = t1
                    self.r = self.r+1  # Otra máquina ha fallado

                    if self.r == self.s+1:
                        return self.t

                    if self.r < self.s+1:
                        X = self.generate_failure_time()
                        self.times_to_ordered_failure.push(X + self.t)

                    if self.r == 1:
                        Y = self.generate_repair_time()
                        self.t_star = self.t + Y

                    self.times_to_ordered_failure.pop()

                else:
                    if self.t_star <= t1:
                        self.t = self.t_star
                        self.r = self.r-1

                        if self.r > 0:
                            Y = self.generate_repair_time()
                            self.t_star = self.t + Y

                        if self.r == 0:
                            self.t_star = float('inf')

            except Exception as e:
                print(f"Error: {e}")
                print(len(self.times_to_ordered_failure.heap))
                break


def run():
    # Ejemplo de uso
    n = 5
    s = 2
    lambda_F = 0.1
    lambda_G = 0.05
    k = 1000
    times = []
    count = 0
    for i in range(k):
        repair_system = RepairSystem(n, s, lambda_F, lambda_G)
        time = repair_system.simulate_system()
        times.append(time)
        count += 1
        if (count == 100):
            print(count)
            count = 0
    print(len(times))


run()
