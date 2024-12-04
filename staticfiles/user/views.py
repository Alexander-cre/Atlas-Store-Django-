from django.shortcuts import render,redirect
from django.contrib.auth import login , logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm , UserCreationForm , AuthenticationForm 
from .forms import UserUpdateForm , ProfileUpdateForm
from .models import Profile

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('/')
        
    else:
        form = UserCreationForm()
    return render(request , 'register/register.html/', {'form':form}) 

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user()) 
            return redirect("/products/")
        
    else:
        form = AuthenticationForm()
        return render(request , "login/SignIn.html", {'form' :form })     
    
def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect('/')    
    

# Gets Logged in user information
@login_required    
def profile_view(request):
    user = request.user 
    return render(request , 'account/profile.html' , {'user': user})

@login_required
def profile_update_view(request):
    # Ensures the user has a profile
    if not hasattr(request.user , 'profile'):
        Profile.objects.create(user=request.user) 

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST , instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/user/profile')
        # Back to Profile Page after updaing

    else :
        user_form = UserUpdateForm(request.POST , instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        context = {
            'user_form': user_form ,
            'profile_form' : profile_form
        }

    return render(request , 'account/updateProfile.html' , context )
