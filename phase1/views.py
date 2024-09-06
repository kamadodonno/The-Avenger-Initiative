from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.conf import settings

SECRET_CODE = 'Tony Stank'

def index(request):
    if request.method == "GET":
        query = request.GET.get('q', None)

        if query:
            if query.lower() == 'ironwarr!or27':  # Update the secret code here
                return redirect('login')
            else:
                google_url = f"https://www.google.com/search?q={query}"
                return redirect(google_url)
        else:
            return render(request, 'index.html')

@login_required
def iron(request):
    return render(request, 'iron.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data.get('secret_code')
            if entered_code == settings.SECRET_SIGNUP_CODE:
                user = form.save()
                login(request, user)
                return redirect('login')
            else:
                form.add_error('secret_code', 'The secret code is incorrect. Please try again.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('iron')  # Redirect to iron page after login
            else:
                form.add_error(None, 'Invalid username or password.')
        else:
            form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})