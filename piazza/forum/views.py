from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import thread, comment
from django.http import Http404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, LoginForm, SuperUserForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from datetime import datetime, timezone

def index(request):
     
    all_thread = thread.objects.all()
    context={ 'all_thread' : all_thread ,'user': request.user}
    
    if request.user.is_authenticated():
        return render(request, 'index.html',context)
    else:
        return redirect('forum:register')



def detail(request,thread_id):
    
    try:
        thread1=thread.objects.get(pk=thread_id)

    except:
        raise Http404("Thread doesnot exist")
    all_thread = thread.objects.all()
    all_comment= comment.objects.all()
    
    if request.user.is_authenticated():
        return render(request, 'details.html',{ 'all_thread' : all_thread ,'thread_id':thread_id,'all_comment' : all_comment,'thread1':thread1})
    #return HttpResponse("<h2>here is your comment"+str(thread_id)+"</h2>") 
    else:
        return redirect('forum:register')
def logoutq(request):
    logout(request)
    return HttpResponse("<h2>Sucessfully Loggedout</h2>")

class threadCreate(CreateView):
    model=thread
    
    fields=['value','subject']
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        if(self.request.user.is_superuser):
            obj.author_type=2
        else:
            obj.author_type=1
        now = datetime.now(timezone.utc)
        obj.created=now
        
        obj.save()        
        return redirect('forum:index')
    

class commentCreate(CreateView):
    model=comment
    
    fields=['comment']
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.Thread_id = self.kwargs['thread_id']
        #if(self.request.user.is_superuser)
        if(self.request.user.is_superuser):
            obj.author_type=2
        else:
            obj.author_type=1
        obj.save()        
        return redirect('forum:index')

class UserFormView(View):
    form_class=UserForm
    template_name='forum/registration_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request, self.template_name,{'form':form})
    
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)

            user.save()

            user=authenticate(username=username,password=password)
            
            #if user is not None:
            login(request,user)
            return redirect('forum:index')
        else:
            return redirect('forum:register')

class LoginFormView(View):
    form_class=LoginForm
    template_name='forum/login_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request, self.template_name,{'form':form})
    
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return redirect('forum:index')
        
        else:   
            return HttpResponse("<h2>INVALID CREDENTIALS</h2>")              
        
class SuperUserFormView(View):
    
    form_class=SuperUserForm
    template_name='forum/superuserform.html'

    def get(self,request):
        if(request.user.is_superuser):
            form=self.form_class(None)
            return render(request, self.template_name,{'form':form})
        else:
            return HttpResponse('<h2><font color="red"> You are not authorised to view this page</font></h2>') 
        
        
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            
            user=form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            User.objects.create_superuser(username=username, password=user.password, email=user.email, first_name=user.first_name,last_name=user.last_name)
            

            user=authenticate(username=username,password=password)
            
            
            
            return redirect('forum:index')
        else:
            return redirect('forum:register')
