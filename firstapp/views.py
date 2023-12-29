from django.shortcuts import render,redirect
from .forms import UserRegister
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
# Create your views here.

def home(request):
    logout_message = messages.get_messages(request)
    return render(request, 'home.html', {'logout_message': logout_message})


def user_signup(request):
    if request.method=='POST':
        form=UserRegister(request.POST)
        if form.is_valid():
            messages.success(request,'user created successfully,now you are login page ')
            form.save()
            return redirect('user_login')
        
    else:
        form=UserRegister()
    return render(request,'user_signup.html',{'form':form})
            



def user_login(request):
    if  not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                user_pass=form.cleaned_data['password']
                user =authenticate(username=name,password=user_pass)
                if user is not None:
                    messages.success(request,'Logged In Successfully')
                    login(request,user)
                    return redirect('profile')
                else:
                    messages.error(request, 'Invalid username or password')
                    
            else:
                
                return render(request, 'user_login.html', {'form': form})
                  
        else:
            form=AuthenticationForm()
            return render(request,'user_login.html',{'form':form})
        
    else:
        return redirect('profile')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('homepage')

def profile(request):
    if  request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('user_login')
    
def pass_change2(request):
    if request.method=='POST':
        form=SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            messages.success(request,'password updeted successfully')
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect ('profile')
    else:
         form=SetPasswordForm(user=request.user,data=request.POST)
         return render(request,'pass_change.html',{'form':form})
def pass_change(request):
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            messages.success(request,'password updeted successfully')
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect ('profile')
    else:
         form=PasswordChangeForm(user=request.user,data=request.POST)
         return render(request,'pass_change.html',{'form':form})