from os import lseek
from geometrics import bassis_manifold, wavy_manifold
from svg_const import header,tail
import util
import math
import time


loop = True
origin = {"x": 100, "y": 100}

frames = 100

for i in range(frames):
    frame_phase = 2*math.pi/frames * i

    appality = []
    appality.append(wavy_manifold(frame_phase))
    appality = util.flat(appality)
    appality = util.transmult_whole(appality, [100.0,100.0], 20)

    appality1 = []
    appality1.append(wavy_manifold(-frame_phase))
    appality1 = util.flat(appality1)
    appality1 = util.transmult_whole(appality1, [100.0,200.0], 20)

    appality.extend(appality1)
    svg = []
    svg.append(header())
    svg.append(util.data_2_path(appality, loop))
    svg.append(tail())

    result_svg = "".join(svg);

    with open('result.svg', 'w') as file:
        file.write(result_svg)

    print(f"frame {i} generated")
    time.sleep(0.5)

# fractal_len = util.calculate_path_length(fractal_points)
# print(f'Fractal lines total length {fractal_len}')

