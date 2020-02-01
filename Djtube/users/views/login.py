from django.contrib import messages
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'users/login.html',
            context={},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('username')

        next_url = request.POST.get('next_url') or reverse('login')  # FIXME: redirect to home

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                '성공적으로 로그인 되었습니다.'
            )
            return redirect(reverse('login'))

        return redirect(next_url)
