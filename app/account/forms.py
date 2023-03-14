import uuid

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class UserSignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2'
        )

    '''
    1. validation
    2. save
    '''

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError('Passwords should match!')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)  # User(...)
        password = self.cleaned_data['password1']
        # user.password = password -> WRONG
        user.is_active = False
        user.username = uuid.uuid4()
        user.set_password(password)
        user.save()  # send request to db

        self._send_email()

        return user

    def _send_email(self):
        from django.core.mail import send_mail
        subject = 'Thank you for sign up!'
        path = reverse('account:activate', args=(self.instance.username,))
        message = f'''
            {settings.HTTP_SCHEMA}://{settings.HOST}{path}
        '''
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [self.instance.email],
            fail_silently=False,
        )
