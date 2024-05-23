from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return HttpResponse("Nexus cloud for bug bounty here we come")


def signup(request):
    if request.method == "POST":
        form = UserCreatingForm(request.POST)
        if form.is_valid():
            form.save()