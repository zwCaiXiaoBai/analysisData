### 这是我日常遇到的一些小问题的解决办法，全部是基于Python3

1.[获取当前CPU状态，存储到Influxdb](https://github.com/injetlee/demo/blob/master/CpuToInfluxdb.py)

2.[模拟登录知乎](https://github.com/injetlee/demo/blob/master/login_zhihu.py)

3.[对目录下所有文件计数](https://github.com/injetlee/demo/blob/master/countFile.py)


4.[爬取豆瓣电影top250](https://github.com/injetlee/demo/blob/master/douban_movie.py)

5.[Excel文件读入数据库](https://github.com/injetlee/demo/blob/master/excelToDatabase.py)

6.[爬取拉勾网职位信息](https://github.com/injetlee/demo/blob/master/lagouSpider.py)

7.[批量修改文件名](https://github.com/injetlee/demo/blob/master/ModifyFilename.py)

8.[读写excel](https://github.com/injetlee/demo/blob/master/readExcel.py)

9.[下载必应首页图片,只下载当天的，一张。](https://github.com/injetlee/Python/blob/master/biyingSpider.py)


python中一切都是对象，类型属于对象，变量是没有类型的.
python是一个动态语言

### 基本语法
__foo 私有成员,只能类本身使用
_foo 表示不能直接访问的类属性，需通过类提供的接口访问，一般是protected
__foo__特殊方法专用

### 字符串
* Python不支持单字符类型，单字符也在Python也是作为一个字符串使用
* 将复杂的字符串进行复制，可以包含各种符号
* 内建函数，各种符号
* u'Hello World !' 表示Unicode编码

### 数据结构
序列
* 列表list[],包含一些函数和方法，包含各种数据
* 元组tup(),固定长度，单元素 tuple 要多加一个逗号“,”
* dict{}，通过get,in获取，返回none,无须，key不可变,values()得到value列表，itervalues(),items()得到对象列表
* 时间和日期
* set(['a','b','c']) in访问
* 对list进行切片L[0:3]=L[:3]
函数
* 可改变mutable和不可变对象immutable
* 关键词参数(可通过参数名改变顺序)，必备参数(和预定义的相同)，缺省参数age=25，不定长参数*var_args

匿名函数
lambda x:x+3


模块
* 如果要给函数内的全局变量赋值，必须使用 global 语句
包
*  __init__.py必须存在该文件

异常
* 一个异常可以是一个字符串，类或对象。
面向对象
* 类
__init__()构造方法或初始化方法，创建类的实例时调用
self类实例，代表当前对象地址
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
析构函数 __del__ 在对象销毁的时候被调用
基类的__init__()方法不会自动调用
全局变量 __name__，模块的模块名


迭代 for . in ...一种抽象的数据操作
注意: 集合是指包含一组元素的数据结构，我们已经介绍的包括：
1. 有序集合：list，tuple，str和unicode；
2. 无序集合：set
3. 无序集合并且具有 key-value 对：dict

enumertate()函数：迭代的每一个元素是tuple


模块管理
- easy_install
- pip(官方推荐，已内置到python2.7.9版本中)

常用函数,内置函数
range(1,11)
len(p)


列式生成式
[x * x for x in range(1, 11) if x % 2 == 0]

[m + n for m in 'ABC' for n in '123'] 多层表达式相当于双层循环

['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]

作用域，命名空间
* 不同的命名空间没有任何联系

包和普通模块的区别



问题
* python常用技术栈
* if __main__()
* 语言的理解
        **kw
for k,v in kw.iteritems():
            setattr(self,k,v)
自适应任何参数定义的函数，可以利用Python的 *args 和 **kw，保证任意个数的参数总是能正常调用


需要根据num计算出斐波那契数列的前N个元素。

参考代码:

class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print f
print len(f)