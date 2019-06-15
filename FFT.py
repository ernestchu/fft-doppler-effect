import numpy as np
import matplotlib.pyplot as plt
def fft(vector, inverse = False):
    n = len(vector)
    if n == 0:
        return np.array([], dtype = np.complex_)
    elif n & (n-1) == 0:
        return fft_radix2(vector, inverse)
    else:
        return fft_radix2(make_radix2(vector), inverse)

def fft_radix2(vector, inverse = False):
    #bit-reversed permutation
    def reverse(x, bits):
        y = 0
        for i in range(bits):
            y = (y << 1) | (x & 1)
            x >>= 1
        return y
    #setup
    n = len(vector)
    #level = log2(n)
    levels = n.bit_length()-1
    if 2**levels != n:
        raise ValueError('Length is not  a power of 2')
    coef = (1j if inverse else -1j)*2*np.pi/n
    W = [np.exp(i*coef) for i in range(n//2)]
    vector = [vector[reverse(i, levels)] for i in range(n)]
    #algorithm for dit fft
    size = 2
    while size <= n:
        halfsize = size//2
        Wstep = n//size #make n in W(k,n) be len(vector)
        for i in range(0, n, size):
            #computing each column of butterfly diagram
            k=0
            for j in range(i, i+halfsize):
                #computing each butterfly
                temp = vector[j+halfsize] * W[k] #store (j+1)W instead of j to reduce complexity
                #-------THE---------
                vector[j+halfsize] = vector[j] - temp
                vector[j] = vector[j] + temp
                #-----FORMULA-------
                k += Wstep
        size *= 2
    if inverse:
        for i in range(len(vector)):
            vector[i]/=len(vector)
    return np.array(vector, dtype=np.complex_)

def make_radix2(vector):
    n=2
    while len(vector) > n:
        n*=2
    appendArr = [0]*(n-len(vector))
    return list(vector)+appendArr

#test
'''
x=[0,1,2,3,4,5,6,7]
X=fft(x)
print(X)
plt.subplot(221)
plt.plot(range(len(x)), x)
plt.title('Original data')

plt.subplot(222)
plt.plot(range(len(X)), X)
plt.title('FFT')

x=fft(X, True)
print(x.real)

plt.subplot(223)
plt.plot(range(len(x)), x)
plt.title('Transformed data')

plt.subplot(224)
plt.plot(range(len(X)), X)
plt.title('FFT')

plt.show()
'''
