from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return HttpResponse("Nexus cloud for bug bounty here we come")


def signup(request):
    def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                messages.success(request, f'Account created for {username}!')
                return redirect('home')  # Redirect to a home page or another page
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')        
