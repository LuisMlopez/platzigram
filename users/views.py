from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from users.forms import CreateUserForm, ProfileForm
from users.models import Profile


def login_view(request):
    if request.user.is_authenticated:
        return redirect('posts_list')

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


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name')
            )

            user_profile = Profile.objects.create(user=user)

            login(request, user)
            return redirect('posts_list')

    else:
        form = CreateUserForm()

    return render(request, 'users/signup.html', {'form': form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if form.is_valid():
            form.save()
            return redirect('update_profile')

    else:
        form = ProfileForm(instance=request.user.profile)

    return render(
        request,
        'users/update_profile.html',
        {
            'form': form,
            'user': request.user
        }
    )
