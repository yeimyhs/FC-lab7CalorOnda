import numpy as np
import matplotlib.pyplot as plt


def solve_wave_equation(f, g, a, b, v):
    # f es la condición inicial de la posición
    # g es la condición inicial de la velocidad
    # v es la velocidad de propagación de la onda
    # a es la longitud de la cuerda
    # b es el tiempo que se necesita para evaluar la onda

    h = k = 0.1
    # h es el tamaño de paso para el espacio
    # k es el tamaño de paso para el tiempo
    
    n = int(a / h + 1)
    m = int(b / k + 1)
    
    # r es el cálculo para la condición de estabilidad
    r = v * k / h
    r1 = r**2
    r2 = r**2 / 2
    s1 = 1 - r**2
    s2 = 2 * (1 - r**2)
    
    U = np.zeros((n, m))
    
    # Cálculo de las primeras dos filas
    for i in range(1, n - 1):
        U[i, 0] = f(h * (i - 1))
        U[i, 1] = s1 * f(h * (i - 1)) + k * g(h * (i - 1)) + r2 * (f(h * i) + f(h * (i - 2)))
    
    # Cálculo a partir de la tercera fila
    for j in range(1, m - 1):
        for i in range(1, n - 1):
            U[i, j + 1] = s2 * U[i, j] + r1 * (U[i - 1, j] + U[i + 1, j]) - U[i, j - 1]
    
    # Visualización de la solución en 3D
    X, Y = np.meshgrid(np.linspace(0, b, m), np.linspace(0, a, n))
    
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(X, Y, U, cmap='viridis')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Posición')
    ax.set_zlabel('Amplitud')
    ax.set_title('Ecuación de Onda')
    
    plt.show()


# Ejemplo
def initial_position(x):
    return np.sin(np.pi * x)

def initial_velocity(x):
    return 0.5 * np.sin(2 * np.pi * x)

solve_wave_equation(f=initial_position, g=initial_velocity, a=1, b=1, v=1)
