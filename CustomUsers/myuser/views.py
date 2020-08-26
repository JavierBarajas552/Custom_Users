from django.shortcuts import render, HttpResponseRedirect, reverse
from myuser.models import MyUser
from myuser.forms import LoginForm, SignupForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from CustomUsers import settings
# Create your views here.


@login_required
def index(request):
    return render(request, 'index.html', {'settings': settings})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser = authenticate(request, username=data.get(
                'username'), password=data.get('password'))
            if MyUser:
                login(request, MyUser)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, "generic_form.html", {'form': form})


def logout_veiw(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(username=data.get(
                'username'), password=data.get('password'), displayname=data.get('displayname'))
        login(request, new_user)
        return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = SignupForm()
    return render(request, "generic_form.html", {'form': form})
