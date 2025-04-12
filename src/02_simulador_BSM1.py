import simpy
import random

def planta_tratamiento(env):
    while True:
        print(f"Inicia ciclo de tratamiento a las {env.now:.2f}h")
        tiempo_tratamiento = random.uniform(3.5, 4.5)
        yield env.timeout(tiempo_tratamiento)
        print(f"Fin de ciclo a las {env.now:.2f}h")

# Inicializar entorno
env = simpy.Environment()
env.process(planta_tratamiento(env))
env.run(until=24)
