from django.conf.urls import url

from agent import views

urlpatterns = [
    url(r'^$', views.all),      #'^$'约束空字符串   '^index/$'
    url(r'^index', views.index, name='index'),
]
