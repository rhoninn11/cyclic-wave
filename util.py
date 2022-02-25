import math

# all in svg context


def svg_path(points, xy, loop=False):
    d = []
    x = xy[0];
    y = xy[1];
    
    for point in points:
        if(len(d) == 0):
            d.append(f'M {point[x]} {point[y]} ')
        else:
            d.append(f'L {point[x]} {point[y]} ')

    if loop:
        d.append("Z ")

    dtxt = "".join(d)
    return dtxt

def generatePathDescription(points_w_md):
# transform
    points = []
    for point_w_md in points_w_md:
        points.append(point_w_md["point"])

    loop = True
    return svg_path(points, ["x", "y"], loop)

def pointsToD(data_list):
    d = []

    loop = True
    for point_list in data_list:
        d.append(svg_path(point_list, ["x", "y"], loop))

    
    return "".join(d)

def data2D(data_list, loop = False):
    d = []

    for point_list in data_list:
        d.append(svg_path(point_list, [0,1], loop))

    
    return "".join(d)

def md_points_2_path(points_w_md):
    path_value = "<path\n"
    path_value = path_value + "style=\"fill:none;stroke:#000000;stroke-width:0.033mm;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1\"\n"
    path_value = path_value + "d=\"" + generatePathDescription(points_w_md) + "\" />\n"

    return path_value

def path_svg(path_decription):
    path_value = "<path\n"
    path_value = path_value + "style=\"fill:none;stroke:#000000;stroke-width:0.033mm;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1\"\n"
    path_value = path_value + "d=\"" + path_decription + "\" />\n"

    return path_value

def points_2_path(points):
    path_value = "<path\n"
    path_value = path_value + "style=\"fill:none;stroke:#000000;stroke-width:0.033mm;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1\"\n"
    path_value = path_value + "d=\"" + pointsToD(points) + "\" />\n"

    return path_value

def data_2_path(points, loop = False):
    path_value = "<path\n"
    path_value = path_value + "style=\"fill:none;stroke:#000000;stroke-width:0.033mm;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1\"\n"
    path_value = path_value + "d=\"" + data2D(points, loop) + "\" />\n"

    return path_value

def isParseLevel(data_list):
    list_probe_top = data_list
    isNotEmptyList_top = isinstance(list_probe_top, list)
    list_probe_inner = data_list[0] 
    isNotEmptyList_inner = isinstance(list_probe_inner, list)

    goDeaper = False
    if isNotEmptyList_top and isNotEmptyList_inner:
        isInnerListIsNumerical = not isinstance(list_probe_inner[0], list)
        # lista wewnętrzna jest listą współżędnych, lista zewnętrzn jest grupą
        goDeaper = isInnerListIsNumerical

    return not goDeaper




def transmult(data, tanslat, mult):
    r = []
    xy = [0,1]
    for point in data:
        r1 = []
        for dir in xy:
            r2 = mult*point[dir] + tanslat[dir]
            r1.append(r2)
        r.append(r1)
    
    return r;

def transmult_whole(data,translat, mult):

    r = []
    for element in data:
        r.append(transmult(element, translat, mult))

    return r;


def flat(data_list):
    r = []

    if isParseLevel(data_list):
        for branch in data_list:
            r1 = flat(branch)
            r.extend(r1)
        return r

    point_list = data_list
    return [point_list]
    for cord_list in point_list:
        r.append(cord2point(cord_list))

    return [r]    

def cord2point(cords):
    return {"x": cords[1], "y": cords[0]}

def calc_point_dist(p1,p2):
    xd = p1["x"] - p2["x"]
    yd = p1["y"] - p2["y"]

    if xd == 0:
        return abs(yd)

    if yd == 0:
        return abs(xd)

    return math.sqrt(xd*xd + yd*yd)

def calculate_path_length(points):
    
    total_d = 0
    for index in range(len(points) - 1):
        p1 = points[index]
        p2 = points[index + 1]
        total_d += calc_point_dist(p1,p2)
    
    return total_d

