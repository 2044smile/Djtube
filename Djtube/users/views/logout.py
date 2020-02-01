from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import logout


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(
            request,
            messages.SUCCESS,
            settings.LOGOUT_SUCCESS_MESSAGE
        )
        return redirect(reverse('login'))
