from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import logout


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('login'))