from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages 
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.views.generic import DetailView
def register(request):
    form = None 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}! You can now login to your account!")
            return redirect('login')
    else:
        form = UserRegisterForm() 
    return render(request, 'users/register.html', {"form": form})

@login_required
def profile(request):
    if request.method == "POST":    
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if (u_form.is_valid() and p_form.is_valid()):
            u_form.save() 
            p_form.save()  
            messages.success(request, f"Your changes are saved! Your account is updated!")
            return redirect("user-profile")
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form, 
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def profile_view(request, id):
    user = User.objects.filter(id=id).first()
    return render(request, 'users/profile-view.html', {"u":user}) 

class ProfileDetailView(DetailView):
    model = User 
