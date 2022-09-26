from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    phone = forms.CharField(label='Ваш телефон', max_length=11)
    email = forms.EmailField(label='Ваша электронная почта')