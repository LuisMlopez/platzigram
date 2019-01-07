from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts_list')
        else:
            return render(
                request,
                'users/login.html',
                {'errors': 'Invalid username and password.'}
            )
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
