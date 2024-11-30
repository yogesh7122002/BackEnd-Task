from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest


def home(request):
    return render(request, 'home.html')


def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('request_success')  # Redirect to a success page (we'll create this)
    else:
        form = ServiceRequestForm()

    return render(request, 'submit_request.html', {'form': form})


def request_success(request):
    return render(request, 'request_success.html')


def view_request(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'view_request.html',{'requests': requests})
