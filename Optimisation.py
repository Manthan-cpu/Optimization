import pulp
#define problem
model=pulp.LpProblem("optimisation problem",pulp.LpMinimize)


#Desicion variables
x=pulp.LpVariable("x",lowBound=0,cat="Continuos")
y=pulp.LpVariable("y",lowBound=0,cat="Continuos")

#objective function
model+= 40*x+50*y

#constraints
model+= 2*x+3*y>=10
model+= 3*y-x==5

model.solve()
print("x=",x.value())
print("y=",y.value())
print("minimum value of objective function is",pulp.value(model.objective))