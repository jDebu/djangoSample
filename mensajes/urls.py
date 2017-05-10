from django.conf.urls import url

from . import views

app_name = 'mensajes'
urlpatterns = [
	url(r'^$', views.IndexView.as_view()),
    url(r'^test/(?P<pk>[0-9]+)/$', views.TestView.as_view()),
    url(r'^test2/$', views.get_name , name='home')
]