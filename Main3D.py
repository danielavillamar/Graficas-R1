# Daniela Villamar 19086
# Graficas por computadora
# Julio 2023

from gl import Renderer, V2, V3, color
import shaders
import random

width = 1920
height = 1920

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel(
    "Doguinho.obj",
    translate=((width / 2), 0, 0),
    scale=(200, 200, 200),
    rotate = (0, 0, 0)
)

rend.glRender()

rend.glFinish("output.bmp")
