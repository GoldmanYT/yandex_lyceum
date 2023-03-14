def is_under_queen_attack(position, queen_position):
    let = 'abcdefgh'
    num = '12345678'
    if type(position) != str:
        raise TypeError()
    if len(position) != 2 or position[0] not in let or position[1] not in num:
        raise ValueError()
    if type(queen_position) != str:
        raise TypeError()
    if len(queen_position) != 2 or queen_position[0] not in let or queen_position[1] not in num:
        raise ValueError()
    if position == queen_position:
        return True
    if position[0] == queen_position[0]:
        return True
    if position[1] == queen_position[1]:
        return True
    x1, y1 = let.find(position[0]), num.find(position[1])
    x2, y2 = let.find(queen_position[0]), num.find(queen_position[1])
    if abs(x1 - x2) == abs(y1 - y2):
        return True
    return False
