from django.shortcuts import render
from django.http import HttpResponse
from .models import thread
from django.http import Http404
from .models import comment
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
def index(request):
     
    all_thread = thread.objects.all()
    context={ 'all_thread' : all_thread }    
    return render(request, 'index.html',context)


def detail(request,thread_id):
    
    try:
        thread1=thread.objects.get(pk=thread_id)

    except:
        raise Http404("Thread doesnot exist")
    all_thread = thread.objects.all()
    all_comment= comment.objects.all()
    
    return render(request, 'details.html',{ 'all_thread' : all_thread ,'thread_id':thread_id,'all_comment' : all_comment,'thread1':thread1})
    #return HttpResponse("<h2>here is your comment"+str(thread_id)+"</h2>") 

class threadCreate(CreateView):
    model=thread
    fields=['value','subject']
    fields_alt=['author','time'] 