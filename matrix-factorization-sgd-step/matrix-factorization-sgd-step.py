def matrix_factorization_sgd_step(U, V, r, lr, reg):
    pred = sum(u * v for u, v in zip(U, V))
    e = r - pred
    
    U_old = U[:]
    V_old = V[:]
    
    U_new = []
    V_new = []
    
    for i in range(len(U)):
        u_i = U_old[i]
        v_i = V_old[i]
        
        u_new = u_i + lr * (e * v_i - reg * u_i)
        v_new = v_i + lr * (e * u_i - reg * v_i)
        
        U_new.append(float(u_new))
        V_new.append(float(v_new))
    
    return U_new, V_new