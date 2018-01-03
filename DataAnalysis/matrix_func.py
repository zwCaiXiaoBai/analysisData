# encoding=utf-8

import numpy as np
from numpy.linalg import *


def main():
    print(np.eye(3))    #单位矩阵
    print('线性方程组')

    lst = np.array([[1,2],[3,4]])
    print('Inv矩阵的逆:')
    print(inv(lst))
    print("T矩阵转置:")
    print(lst.transpose())
    print("T矩阵行列式:")
    print(det(lst))
    print("T矩阵特征值:特征向量")
    print(eig(lst))
    y=np.array([[5.],[7.]])
    print('Solve解线性方程组')
    print(solve(lst,y))

    print('FFT:其他通讯')
    print(np.fft.fft(np.array([1,1,1,1,1,1,1,1,1,1,1,1])))
    print('Coef:')
    print(np.corrcoef([1,0,1],[0,2,1]))

    print('Poly一元函数:')
    print(np.poly1d([2,1,3]))
if __name__ == "__main__":
    main()
