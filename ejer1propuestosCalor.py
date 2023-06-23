import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def solve_heat_equation(f, alfa, beta, a, b):
    # f = u(x, 0) es la condición inicial
    # alfa = u(0, t) y beta = u(a, t) son las condiciones en la frontera
    # a es el ancho del alambre
    # b es el tiempo de la simulación
    c = 1
    # c es el coeficiente de difusión

    h = 0.2
    k = 0.02
    # h es el tamaño de paso en el espacio
    # k es el tamaño de paso en el tiempo
    
    n = int(a / h + 1)
    m = int(b / k + 1)
    r = c**2 * k / h**2
    s = 1 - 2 * r
    
    U = np.zeros((n, m))
    
    # Condiciones en la frontera
    U[0, :] = alfa(np.linspace(0, b, m))
    U[n-1, :] = beta(np.linspace(0, b, m))
    
    # Condición inicial: primera fila de U
    U[1:n-1, 0] = f(np.linspace(h, (n-2)*h, n-2))
    
    # Cálculo a partir de la segunda columna
    for j in range(1, m):
        for i in range(1, n-1):
            U[i, j] = s * U[i, j-1] + r * (U[i-1, j-1] + U[i+1, j-1])
    
    # Visualización de la solución en 3D
    X, T = np.meshgrid(np.linspace(0, a, n), np.linspace(0, b, m))
    
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, U, cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('u(x,t)')
    ax.set_title('Ecuación de Calor')
    
    plt.show()


# Ejemplo
def initial_condition(x):
    return np.sin(np.pi * x / 2)

def boundary_condition1(t):
    return 0

def boundary_condition2(t):
    return 0

solve_heat_equation(f=initial_condition, alfa=boundary_condition1, beta=boundary_condition2, a=2, b=0.2)
