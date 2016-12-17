#Rasmi Lamichhane
#source pair-programming with Richard 


import numpy as np
def givens_rot(theta, v, x):
    G = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
    normalized_v = v / np.linalg.norm(v)
    u = np.array([0] + list(normalized_v))
    e = np.zeros_like(u)
    e[0] = 1
    U = np.array([e, u]).T
    return x + U.dot(G - np.eye(len(G))).dot(U.T).dot(x)

def givens_rot_matrix(theta, v, x):
    m, n = x.shape
    while len(v) != m - 1:
        v = np.array([0] + list(v))
    columns = []
    for i in range(n):
        column = x[:,i].copy()
        column = givens_rot(theta, v, column)
        columns.append(column)
    return np.array(columns).T

def calculate_angle(x):
    return np.arctan2(np.linalg.norm(x[1:]), x[0]) + np.pi

def qr_householder(A):
    m, n = A.shape
    R = A.copy()
    V = []
    for i in range(n):
        v = R[i:,i].copy()
        theta = calculate_angle(v)
        R[i:,i:] = givens_rot_matrix(theta, v[1:], R[i:,i:])
        V.append((theta, v[1:]))
    Q = np.eye(m, n)
    for i in range(n):
        Q[:,i] = givens_Q_times(V, Q[:,i])
    return Q, R

def givens_Q_times(V, x):
    y = x.copy()
    for i in reversed(range(len(V))):
        y[i:] = givens_rot(V[i][0], -V[i][1], y[i:])
    return y

m = 20
V = np.vander(np.linspace(-1,1,m), increasing=False)
def qr_test20(qr, V):
    Q, R = qr(V)
    m = len(Q.T)
    print(qr.__name__, np.linalg.norm(Q.dot(R) - V), np.linalg.norm(Q.T.dot(Q) - np.eye(m)))
    
qr_test20(qr_householder, V)
A=np.random.rand(2,2)

m = 10
V = np.vander(np.linspace(-1,1,m), increasing=False)
def qr_test10(qr, V):
    Q, R = qr(V)
    m = len(Q.T)
    print(qr.__name__, np.linalg.norm(Q.dot(R) - V), np.linalg.norm(Q.T.dot(Q) - np.eye(m)))
    
qr_test10(qr_householder, V)
A=np.random.rand(2,2)

#A = np.array([[1.0, 1.0,1.0], [2.0, 3.0, 4.0],[4.0, 5.2, 1.86]])
#print('--householder---')
#print(qr_householder(A)[2])
#print('--------')
#print(np.linalg.qr(A)[0])
#print('--------')
#print(qr_householder(A)[0])
