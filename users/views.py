from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)    # 가입 폼을 만든다
        if form.is_valid():
            user = form.save(commit=False)    # 바로 저장하지 않고
            user.username = user.username.lower()    # 이름을 소문자로 바꿔서
            user.save()    # 저장
            messages.success(request, "You have signed up seccessfully")
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'users/register.html', {'form': form})


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()    # get 기본 생성자
        return render(request, 'users/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)    # 매게인자 있는 생성자

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('posts')
            # 유효하지 않거나 사용자가 인증되지 않은 경우
            messages.error(request, f'Invalid username or password')
            return render(request, 'users.lognin.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('login')
