from django.shortcuts import render
from django.views.generic import View


class PostCreateFormView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'posts/new.html',
            context={},
        )

    def post(self, request, *args, **kwargs):
        pass


# class PostCreateConfirmView(View):
#     def post(self, request, *args, **kwargs):
#         return render(
#             request,
#             'posts/confirm.html',
#             context={},
#         )