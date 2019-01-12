from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from posts.forms import PostCreateForm
from posts.models import Post


@login_required
def list_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/feed.html', {'posts': posts})


@login_required
def new_post(request):
    if request.method == 'POST':
        # TODO: create form, create template
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.profile = request.user.profile
            post.save()

            return redirect('posts_list')

    else:
        form = PostCreateForm()

    return render(request, 'posts/create.html', {'form': form})
