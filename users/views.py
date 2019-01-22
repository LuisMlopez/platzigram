from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

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
            form.save()

            login(request, form.instance)
            return redirect('posts_list')

    else:
        form = CreateUserForm()

    return render(request, 'users/signup.html', {'form': form})


class UserProfile(DetailView, LoginRequiredMixin):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = {}
        user = self.get_object()
        if user:
            posts = user.post_set.all()
            context.update({'posts': posts})

        context.update(kwargs)
        return super().get_context_data(**context)


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
            url = reverse(
                'profile',
                kwargs={'username': request.user.username}
            )
            return redirect(url)

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
