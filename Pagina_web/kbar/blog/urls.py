from nturl2path import url2pathname
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.Blog, name='Blog'),
    path('categoria/<int:categoria_id>/',views.categoria, name="categoria"),
]


