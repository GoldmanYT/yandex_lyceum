from random import randint

score = 0
correct = True
while True:
    if correct:
        a, b = (randint(11, 99) for i in range(2))
    print(f'Очки: {score}')
    print(f'{a} * {b} = ?')
    try:
        c = int(input())
        if a * b == c:
            score += 10
            correct = True
        else:
            correct = False
    except ValueError:
        pass
