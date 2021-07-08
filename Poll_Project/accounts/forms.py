from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, min_length=5, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username'}))
    email = forms.EmailField(label='Email', max_length=100, min_length=5, required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='Password', max_length=100, min_length=5, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(label='Confirm Password', max_length=100, min_length=5, required=True,
                                       widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password Again'}))


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, min_length=5, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username'}))
    password = forms.CharField(label='Password', max_length=100, min_length=5, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

