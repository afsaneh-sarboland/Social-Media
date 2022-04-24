from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Post, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from socialmedia import settings
from django.shortcuts import render, redirect
from django.utils.timezone import timezone


def index(request):
    post_01 = Post.objects.get(id=1)
    post_02 = Post.objects.get(id=2)
    return render(request, 'blog/index.html', {'post_01': post_01, 'post_02': post_02})


def post_detail(request, slug):
    if request.method == "GET":
        template = loader.get_template('blog/post_detail.html')
        post = Post.objects.get(slug=slug)
        comments = post.comment_set.all()
        return HttpResponse(template.render({'post': post,
                                             'comments': comments,
                                             "count_comments": len(comments)},
                                            request))
    elif request.method == "POST":
        author = request.POST["author"]
        author_id = User.objects.get(first_name=author).id
        post_id = Post.objects.get(slug=slug)
        # return HttpResponse(post_id)
        if author_id:
            comment = Comment(content=request.POST["content"],
                              email=request.POST["email"],
                              status=True,
                              author_id=author_id,
                              post_id=post_id)
            comment.save()
            return redirect(f"/blog/detail-post/{slug}")


class PostList(ListView):
    model = Post


def new_post(request):
    if request.method == "GET":
        return render(request, 'blog/new_post.html', {})
    elif request.method == "POST":
        username = request.POST["username"]
        title = request.POST["title"]
        tags = request.POST["tags"]
        content = request.POST["content"]
        image = request.FILES['image']
        author = User.objects.get(username=username)
        post = Post(title=title,
                    tags=tags,
                    content=content,
                    author_id=author,
                    status=True,
                    image=image)
        post.save()
        return HttpResponse("Saved!")


def last_week_posts(request):
    template = loader.get_template('blog/post_list.html')
    posts = Post.objects.get_last_week_posts().all()
    return HttpResponse(template.render({'object_list': posts}, request))