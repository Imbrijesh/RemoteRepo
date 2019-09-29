from django import forms
from .models import ProData


class RegistrationForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' Enter Your Name'
            }
        )
    )
    contact = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' Enter Your Mobile No.'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' Enter Your Email'
            }
        )
    )
    uname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' Enter Your Username'
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' Enter Your Password'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm password'
            }
        )
    )
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name)<=3 or len(name)>=30:
            raise forms.ValidationError("Name Must Have more than 3 or less than 30 Characters ")
        return name

    def clean_uname(self):
        uname = self.cleaned_data.get('uname')
        qs = ProData.objects.filter(uname=uname)
        if qs.exists():
            raise forms.ValidationError("User name is taken already.")
        elif len(uname)<=5:
            raise  forms.ValidationError("User Name Must have more than 5 Chars")
        return uname


    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = ProData.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email name is taken already.")
        elif not 'gmail.com' in email:
            raise forms.ValidationError("Email has to end with gmail.com")
        return email

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        mob = ProData.objects.filter(contact=contact)
        if mob.exists():
            raise  forms.ValidationError('Mobile Number Already Taken')
        elif len(str(contact)) != 10:
            raise forms.ValidationError('Enter Valid Mobile Number')
        return contact


    def clean(self):
        data = self.cleaned_data
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password2 != password1 :
            raise forms.ValidationError("Passwords must match.")
        elif len(password1) <= 4 or len(password1) >= 15:
            raise forms.ValidationError("Password length must be more then 4 chars or less then 15")
        return data