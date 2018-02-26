from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate

from account.forms import UserModelForm


class SignUp(View):
    form_user = UserModelForm

    def get(self, request):
        form = self.form_user(None)
        context = {'form': form}

        return render(request, 'account/sign_up.html', context)

    def post(self, request):
        form = self.form_user(request.POST)
        context = {'form': form}

        if form.is_valid():
            user = form.save(commit=False)

            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            user.set_password(password)
            user.save()

        return render(request, 'account/sign_up.html', context)

