from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^news/(?P<id>(\d+))$',views.single_news, name='news'),
    url(r'^$',views.index,name='index')
]
