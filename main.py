def cat_and_mouse(map_str, moves):
    map_lines = map_str.strip().split('\n')
    
    cat_position = None
    mouse_position = None
    for i, line in enumerate(map_lines):
        for j, char in enumerate(line):
            if char == 'C':
                cat_position = (i, j)
            elif char == 'm':
                mouse_position = (i, j)
    if not cat_position or not mouse_position:
        return "boring without two animals"
    distance = abs(cat_position[0] - mouse_position[0]) + abs(cat_position[1] - mouse_position[1])
    if distance <= moves:
        return "Caught!"
    else:
        return "Escaped!"
map1 = """
..C......
.........
....m....
"""

print(cat_and_mouse(map1, 5)) 
