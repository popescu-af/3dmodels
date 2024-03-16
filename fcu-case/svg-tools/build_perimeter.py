import math
import random


# Calculate Manhattan distance between two points
def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


# Function to find the nearest unvisited point
def find_nearest_unvisited_point(current_point, unvisited_points):
    min_distance = math.inf
    nearest_point = None
    for point in unvisited_points:
        distance = manhattan_distance(current_point, point)
        if distance < min_distance:
            min_distance = distance
            nearest_point = point
    return nearest_point


# Function to scale the point
def scale(point, multiplier=4000, offset=200):
    return (int(point[0] * multiplier + offset), int(point[1] * multiplier + offset))


# Function to construct the path
def construct_path(coordinates, start_point):
    path = [start_point]
    unvisited_points = coordinates.copy()
    unvisited_points.remove(start_point)

    current_point = start_point
    while len(unvisited_points) > 0:
        nearest_point = find_nearest_unvisited_point(current_point, unvisited_points)
        path.append(nearest_point)
        unvisited_points.remove(nearest_point)
        current_point = nearest_point

    path.append(start_point)
    return path


def write_svg_file(width, height, path_string, filename):
    contents = f"""<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <polyline points="{path_string}" fill="none" stroke="black" stroke-width="1"/>
</svg>
"""
    with open(filename, "w") as file:
        file.write(contents)


files = [
    # "~/Desktop/front.txt",  # OK edited
    # "~/Desktop/back.txt",   # OK
    # "~/Desktop/left.txt",   # OK
    # "~/Desktop/right.txt",  # OK
    # "~/Desktop/top.txt",    # OK edited
    # "~/Desktop/bottom.txt", # OK edited
]


for f in files:
    with open(f, "r") as file:
        data = file.read()
        data = data.split("\n")
        coordinates = []

        minx, miny, maxx, maxy = math.inf, math.inf, -math.inf, -math.inf
        for line in data:
            if line:
                x, y = line.split(",")
                x = float(x)
                y = float(y)
                coordinates.append((x, y))
                minx = min(minx, x)
                miny = min(miny, y)
                maxx = max(maxx, x)
                maxy = max(maxy, y)

        centerx = (maxx - minx) / 2 * 1.1
        centery = (maxy - miny) / 2 * 1.1

        to_add_x = 5
        if minx < 0:
            to_add_x += abs(minx)

        to_add_y = 5
        if miny < 0:
            to_add_y += abs(miny)

        for i in range(len(coordinates)):
            x, y = coordinates[i]
            x = x + to_add_x
            y = y + to_add_y
            coordinates[i] = (x, y)

        start_point = random.choice(coordinates)
        path = construct_path(coordinates, start_point)
        result = ""
        for pt in path:
            result += f"{pt[0]},{pt[1]} "

        write_svg_file(centerx * 2, centery * 2, result, f + ".svg")
