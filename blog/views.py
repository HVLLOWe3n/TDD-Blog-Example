from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login

from datetime import datetime

from blog.forms import PostForm
from .models import Post


def main_page(request):
    posts = Post.objects.filter(published_date__lte=datetime.now()).order_by('-create_date')

    context = {'posts': posts}

    return render(request, 'blog/post_list.html', context)


class New_Post(View):
    def get(self, request):
        form = PostForm(None)
        context = {'form': form}

        return render(request, 'blog/post_new.html', context)

    def post(self, request):
        form = PostForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            author = request.POST['author']
            title = request.POST['title']
            text = request.POST['text']

            p = Post(author=author, title=title, text=text)
            p.save()
            return redirect('/')

        return render(request, 'blog/post_new.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        'post_info': post
    }

    return render(request, 'blog/post_detail.html', context)
