import numpy as np

def simplex_eq(c, A, b):
  
    m, n = A.shape

    # Phase I: add artificial variables
    A_phase1 = np.hstack([A, np.eye(m)])
    c_phase1 = np.hstack([np.zeros(n), np.ones(m)])

    tableau = np.zeros((m+1, n+m+1))
    tableau[:m, :n+m] = A_phase1
    tableau[:m, -1] = b
    tableau[-1, :n+m] = c_phase1

    # Make initial basis feasible
    basis = list(range(n, n+m))

    # Phase I simplex
    def pivot(tableau, row, col):
        tableau[row, :] /= tableau[row, col]
        for i in range(tableau.shape[0]):
            if i != row:
                tableau[i, :] -= tableau[i, col] * tableau[row, :]

    while True:
        col = np.argmin(tableau[-1, :-1])
        if tableau[-1, col] >= -1e-12:
            break
        ratios = [tableau[i, -1] / tableau[i, col] if tableau[i, col] > 1e-12 else np.inf
                  for i in range(m)]
        row = np.argmin(ratios)
        if ratios[row] == np.inf:
            raise ValueError("Infeasible LP")
        pivot(tableau, row, col)
        basis[row] = col

    # Check feasibility
    if abs(tableau[-1, -1]) > 1e-8:
        raise ValueError("Infeasible LP")

    # Phase II: drop artificial variables
    tableau = tableau[:, :n+1]
    tableau[-1, :] = 0
    tableau[-1, :n] = -c

    # Fix objective row 
    for i, bi in enumerate(basis):
        if bi < n:
            tableau[-1, :] += c[bi] * tableau[i, :]

    # Phase II simplex
    while True:
        col = np.argmin(tableau[-1, :-1])
        if tableau[-1, col] >= -1e-12:
            break
        ratios = [tableau[i, -1] / tableau[i, col] if tableau[i, col] > 1e-12 else np.inf
                  for i in range(m)]
        row = np.argmin(ratios)
        if ratios[row] == np.inf:
            raise ValueError("Unbounded LP")
        pivot(tableau, row, col)
        basis[row] = col

   
    x = np.zeros(n)
    for i, bi in enumerate(basis):
        if bi < n:
            x[bi] = tableau[i, -1]
    z = tableau[-1, -1]
    return x, z



if __name__ == "__main__":
    c = np.array([3, 2])
    A = np.array([[1, 1],
                  [2, 0]])
    b = np.array([4, 2])

    x, z = simplex_eq(c, A, b)
    print("Optimal x:", x)
    print("Optimal z:", z)
