

### django基本使用
* 参考地址：http://www.imooc.com/learn/790
1、安装django
2、cd /django/
3、执行命令django-admin
4、创建djangoproject:django-admin startproject mysite
5、打开项目
6、python manage.py查看项目管理器功能
7、启动服务python manage.py runserver
8、修改端口python manage.py runserver 9999
9、创建应用cd manage.py 执行python manage.py startapp blog
10、添加应用名到setting.py/installed_apps节点下面
11、在polls的views.py下增加函数
12、在urls.py中进行配置
13、url测试请求 http://127.0.0.1:8000/polls/
14、模板的使用 创建templates文件夹
15、render()函数支持dict类型，键值为参数名，使用{{参数名}}
16、在templates下创建apps名称目录，防止获取html文件冲突
17、models模块实现Model继承
18、生成数据表 执行：python manage.py makemigrations app名（可选），在app/migrations目录下
19、迁移 执行：python manage.py migrate
20、执行：python manage.py sqlmigrate 应用名 文件id,可以查看运行SQL语句
21、SQLite Expert Personal轻量级，数据库软件
22、呈现数据 f = models.Article.objects.get(pk=1),render(request,{'article',f}),{{article.title}}
23、admin管理 python manage.py createsuperuser
24、管理地址 http://127.0.0.1:8000/admin/   账号：admin 密码：bgdbadmin。进行管理后台操作
25、修改语言 settings.py/LANGUAGE_CODE='zh_Hans'    # zh-cn
26、标签for训话{%for xx in xxs%}html{%endfor%}
27、Django html超链接{% url 'app_name:url_name' param%}
28、使用request.post['参数名'] 获取表单数据，Django将结果组装为字典结构
29、{% if .. %},{% else %},{% end if %}
30、Templates过滤器，模板语言。{{value|filter1|filter2|...}},可叠加
31、模板中出现不存在的值，会显示空值
32、Django shell,python交互式命令行工具，引入项目环境和项目进行交互
33、python manage.py shell。  通过直接引进from blog.models import article \n Article.objects.all()
34、通过shell 进行调试，测试未知方法
35、管理后台显示数据字段list_display:通过继承，实现字段扩充
36、管理后台过滤器list_filter:
37、在DEBUG为true时我们只需要建立static目录后，把静态资源放进去就可以访问。在DEBUG为False时需要我们手动指定静态资源目录，并配置映射关系。

### 博客
1、博客主页面
    * 标题==超链接
    * 按钮发表
2、博客文章内容页面
    *
3、博客撰写页面
    * 标题编辑栏
    * 文章内容编辑区
    * 提交按钮

### Django项目部署
1、下载mod_wsgi，注意其版本
2、解压得到mod_wsgi.so文件。拷贝到tomcat\modules\目录下
3、配置web服务，在.conf文件中
    tomcat 存放目录：D:\pydj\Apache24
    django项目目录：D:\pydj\myweb
    #添加mod_wsgi.so 模块
    LoadModule wsgi_module modules/mod_wsgi.so
    #指定myweb项目的wsgi.py配置文件路径
    WSGIScriptAlias / D:/pydj/myweb/myweb/wsgi.py
    #指定项目路径
    WSGIPythonPath D:/pydj/myweb
    <Directory D:/pydj/myweb/myweb>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
4、保持wsgi.py文件不变
5、修改setting.py ALLOWED_HOSTS = ['127.0.0.1', 'localhost']



wsgi.py 服务器网关接口
urls.py url配置文件
setting.py
migrations 内容移植模块，自动生成
admin.py 当前应用的后台管理配置，自带
apps.py 当前应用的配置
models.py 数据模块，使用orm框架，类型MVC中的M
test.py 自动化测试模块
views.py 执行响应的逻辑代码

