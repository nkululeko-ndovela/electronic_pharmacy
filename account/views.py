from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from ePrescribe.models import Patient
from .forms import SignUpForm, LoginForm
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.instance.is_patient = True
            form.instance.password = make_password(form.instance.password)
            PatientProfile = Patient.objects.create(username=form.instance.username, password=form.instance.password)
            PatientProfile.save()
            form.save(commit=True)
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin-page')
            elif user is not None and user.is_doctor:
                login(request, user)
                return redirect('med-rec-list')
            elif user is not None and user.is_pharmacist:
                login(request, user)
                return redirect('prescription-list')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('med-rec-list')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login_view")


def admin(request):
    return render(request,'ePrescribe/templates/index.html')
