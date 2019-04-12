from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static 
app_name='forum'
urlpatterns = [
  
    url(r'^$',views.index, name="index"),
    
    #/music/71/
    
    url(r'^(?P<thread_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<thread_id>[0-9]+)/add/$',views.commentCreate.as_view(),name='comment-add'),  
    url(r'thread/add/$',views.threadCreate.as_view(),name='thread-add'), 
    url(r'resource/add/$',views.resourceCreate.as_view(),name='resource-add'), 
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'^login/$',views.LoginFormView.as_view(),name='login'),
    url(r'^superuser/$',views.SuperUserFormView.as_view(),name='superuser'),
    url(r'^logout/$',views.logoutq,name='logout'),
    url(r'^(?P<pk>[0-9]+)/delete/$',views.threadDelete.as_view(),name='thread-delete'),
    url(r'resource/$',views.Resource,name='resources'),
    
    
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
