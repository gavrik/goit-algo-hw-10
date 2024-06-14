import pulp

# A - water
# B - sugar
# C - puree
# D - lemon

#A = 100
#B = 50
#C = 40
#D = 30

model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')
juice = pulp.LpVariable('juice', lowBound=0, cat='Integer')

#A = pulp.LpVariable('A', lowBound=0, upBound=100, cat='Integer')
#B = pulp.LpVariable('B', lowBound=0, upBound=50, cat='Integer')
#C = pulp.LpVariable('C', lowBound=0, upBound=40, cat='Integer')
#D = pulp.LpVariable('D', lowBound=0, upBound=30, cat='Integer')

model += lemonade + juice , "Profit"
model += 2 * lemonade + juice <= 100 
model += lemonade <= 50
model += lemonade <= 30
model += 2 * juice <= 40

model.solve()

print(model)

print(lemonade.varValue)
print(juice.varValue)


