from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm


def home(request):
    user_id = request.session.get('user')

    if user_id:
        user = User.objects.get(pk=user_id)
        return HttpResponse(user.username)

    return HttpResponse('Home!')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')
         

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    # 연습용
    # if request.method == "GET":
    #     return render(request, 'login.html')
    # elif request.method == "POST":
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)
         
    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = '모든 값을 입력해야 합니다'
    #     else:
    #         # get(attr=input_val)순서
    #         user = User.objects.get(username=username)

    #         if check_password(password, user.password):
    #             print(':::::::::: password checked :::::::::::::, session::: ', user.id)
    #             request.session['user '] = user.id
    #             return redirect('/')
    #         else:
    #             res_data['error'] = '비밀번호가 틀렸습니다'

    return render(request, 'login.html', {'form':form})

    

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        # input값이 없을때 에러처리를 위해 get 사용
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)

        res_data = {}
        if not (username and password and re_password and useremail):
            res_data['error'] = '모든 값을 입력해야 합니다'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            # class 객체생성해서 db에 삽입
            user = User(
                username = username,
                password = make_password(password),
                useremail = useremail
            )
            user.save()

        print('res_data ::::::::::::: ', res_data)
        # return render(request, 'register.html', res_data)
        return redirect('/user/login')
    