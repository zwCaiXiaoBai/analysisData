# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def main():
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)
    plt.figure(1)
    plt.plot(x, c, color='blue', linewidth=1.0, linestyle="-", label="COS", alpha=0.5)
    plt.plot(x, s, "r*", label="SIN")
    plt.title('cos & sin')

    ax = plt.gca()  # 轴的编辑器
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.2))

    plt.legend(loc='upper left')
    plt.grid()
    # plt.axis([-1,1,-0.5,1])  #显示范围

    plt.fill_between(x, abs(x) < 0.5, c, c > 0.5, color='green', alpha=0.25)
    t = 1
    plt.plot([t, t], [0, np.cos(t)], 'y', linewidth=3, linestyle='--')
    plt.annotate('cos(1)', xy=(t, np.cos(1)), xycoords='data', xytext=(+10, +30),
                 textcoords="offset points", arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
    plt.show()


# 散点图
def scaphrase():
    fig = plt.figure()
    ax = fig.add_subplot(3, 3, 1)
    n = 128
    x = np.random.normal(0, 1, n)
    y = np.random.normal(0, 1, n)
    T = np.arctan2(y, x)
    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.scatter(x, y, s=75, c=T, alpha=0.5)
    plt.xlim(-1.5, 1.5), plt.xticks([])
    plt.ylim(-1.5, 1.5), plt.yticks([])
    plt.axis()
    plt.title('scatter')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


# 饼图
def piehrase():
    fig = plt.figure()
    # ax = fig.add_subplot(3, 3, 2)
    n = 20
    zz = np.ones(n)
    zz[-1] *= 2
    plt.pie(zz, explode=zz * 0.5, colors=['%f' % (i / float(n)) for i in range(n)],
            labels=['%.2f' % (i / float(n)) for i in range(n)])
    plt.gca().set_aspect('equal')
    plt.xticks([]), plt.yticks([])

    plt.show()


# 条形图
def barhrase():
    fig = plt.figure()
    # ax = fig.add_subplot(3, 3, 2)
    n = 10
    xx = np.arange(n)
    y1 = (1 - xx / float(n)) * np.random.uniform(0.5, 1.0, n)
    y2 = (1 - xx / float(n)) * np.random.uniform(0.5, 1.0, n)

    plt.bar(xx, +y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(xx, -y2, facecolor='#ff9999', edgecolor='white')

    for x, y in zip(xx, y1):
        plt.text(x + 0.4, y + 0.0, '%.2f' % y, ha='center', va='bottom')

    for x, y in zip(xx, y2):
        plt.text(x + 0.4, -y - 0.0, '%.2f' % y, ha='center', va='top')
    plt.show()


# 极坐标图
def polarhrase():
    fig = plt.figure()
    #ax = fig.add_subplot(3, 3, 2,polar = True)
    n = 20
    theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / n)
    radii = 10 * np.random.rand(n)

    plt.polar(theta, radii)
    plt.show()


# 热图
def hotphrase():
    fig = plt.figure()
    # ax = fig.add_subplot(3, 3, 2)
    data = np.random.rand(3,3)
    cmap = cm.Blues
    map = plt.imshow(data,interpolation='nearest',cmap=cmap,aspect='auto',vmin=0,vmax=1)
    plt.show()


# 3D图
def D3phrase():
    fig = plt.figure()
    ax = fig.add_subplot(336,projection='3d')
    ax.scatter(1,1,3,s=100)
    plt.show()

# heat热力图
def heatPhrase():
    fig = plt.figure()
    ax = fig.add_subplot(313)
    def f(x,y):
        return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
    n = 256
    x = np.linspace(-3,3,n)
    y = np.linspace(-3,3,n)
    xx,yy = np.meshgrid(x,y)
    plt.contourf(xx,yy,f(xx,yy),8,alpha=0.75,cmap=plt.cm.hot)
    plt.savefig('./data/fig.png')
    plt.show()


if __name__ == "__main__":
    heatPhrase()
