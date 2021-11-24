def calculate_distance(coords, area_boundary):
    return ((coords[0] - area_boundary[0]) ** 2 + (coords[1] - area_boundary[1]) ** 2) ** (1 / 2)