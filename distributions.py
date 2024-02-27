import random
import numpy as np

def uniform(a, b):
    return random.uniform(a, b)

def exp(n, lambd):
    #Generar variables uniformes U
    u = np.random.rand(n)

    #Función de distribución acumulativa: F(x;λ)=1−e^(−λx), x≥0

    #Método de la inversa -> generar variables aleatorias uniformes U y 
    #aplicar la inversa de la FDA para obtener las variables aleatorias exponenciales.
    exponential_variables = -np.log(1 - u) / lambd

    return exponential_variables

