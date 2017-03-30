from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

# Create your views here.

from .models import Profile, Akcija


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(username=username, password=password)
            if user.is_authenticated():
                return HttpResponseRedirect('/feed')
        except AttributeError:
            return render(request, 'login.html', {'errormsg': 'Not valid form'})
        return render(request, 'login.html', {})


class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html', {})

    def post(self, requset):
        username = requset.POST['username']
        password = requset.POST['password']
        password_confirm = requset.POST['password_confirm']
        email = requset.POST['email']
        ime = requset.POST['ime']
        prezime = requset.POST['prezime']

        if not password == password_confirm:
            return render(requset, 'register.html', {'errormsg': 'ne poklapaju ti se sifre maleniii'})

        try:
            user = User.objects.create(username=username, password=password, email=email, first_name=ime, last_name=prezime)
        except IntegrityError:
            return render(requset, 'register.html', {'errormsg': 'Username vec postoji!'})
        profile = Profile.objects.create(user=user)
        profile.save()
        return HttpResponseRedirect('/admin')


class FeedView(View):

    def get(self, request):
        lista_akcija = Akcija.objects.all().filter(successful=False)
        context = {
            'lista_akcija': lista_akcija,
        }
        return render(request, 'feed.html', context)

def show_akcija(request, id=None):
    instance = get_object_or_404(Akcija, id=id)
    context = {
       "instance": instance,
        "title": instance.title,
    }
    return render(request, "akcija_detail.html", context)
