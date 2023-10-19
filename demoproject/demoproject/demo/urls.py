from django.urls import path
from . import views
app_name='demo'
urlpatterns = [
    path('',views.func,name="func"),
    #path('passingvalue',views.passingval,name='passing'),
    #path('getvalue',views.getentry,name='getval'),
    #path('add',views.addition,name='addition'),
    #path('index',views.index,name='index')
]
