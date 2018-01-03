#coding=utf-8
import os

import sys

from envs.python35.Tools.scripts.treesync import raw_input

if os.getuid()==0:
    pass
else:
    print("当前不是root用户！！")
    sys.exit(1)

version = raw_input('请输入你想安装的python版本')
if version=='2.7':
    url = 'http://'
elif version=='3.5':
    url = 'http://'
else:
    print('输入有误，请输入。。。')
    sys.exit(1)

cmd = 'wget '+url
res = os.system(cmd)
if res!=0:
    print('下载源码包失败，请检查当前网络！')

if version=='2.7':
    package_name = 'Python-2.7.12'
else:
    package_name = 'Python-3.5.2'
cmd = 'tar xf '+ package_name+'.tgz'
res = os.system(cmd)
if res !=0:
    os.system('rm '+package_name+' .tgz')
    print('解压源码包，请重新下载运行这个源码包')
    sys.exit(1)

cmd = 'cd '+package_name+' && ./configure --prefix=/usr/local/python && make && make install'
res = os.system(cmd)
if res!=0:
    print('编译源码失败，请重新检查依赖库')
    sys.exit(1)