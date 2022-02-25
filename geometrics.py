
import math
import util

def calculate_bassis():
    whole = 2*math.pi
    dim = whole/3
    start = 0
    
    ref_bassis = [
        [ math.sin(dim+start), math.cos(dim+start) ],
        [ math.sin(2*dim+start), math.cos(2*dim+start) ],
        [ math.sin(3*dim+start), math.cos(3*dim+start) ]
    ]

    bassis = [
        [ref_bassis[0][0], -ref_bassis[0][1]],
        [ref_bassis[1][0], -ref_bassis[1][1]],
        [ref_bassis[2][0], -ref_bassis[2][1]],
    ]

    return bassis;
    
def bassis_manifold():
    bassis = calculate_bassis()

    center = [0.0, 0.0]

    drogowskaz = [[center, bassis[0]], [center, bassis[1]], [center, bassis[2]]]
    return drogowskaz

def wavy_manifold(phase_offset = 0.0):

    bassis = calculate_bassis()

    segments = 100;

    cycle = 2*math.pi
    f_cycle = cycle*3

    delta1 = cycle/segments
    delta2 = f_cycle/segments

    rounds = []

    for i in range(27):

        round = []
        size = 0.1 + i*0.1
        start = 2*math.pi*0.0 + i*0.1 + phase_offset;
        for seg in range(segments):
            elo = util.transmult([bassis[0]], [0.0, 0.0], math.cos(start + seg*delta1)*size)
            elo1 = util.transmult([bassis[1]], [0.0, 0.0], -math.sin(start + seg*delta1)*size)
            elo2 = util.transmult([bassis[2]], [0.0, 0.0], math.cos(seg*delta2)*size*0.5)
            elo3 = util.transmult(elo, elo1[0], 1)
            round.extend(util.transmult(elo3, elo2[0], 1));

        rounds.append(round)

    return rounds
