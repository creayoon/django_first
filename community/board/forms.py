from django import forms
# from .models import Board

class BoardForm(forms.Form):
    title = forms.CharField(max_length=32, label="제목", error_messages={
         'required':'제목을 입력해주세요'
    })
    contents = forms.CharField(widget=forms.Textarea, label="내용", error_messages={
         'required':'내용을 입력해주세요'
    })
    tags = forms.CharField(label="태그", required=False )
