from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return render(request, 'blog/base.html')