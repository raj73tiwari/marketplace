from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form=forms.Signin_form(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            user_name=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {user_name}, Account Created Successfully ! ')
            return redirect('basicapp:index')
    else:
        form=forms.Signin_form()
    context={'form':form}
    return render(request,'user/signup.html',context)

def profile(request):
    return render(request,'user/profile_form.html')


