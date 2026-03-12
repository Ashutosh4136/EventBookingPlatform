from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileUpdateForm,EditProfileForm
from django.contrib import messages


def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'users/login.html')


@login_required
def logout_view(request):

    logout(request)
    return redirect('login')


@login_required
def profile_view(request):

    if request.method == 'POST':

        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'users/profile.html', {'form': form})



@login_required
def edit_profile(request):

    if request.method == 'POST':

        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')

    else:

        form = EditProfileForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'users/edit_profile.html', context)