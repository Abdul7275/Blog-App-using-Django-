from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import *
from django.contrib import auth
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def index(request):
#    return HttpResponse('Hello World')
    return render(request,'parallax.html')


# Create your views here.
def nxt(request):
#    return HttpResponse('Hello World')
    person={'fname':'Abdul', 'city':'Kannauj'}
    abdul="Hello Kalam Bhai"
    data=info.objects.all().order_by('fname')
    if request.method=='POST':
        form=myform(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/nextpage')
    else:
        form=myform()
    return render(request,'nextpage.html',{'info':data,'form':form})
#18

def detail(request,d):
    data=info.objects.get(id=d)
    return render(request,'detail.html',{'det':data})
    
def delete_record(request,d):
    a=info.objects.get(id=d)
    a.delete()
    #data=info.objects.all()
    #return render(request,'nextpage.html',{'info':data})
    return HttpResponseRedirect('/nextpage')
#30
def form(request):
    if request.method=='POST':
        form=myform(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/nextpage')
    else:
        form=myform()
    return render(request,'contact.html',{'form':form})
#47


def comment(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        form=blogform()
        posts=blog.objects.all().order_by('-date_created')
        abdul='Enter post title in search box to search a post'
        if request.POST:
            if 'post_comment' in request.POST:
                form=blogform(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/blog/')
            elif 'search_btn' in request.POST:
                squery=request.POST['search_box']
                if squery:
                    s=blog.objects.filter(title__icontains=squery)
                    if not s:
                        s=blog.objects.filter(description__icontains=squery)
                    return render(request,'post.html',{'q':s,'form':form,'post':posts})
        else:
            abdul='Enter post title in search box to search a post'
        return render(request,'post.html',{'form':form,'post':posts,'abdul':abdul,'fullname':request.user.username})


def register_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/blog')
    else:
        form = UserForm()
        #form = RegForm()
        if request.method=='POST':
            form=UserForm(request.POST)
            #form = RegForm(request.POST)
            if form.is_valid():
                user = form.save(commit = False)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                email = form.cleaned_data['email']
                user.set_password(password)
                form.save()
                return render(request, 'login.html',{'registered':'Account Registered,You may Log in now'})
        return render(request,'register.html',{'form':form})

def check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/blog')
    else:
        return render(request,'login.html',{'error_message':'Invalid Login'})
        #return HttpResponseRedirect('/invalid/')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/blog/')


#55
#Delete Post
def deletePost(request,d):
    a=blog.objects.get(id=d)
    a.delete()
    return HttpResponseRedirect('/blog/')
#61
def search(request):
    if request.POST:
        squery=request.POST['search_box']
        if squery:
            s=info.objects.filter(fname__icontains=squery)
            if s:
                return render(request,'search.html',{'q':s})
            else:
                return render(request,'notfound.html')
        else:
            return HttpResponseRedirect('/')
    else:
        return render(request,'search.html')
