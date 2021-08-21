import math
def normal(u,o,x):
    return ((math.pi*2)**0.5*o)**-1*math.e**-((x-u)**2/(2*o**2))

    
def calculate_probability(low, high):
    i, step, ans = low, 0.001, 0
    ans = 0
    while i < high:
        ans += (normal(20,2,i)*step)
        i += step
    return round(ans,3)

print(calculate_probability(0,19.5))
print(calculate_probability(20,22))