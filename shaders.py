def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]

    vt = [vertex[0], vertex[1], vertex[2], 1]

    vt = modelMatrix @ vt

    vt = [vt[0, 0], vt[0, 1], vt[0, 2], vt[0, 3]]

    vt = [vt[0] / vt[3], vt[1] / vt[3], vt[2] / vt[3]]

    return vt


def fragmentShader(**kwargs):
    # Color white
    color = (1, 1, 1)
    return color
