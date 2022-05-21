import numpy as np
import matplotlib.pyplot as plt

'''
bueno ya luego a seguir y listo'''


gravedad = {'Mercurio': 2.8,
            'Venus': 8.9,
            'Tierra': 9.8,
            'Marte': 3.7,
            'Jupiter': 22.9,
            'Saturno': 9.1,
            'Urano': 7.8,
            'Neptuno': 11.0,
            'Luna': 1.6
            }

def tiempo_total(p, h):
    g = gravedad[p]
    vf = np.sqrt(2*g*h)
    tf = vf/g
    return tf

def velocidad(p, t):
    g = gravedad[p]
    vel = g*t
    return vel


def altura(p, t):
    g = gravedad[p]
    h = 1/2*g*(t**2)
    return h


def comparar(p1,p2,h,m):
    tf1 = tiempo_total(p1,h)
    vf1 = velocidad(p1,h)
    tf2 = tiempo_total(p2,h)
    vf2 = velocidad(p2,h)
    if m > tf1 or m > tf2:
        print("Tiempo no valido")
        return ()
    vPoint1 = m*vf1/tf1
    vpoint2 = m*vf2/tf2
    plt.subplot(1, 2, 1)
    ax = plt.gca()
    plt.plot([0, tf1], [0, vf1])
    plt.scatter([tf1], [vf1])
    plt.plot([tf1, tf1], [0, vf1], linestyle='dotted')
    plt.plot([0, tf1], [vf1, vf1], linestyle='dotted')
    plt.scatter([m], [vPoint1])
    plt.plot([m, m], [0, vPoint1], linestyle='dotted')
    plt.plot([0, m], [vPoint1, vPoint1], linestyle='dotted')
    plt.title(p1)
    plt.grid(axis='y', color='gray')
    plt.grid(axis='x', color='gray')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xlabel('TIEMPO (S)')
    plt.ylabel('VELOCIDAD (M/S)')
    plt.legend()

    plt.subplot(1, 2, 2)
    ax = plt.gca()
    plt.plot([0, tf2], [0, vf2])
    plt.scatter([tf2], [vf2])
    plt.plot([tf2, tf2], [0, vf2], linestyle='dotted')
    plt.plot([0, tf2], [vf2, vf2], linestyle='dotted')
    plt.scatter([m], [vpoint2])
    plt.plot([m, m], [0, vpoint2], linestyle='dotted')
    plt.plot([0, m], [vpoint2, vpoint2], linestyle='dotted')
    plt.title(p2)
    plt.suptitle("Velocidad vs tiempo")

    plt.grid(axis='y', color='gray')
    plt.grid(axis='x', color='gray')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xlabel('TIEMPO (S)')
    plt.ylabel('VELOCIDAD (M/S)')
    plt.legend()
    plt.show()


comparar('Mercurio','Saturno',40,2)
