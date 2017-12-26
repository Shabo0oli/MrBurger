from django.conf.urls import url
from controlcenter.views import controlcenter
from . import views

urlpatterns = [
    url(r'^api/answer/?$', views.answer, name='answer'),
    url(r'^$', views.index, name='index'),
    url(r'^export/$', views.export, name='export'),
]

