from django.conf.urls import url
from . import views
urlpatterns = [
    #/rango/
    url(r'^$', views.rango_index, name='rango_index'),
    #/rango/about/
    url(r'^about/', views.rango_about, name='rango_about')
]
