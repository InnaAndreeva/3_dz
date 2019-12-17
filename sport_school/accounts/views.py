from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from .models import User_Data
from .userDomainModel import User_DM
# Create your views here.

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        sport_interests = request.POST['sport_interests']

        # Patterns
        user = User_DM.create_user(
            first_name, last_name, username, email, phone, password, password2, sport_interests)
        if user.has_errors():
            for err in user.get_errors():
                messages.error(request, err)
                # return redirect('register')
                return render(request, 'accounts/register.html', status=400)
        else:
            messages.success(request, 'You are now registered. Please log in')
            return redirect('login')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'accounts/login.html', status=400)
            # return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    user_id = request.user.id
    u_d = User.user_data
    context = {'msg_to_user': user_id, 'user_data': u_d}
    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # clear messages
        storage = messages.get_messages(request)
        storage.used = True
        messages.success(request, 'Your are now logged out')
        return redirect('index')


def edit(request):
    return render(request, 'accounts/edit.html')


def save_changes(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        user = User.objects.get(pk=request.user.id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        return redirect('dashboard')
