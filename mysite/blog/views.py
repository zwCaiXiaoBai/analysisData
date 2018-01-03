from django.shortcuts import render
from django.db import connection
# Create your views here.

from django.http import HttpResponse
from . import models

def index(request):
    print('blog/view')
    f = models.Article.objects.get(pk=1)
    return render(request,'blog/index.html',{'article':f})


def all(request):
    print('blog/all')
    articles = models.Article.objects.all()
    return render(request, 'blog/all.html', {'articles': articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,"blog/article_page.html",{'article':article})

def edit_page(request,article_id):
    print('blog/edit')
    if str(article_id)=='0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html',{'article':article})



def edit_action(request):
    print('blog/edit/action')
    title = request.POST.get("title",'TITLE')
    content = request.POST.get('content','CONTENT')
    article_id = request.POST.get('article_id','0')
    if str(article_id)=='0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/all.html', {'articles': articles})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    articles = models.Article.objects.all()
    return render(request,'blog/all.html',{'articles':articles})




def dbc():
    # 创建连接
    config = {
        'user': 'root',
        'password': 'Bg1234',
        'host': '192.168.15.211',
        'port': 3306,
        'database': 'bgdb'}
    conn = connection(**config)

    # 创建游标
    cur = conn.cursor()

    # 执行查询SQL
    sql = "select * from student"
    cur.execute(sql)

    # 获取查询结果
    result_set = cur.fetchall()
    if result_set:
        for row in result_set:
            print("%s, %s, %s, %s, %s, %s" % (row[0], row[1], row[2], row[3], row[4], row[5]))

    # 关闭游标和连接
    cur.close()
    conn.close()





