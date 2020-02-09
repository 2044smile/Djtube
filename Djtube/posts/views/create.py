from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from posts.models import Post
from posts.utils import youtube


class PostCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'posts/new.html',
            context={},
        )

    def post(self, request, *args, **kwargs):
        video_id = request.POST.get('video_id')
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = request.user.post_set.create(
            video_id=video_id,
            title=title,
            content=content,
        )
        post.save()

        return redirect(reverse('posts:create'))


class PostCreateConfirmView(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('posts:create'))

    def post(self, request, *args, **kwargs):
        video_id = request.POST.get('video_id')
        title = request.POST.get('title')
        content = request.POST.get('content')

        return render(
            request,
            'posts/confirm.html',
            context={
                'video_id': video_id,
                'title': title,
                'content': content,

                "youtube_original_url": youtube.get_youtube_original_url(video_id),
                "youtube_embed_url": youtube.get_youtube_embed_url(video_id),
            },
        )
