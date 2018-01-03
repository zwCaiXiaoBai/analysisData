# encoding=utf-8

import numpy as np
from scipy.integrate import quad,dblquad,nquad
def main():

    # 1--Integral
    print(quad(lambda x:np.exp(-x),0,np.inf))
    # 2--Integral  二维积分
    print(dblquad(lambda t,x:np.exp(-x*t)/t**3,0,np.inf,lambda x:1,lambda x:np.inf))

    def f(x,y):
        return x*y
    def bound_y():
        return [0,0.5]
    def bound_x(y):
        return [0,1-2*y]
    print(nquad(f,[bound_x,bound_y]))

    # Optimizer优化器,求取最值,求根
    from scipy.optimize import minimize
    def rosen(x):
        pass


if __name__=="__main__":
    main()