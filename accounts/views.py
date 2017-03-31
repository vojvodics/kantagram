from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from .models import Profile, Akcija, Komentar

# Create your views here.




class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('feed'))
        return render(request, 'login.html', {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(username=username, password=password)
            if user.is_authenticated():
                login(request, user)
                return redirect(reverse('feed'))
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
        login(requset, user)
        return redirect(reverse('feed'))


class FeedView(View, LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        lista_akcija = Akcija.objects.all().filter(successful=False)
        context = {
            'lista_akcija': lista_akcija,
        }
        return render(request, 'feed.html', context)

'''
@login_required(login_url='/login/')
def show_akcija(request, id=None):
    instance = get_object_or_404(Akcija, id=id)
    context = {
       "instance": instance,
        "title": instance.title,
    }
    return render(request, "akcija_detail.html", context)
'''

# @login_required(login_url='/login/')
class Show_akcija(View):

    def get(self, request, id=None):
        instance = get_object_or_404(Akcija, id=id)
        comments = instance.komentar_set.all()

        if request.user.is_authenticated():
            ulogovan = True
        else:
            ulogovan = False
        context = {
           "instance": instance,
            "title": instance.title,
            "comments" : comments,
            "ulogovan" : ulogovan
        }
        return render(request, "akcija_detail.html", context)

    def post(self, request, id=None):

        user = request.user
        instance = get_object_or_404(Akcija, id=id)
        Komentar.objects.create(autor=user, tekst=request.POST['tekst'], akcija=instance)

        comments = instance.komentar_set.all()

        if request.user.is_authenticated():
            ulogovan = True
        else:
            ulogovan = False
        context = {
           "instance": instance,
            "title": instance.title,
            "comments" : comments,
            "ulogovan" : ulogovan
        }
        return render(request, "akcija_detail.html", context)


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

