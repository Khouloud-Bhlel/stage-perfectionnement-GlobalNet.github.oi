from django import forms
from captcha.fields import CaptchaField

class FormWithCaptcha(forms.Form):
    captcha = CaptchaField()
