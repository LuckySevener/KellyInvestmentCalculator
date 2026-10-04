import kelly_calculator



edge = 0.1
ratio = 4


p = (1 / ratio) * (1 + edge)
q = 1 - p

k = kelly_calculator.calculator(p, ratio, q)
result = k.kelly_criterion()
print("The Kelly Criterion result is:", result) 