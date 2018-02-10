# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, HttpResponse

from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'billboard_app/post_list.html', {'posts': posts, "form" :form})

# def post_create(request):
#     form = PostForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         print form.cleaned_data.get("title")
#         instance.save()
#     return render(request, 'billboard_app/post_form.html', {'form': form})

# def base(request):
#     return render(request,'billboard_app/base.html')