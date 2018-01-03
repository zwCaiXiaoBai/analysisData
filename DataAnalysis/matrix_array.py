# encoding=utf-8
import numpy as np


def main():
    lst = [[1, 3, 5], [2, 4, 6]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    np_lst = np.array(lst, dtype=np.float)
    # bool,int,int8,int16,uint8,float,float16
    print(np_lst.shape)  # (2, 3)
    print(np_lst.ndim)
    print(np_lst.size)
    print(np_lst.dtype)
    print(np_lst.itemsize)
    print(np.zeros([2, 4]))
    print(np.ones([3, 5]))

    print('Rand:')
    print(np.random.rand(2, 4))
    print(np.random.rand())
    print('RandInt:')
    print(np.random.randint(1, 10, 5))
    print('Randn标准正态分布随机数:')
    print(np.random.randn(1, 10))
    print('Choice从指定中随机生成:')
    print(np.random.choice([10, 20, 30]))
    print('Distribute生成特定分布:')
    print(np.random.beta(1, 10, 100))  # beta分布

    print(np.arange(1, 11).reshape([2, 5]))  # 可缺省为-1
    lst = np.arange(1, 11).reshape([2, 5])
    print('exp')
    print(np.exp(lst))  # 自然指数
    print('exp2')
    print(np.exp2(lst))  # 2指数
    print('sqrt')
    print(np.sqrt(lst))
    print('sin')
    print(np.sin(lst))
    print('log')
    print(np.log(lst))

    print('多维数组')  # axis越大，深入程度越高
    lst = np.array([[[1, 2, 3, 4], [4, 5, 6, 7]],
                    [[7, 8, 9, 10], [10, 11, 12, 13]],
                    [[13, 14, 15, 16], [17, 18, 19, 20]]
                    ])
    print(lst.sum(axis=0))
    print(lst.max(axis=0))

    print('数据操作')
    lst1 = np.array([10, 20, 30, 40])
    lst2 = np.array([1, 2, 3, 4])
    print('Add')
    print(lst1 + lst2)
    print('Sub')
    print(lst1 - lst2)
    print('Mul')
    print(lst1 * lst2)
    print('Div')
    print(lst1 / lst2)
    print('Square')
    print(lst1 ** 2)
    print('Dot矩阵操作')
    print(np.dot(lst1.reshape([2,2]),lst2.reshape([2,2])))

    print('Cancatenate水平拼接')
    print(np.concatenate((lst1,lst2),axis=0))

    print('vstack垂直拼接')
    print(np.vstack((lst1, lst2)))

    print('hstack水平拼接')
    print(np.hstack((lst1, lst2)))

    print('split切分4分')
    print(np.split(lst1, 4))
    print(np.copy(lst1))

    print('线性方程组')

if __name__ == "__main__":
    main()
