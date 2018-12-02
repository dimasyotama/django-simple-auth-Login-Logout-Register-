from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from account.forms import SignUpForm


@login_required
def home(request):
    return render(request, 'account/home.html')


def signup(request):
    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user,password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'account/signup.html',{'form':form})


