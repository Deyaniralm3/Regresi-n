import numpy as np

def read_input (text_basis):
    a_temp, b_temp =text_basis.strip().split('=')
    b_temp=eval(b_temp.strip(' '))
    a_temp=a_temp[:-1]
    a_temp=[eval(i) for i in a_temp.split()]
    return a_temp,b_temp

def read_file(ruta):
    A=[]
    b=[]
    with open (ruta, 'r') as f:
        flag=0
        for line in f:
            if line.strip()!='X':
                pass
            else:
                flag=1
                continue
            if line == 'Y':
                break
            if flag==1:
                aux_1, aux_2=read_input(line)
                A.append(aux_1)
                b.append(aux_2)
    return A,b

ruta1='C:/Users/Iraide/Documents/sistema.txt'
            
print ("A=",read_file(ruta1)[0])  
print ("b=",read_file(ruta1)[1])  

def gauss_seidel_conlect(ruta,tam, umbral, max_iter):
    A=read_file(ruta)[0]
    b=read_file(ruta)[1]
    m=len(A[0])
    n=len(A)
    if m==n:
        x = [0.0 for i in range(tam)]
        aux = [1.0 for i in range(tam)]
        for ite in range(max_iter):
            for h in range(tam):
                aux[h] = 0.0  
                x[h] = (b[h]-sum([i*j*k for i,j,k in zip(aux,x,A[h])]))/A[h][h]
                aux[h] = 1.0
            current_differences = [b[h] - sum([i*j for i,j in zip(x,A[h])]) for h in range(tam)]
            error = sum([abs(i) for i in current_differences])
            
            if error < umbral:
                return x
                break
    else:
        return ("La matriz no es cuadrada, no puedo encontrar solución")

            
        
def gauss_seidelnumphy_conlect(ruta, tam, umbral, max_iter):
    A=read_file(ruta)[0]
    b=read_file(ruta)[1]
    m=len(A[0])
    n=len(A)
    if m==n:
        A_np = np.array(A)
        b_np = np.array(b)
        x_np = np.zeros(tam) 
        aux_np = np.ones(tam)
        for ite in range(max_iter):
            for i in range(tam):
                aux_np[i] = 0.0
                x_np[i] = (b_np[i] - np.sum(x_np*aux_np*A_np[i,:]))/A_np[i][i]
                aux_np[i] = 1.0
            
            current_b = np.dot(A_np,x_np)
            error = np.sum(np.abs(current_b-b_np))
            
            if error < umbral:
                return x_np
                break
    else:
        return ("La matriz no es cuadrada, no puedo encontrar solución") 