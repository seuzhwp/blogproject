# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse


# Create your views here.

def index(request):
    # return HttpResponse("hello world!")
    post_list = Post.objects.all().order_by('-created_time')
    # return render(request, "blog/index.html", context={
    #     'title': 'my blog',
    #     'welcome': 'welcome to my blog'
    # })
    return render(request, 'blog/index.html', context={
        'post_list'
    })
