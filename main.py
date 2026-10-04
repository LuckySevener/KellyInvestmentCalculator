import kelly_calculator



edge = 0.1
p = 0.25 * (1 + edge)
q = 1 - p
ratio = 4

k = kelly_calculator.calculator(p, ratio, q)
result = k.kelly_criterion()
print("The Kelly Criterion result is:", result) 