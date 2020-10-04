from django import forms
from .models import User
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="사용자이름", error_messages={
         'required':'아이디를 입력해주세요'
    })
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호 ", error_messages={
         'required':'비밀번호를 입력해주세요'
    })

    # password check
    def clean (self):
        clean_data= super().clean()
        username = clean_data.get('username')
        password = clean_data.get('password')

        if username and password:
            # print('::: User.objects :::', username, dir(User.objects))
            # try:
            #     user = User.objects.get(username=username)
            # except DoesNotExist:
            #     go = None
                
            user_data = User.objects.get(username=username)
            if user_data.password:
                if not check_password(password, user_data.password):
                    self.add_error('password', '비밀번호를 틀렸습니다')
                else:
                    self.user_id = user_data.id