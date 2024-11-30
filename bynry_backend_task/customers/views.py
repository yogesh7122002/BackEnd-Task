from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm, UserRegisterForm
from .models import ServiceRequest


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')


@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            # Save Data Into the database
            form.save()
            return redirect('request_success')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})


@login_required
def request_success(request):
    return render(request, 'request_success.html')


def view_request(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'view_request.html', {'requests': requests})


@login_required
def profile(request):
    user_requests = ServiceRequest.objects.filter(customer_email=request.user.email)
    return render(request, 'profile.html', {'user_requests': user_requests})