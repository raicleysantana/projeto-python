import numpy as np
import math
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-10.0, 10.0, -5.0, 5.0)

def sin():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5, 0.5, 0.0)
    glPointSize(3.0)

    for x in np.arange(-10, 10, 0.01):
        glBegin(GL_POINTS)
        y = math.sin(x)
        glVertex2f(x, y)
        glEnd()

    glBegin(GL_LINES)
    glEnd()
    glFlush()

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("Exemplo em curvas")
    glutDisplayFunc(sin)
    init()
    glutMainLoop()