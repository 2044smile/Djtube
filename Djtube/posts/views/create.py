from django.shortcuts import render
from django.views.generic import View

from posts.models import Post


class PostCreateFormView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'posts/new.html',
            context={},
        )

    def post(self, request, *args, **kwargs):
        Post.objects.create(
            video_id=request.POST['video_id'],
            title=request.POST['title'],
            content=request.POST['content'],
        )


class PostCreateConfirmView(View):
    pass
