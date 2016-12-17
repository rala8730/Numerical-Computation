import matplotlib.pyplot as plt
import numpy
#%matplotlib inline

def rk4_systems(f1, f2, f3, f4, a, b, N, alpha1, alpha2, alpha3, alpha4):
    data = []
    h = (b - a) / N
    t = a
    w1 = alpha1
    w2 = alpha2
    w3 = alpha3
    w4 = alpha4
    #print('%.1f & %.8f & %.8f \\\\ \\hline' % (t, w1, w2))
    data.append((t, w1, w2, w3, w4))
    for i in range(1, N + 1):
        K11 = h * f1(t, w1, w2, w3, w4)
        K12 = h * f2(t, w1, w2, w3, w4)
        K13 = h * f3(t, w1, w2, w3, w4)
        K14 = h * f4(t, w1, w2, w3, w4)
        
        c= t + h / 2
        d= w1 + K11 / 2
        e=w2 + K12 / 2
        f=w3 + K13 / 2
        g=w4 + K14 / 2
        
        K21 = h * f1(c,d,e,f,g)
        K22 = h * f2(d,d,e,f,g)
        K23 = h * f3(c,d,e,f,g)
        K24 = h * f4(c,d,e,f,g)
        
        k=w1 + K21 / 2
        l=w2 + K22 / 2
        m=w3 + K23 / 2
        n=w4 + K24 / 2
        
        K31 = h * f1(c, k, l, m, n)
        K32 = h * f2(c, k, l, m, n)
        K33 = h * f3(c, k, l, m, n)
        K34 = h * f4(c, k, l, m, n)
        
        o=t + h
        p=w1 + K31
        q=w2 + K32
        r=w3 + K33
        s=w4 + K34
        
        K41 = h * f1(o, p, q, r, s)
        K42 = h * f2(o, p, q, r, s)
        K43 = h * f3(o, p, q, r, s)
        K44 = h * f4(o, p, q, r, s)
        
        w1 += (K11 + 2 * K21 + 2 * K31 + K41) / 6
        w2 += (K12 + 2 * K22 + 2 * K32 + K42) / 6
        w3 += (K13 + 2 * K23 + 2 * K33 + K43) / 6
        w4 += (K14 + 2 * K24 + 2 * K34 + K44) / 6
        
        t = a + i * h
        #print('%.1f & %.8f & %.8f \\\\ \\hline' % (t, w1, w2))
        data.append((t, w1, w2, w3, w4))
    return data

def f1(x, y1, y2, y3, y4):
    return y3

def f2(x, y1, y2, y3, y4):
    return y4

def f3(x, y1, y2, y3, y4):
    #return 0
    force= - numpy.pi / 2 * numpy.sqrt(y3 **2 + y4 ** 2) * 0.2 * 0.05**2
    return (1/8)*force

def f4(x, y1, y2, y3, y4):
    force= - numpy.pi / 2 * numpy.sqrt(y3 **2 + y4 ** 2) * 0.2 * 0.05**2
    return (1/8)* force - 9.8
#return -9.8

theta = 28.59
pos = rk4_systems(f1, f2, f3, f4, 0, 30, 100000, 0, 0, 300*numpy.cos(numpy.deg2rad(theta)), 300 *numpy.sin(numpy.deg2rad(theta)))
#print(anh)
#print(len(anh))
xs = []
ys = []
for tup in pos:
    xs.append(tup[1]) # is x position
    ys.append(tup[2])#y position

for tup in pos:
    if(tup[1] > 3000):
        print('theta:',theta,'time: {:.3} second'.format((tup[0])))
        break



plt.plot(xs, ys)
plt.plot(3000, 1000, 'r*') #plotting the * in the destination
plt.xlim((0, 3500)) #setting the limit of x
plt.ylim((0, 1300))#setting the limit of y

