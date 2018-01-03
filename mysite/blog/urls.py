from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.all),      #'^$'约束空字符串   '^index/$'
    url(r'^index$', views.index, name='index'),
    url(r'^article/(?P<article_id>[0-9]+)', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)', views.edit_page, name='edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
]
