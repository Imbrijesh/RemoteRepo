from django import forms
class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label="Enter Your First Name",
        widget=forms.TextInput(
            attrs={
                  'class':'form-control',
                  'placeholder':'Your First Name'
            }
        )
    )

    last_name=forms.CharField(
    label="Enter Your Last Name",
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Your Last Name'
        }
    )
)
    username=forms.CharField(
    label="Enter Your Username",
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Your Username'
        }
    )
)
    password=forms.CharField(
    label="Enter Your Password",
    widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Your Password'
        }
    )
)
    email=forms.EmailField(
    label="Enter Your Email",
    widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'Your Email ID'
        }

    )
)
    mobile=forms.IntegerField(
    label="Enter Your Mobile Number",
    widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Your Mobile Number'
        }
    )
)
class LoginForm(forms.Form):
    username = forms.CharField(
        label="Enter Your Username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Username'
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Password'
            }
        )
    )