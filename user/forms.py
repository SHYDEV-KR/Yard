from allauth.account.forms import SignupForm
from django import forms
from .models import *

YEARS= [x for x in range(1940,2030)]

class CustomSignupForm(SignupForm):
    nickName = forms.CharField(label="닉네임", max_length=30)
    gender = forms.ChoiceField(label="성별", choices=GENDER_CHOICES, required=False)
    birth = forms.DateField(label="생년월일", widget=forms.SelectDateWidget(years=YEARS), initial="2022-01-01", required=False)
    userImg = forms.ImageField(label="유저 이미지", required=False)

    field_order = ['email', 'password1', 'password2',  'userImg', 'nickName', 'gender', 'birth']

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.nickName = self.cleaned_data['nickName']
        user.gender = self.cleaned_data['gender']
        user.birth = self.cleaned_data['birth']
        user.userImg = self.cleaned_data['userImg']
        user.save()
        return user


class createFeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = "__all__"
    createdDate = forms.DateField(label='date', widget=forms.SelectDateWidget)

class createCertForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ('albumImg', 'title', 'artist', 'albumTitle', 'releasedDate') 