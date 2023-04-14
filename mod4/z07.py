points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

def calculate_distance(coordinates):
    global points
    para = []
    distance = 0
    if len(coordinates) <= 1:
        return distance
    else:
        for i, value in enumerate(coordinates, 1):
            if i == len(coordinates):
                break
            if coordinates[i-1] < coordinates[i]:
                kortej = (coordinates[i-1], (coordinates[i]),)
            else:
                kortej = (coordinates[i], (coordinates[i-1]),)
            para.append(kortej)
        #print(para)
        for key in para:
        #    print(f'{key} : {b_point}')
            distance += points.get(key)
        return distance

#calculate_distance([0, 1, 3, 2, 0])
print(calculate_distance([0, 1, 3, 2, 0]))
