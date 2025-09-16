import pulp
model = pulp.LpProblem("Optimisation Problem", pulp.LpMinimize)

x1=pulp.LpVariable("x1",lowBound=0,cat="Continuos")
x2p=pulp.LpVariable("x2p",lowBound=0,cat="Continuos")#x2plus
x2m=pulp.LpVariable("x2m",lowBound=0,cat="Continuos")#x2minus
x3p=pulp.LpVariable("x3p",lowBound=0,cat="Continuos")
x3m=pulp.LpVariable("x3m",lowBound=0,cat="Continuos")

model+= (-2)*x1+ 3*x2p - 3*x2m - 2*x3p + 2*x3m ,"Objective Function"
model+= 4*x1 - x2p + x2m - 5*x3p + 5*x3m == 10, "Constraint 1"
model+= 2*x1 + 3*x2p - 3*x2m + 2*x3p - 2*x3m == 12, "Constraint 2"

model.solve()
print("x1=",x1.value())
print("x2=",x2p.value()-x2m.value())
print("x3=",x3p.value()-x3m.value())
print("minimum value of objective function in case 1 is",pulp.value(model.objective))