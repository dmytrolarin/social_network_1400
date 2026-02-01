from django.shortcuts import render
from django.http import HttpRequest
from .models import Post


def render_posts(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, 'post_app/posts.html', context= {"posts": posts})
