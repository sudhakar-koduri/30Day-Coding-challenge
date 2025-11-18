from collections import defaultdict

def check_valid_rectangle(y1, y2, y1_set, y2_set, negative_list):
    filtered_set = {y for y in y1_set if y > y1 and y < y2}
    if len(filtered_set) > 0:
        return False
    filtered_set = {y for y in y2_set if y > y1 and y < y2}
    if len(filtered_set) > 0:
        return False
    # intermediate list check
    filtered_set = {y for y in negative_list if y >= y1 and y <= y2}
    if len(filtered_set) > 0:
        return False             
    return True

def max_rectangle_area(points):

    x_map = defaultdict(set)
    x_list = []
    for point in points:
        if point[0] not in x_list:
           x_list.append(point[0])
        x_map[point[0]].add(point[1])
    x_list.sort()

    max_area = -1
    for idx, x1 in enumerate(x_list):
      y1_set = x_map.get(x1) 
      negative_list = set()
      for x2 in x_list[idx+1:]:
        y2_set = x_map.get(x2)
        match_set = y1_set & y2_set
        
        if len(match_set) >= 2:
          check_list = list(match_set)
          check_list.sort()
          y1 = check_list[0]
          for y2 in check_list[1:]:
            if check_valid_rectangle(y1,y2, y1_set, y2_set, negative_list):
               max_area = max(max_area, (x2-x1) * (y2 - y1))
            y1 = y2   
        negative_list = negative_list.union(y2_set)       
    return max_area

print(max_rectangle_area([[1,2],[1,4],[1,8],[3,1],[3,2],[3,4],[5,2],[5,1],[5,4]]))

def inside_or_border_rectangle(x1, y1, x2, y2, px, py):
    return x1 <= px <= x2 and y1 <= py <= y2

def max_rectangle_area_sol(points):
    point_set = set(map(tuple, points))
    max_area = -1

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            if x1 == x2 or y1 == y2:
                continue

            if (x1, y2) in point_set and (x2, y1) in point_set:
                x_min, x_max = min(x1, x2), max(x1, x2)
                y_min, y_max = min(y1, y2), max(y1, y2)

                valid = True
                for px, py in points:
                    if (px, py) in [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]:
                        continue
                    elif inside_or_border_rectangle(x_min, y_min, x_max, y_max, px, py):
                        valid = False
                        break

                if valid:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    max_area = max(max_area, area)

    return max_area


def main():
    points_array = [
        [(1, 1), (1, 3), (3, 1), (3, 3), (2, 2)],
        [(1, 1), (1, 4), (4, 1), (4, 4)],
        [(0, 0), (2, 2), (2, 0), (0, 2)],
        [(0, 0), (0, 5), (5, 0), (5, 5)],
        [(1, 1), (2, 2), (2, 1), (1, 2), (3, 3)]
    ]