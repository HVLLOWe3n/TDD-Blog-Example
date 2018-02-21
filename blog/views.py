from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import PostForm
from .models import Post


def main_page(request):
    return render(request, 'blog/base.html')


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

        return render(request, 'blog/post_new.html', context)
