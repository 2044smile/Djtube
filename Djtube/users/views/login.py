from django.contrib import messages
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.conf import settings


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'users/login.html',
            context={},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        next_url = request.POST.get('next_url') or reverse('users:login')  # FIXME: redirect to home

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                settings.LOGIN_SUCCESS_MESSAGE
            )
            return redirect(reverse('users:login'))

        return redirect(next_url)
