from django.urls import path

from posts.views import *


app_name = 'posts'
urlpatterns = [
    path('new/', PostCreateView.as_view(), name='create'),
    path('confirm/', PostCreateConfirmView.as_view(), name='confirm'),
]