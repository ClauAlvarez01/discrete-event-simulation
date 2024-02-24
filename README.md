# Discrete Event Simulation
## Objetivo:

Aplicar los principios de simulación de eventos discretos para modelar y experimentar con ciertos fenómenos, y obtener resultados que nos ayuden a tomar decisiones informadas.



## Problema:

Un sistema necesita n máquinas funcionando para estar operativo. Para protegerse contra las averías de las máquinas, se mantienen máquinas adicionales disponibles como repuestos. Cuando una máquina se avería, es inmediatamente reemplazada por un repuesto y se envía a la instalación de reparación, que consta de un único reparador que repara las máquinas averiadas una a la vez. Una vez que una máquina averiada ha sido reparada, se vuelve a disponer como repuesto para ser utilizada cuando sea necesario.
Todos los tiempos de reparación son variables aleatorias independientes que tienen la función de distribución común G. Cada vez que una máquina se pone en uso, la cantidad de tiempo que funciona antes de averiarse es una variable aleatoria, independiente del pasado, que tiene la función de distribución F.
Se dice que el sistema falla cuando una máquina falla y no hay repuestos disponibles. Asumiendo que inicialmente hay n+s máquinas funcionales de las cuales n se ponen en uso y s se mantienen como repuestos, estamos interesados en simular este sistema para aproximar E[T], donde T es el tiempo en el que el sistema se estrella.

