import random as rn

times_tested = 10**6
doors = 3
sum = 0
avg = sum

def simulate(n):
    remaining = set(i for i in range(n))
    car = rn.choice(list(remaining))
    chose = rn.choice(list(remaining))
    leave = {chose, car}

    if car == chose:
        leave = {chose, rn.choice(list(remaining - {chose} - {car}))}

    for i in range(n):
        if i in remaining - leave :
            remaining = remaining - {i}

    for r in remaining:
        if r != chose:
            chose = r
            break
    if chose == car:
        return 1
    return 0

for _ in range(times_tested):
    sum += simulate(doors)
avg = sum/times_tested
print(avg)
