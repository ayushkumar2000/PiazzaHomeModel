from django.conf.urls import url
from .import views

app_name='forum'
urlpatterns = [
  
    url(r'^$',views.index, name="index"),
    
    #/music/71/
    
    url(r'^(?P<thread_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<thread_id>[0-9]+)/add/$',views.commentCreate.as_view(),name='comment-add'),  
    url(r'thread/add/$',views.threadCreate.as_view(),name='thread-add'), 
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'^login/$',views.LoginFormView.as_view(),name='login'),
    url(r'^superuser/$',views.SuperUserFormView.as_view(),name='superuser'),
    url(r'^logout/$',views.logoutq,name='logout'),
]