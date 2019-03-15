from django.conf.urls import url
from . import views

app_name='forum'
urlpatterns = [
  
    url(r'^$',views.index, name="index"),
    
    #/music/71/
    
    url(r'^(?P<thread_id>[0-9]+)/$',views.detail,name='detail'),  
    url(r'thread/add/$',views.threadCreate.as_view(),name='thread-add'), 
]