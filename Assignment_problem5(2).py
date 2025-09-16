import pulp
model = pulp.LpProblem("Optimisation Problem", pulp.LpMinimize)

x1=pulp.LpVariable("x1",lowBound=0,cat="Continuos")
x2a=pulp.LpVariable("x2a",lowBound=0,cat="Continuos")#x2'
x3a=pulp.LpVariable("x3a",lowBound=0,cat="Continuos")#x3'
w=pulp.LpVariable("w",lowBound=0,cat="Continuos")


model+= (-2)*x1+ 3*x2a  - 2*x3a + 1*w ,"Objective Function"
model+= 4*x1 - x2a  - 5*x3a + 5*w == 10, "Constraint 1"
model+= 2*x1 + 3*x2a  + 2*x3a - 3*w == 12, "Constraint 2"

model.solve()
print("x1=",x1.value())
print("x2=",x2a.value()-w.value())
print("x3=",x3a.value()-w.value())
print("minimum value of objective function in case 2 is",pulp.value(model.objective))