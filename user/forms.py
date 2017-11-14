from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _


class UserProfileCreateForm(forms.ModelForm):
    """
    Class for User registration form.
    """
    username = forms.CharField(label=_("Nome de usuário"))
    first_name = forms.CharField(label=_("Nome"))
    last_name = forms.CharField(label=_("Sobrenome"))
    email = forms.CharField(label=_("E-mail"), validators=[validate_email])
    password = forms.CharField(label=_("Senha"), widget=forms.PasswordInput)
    password_validation = forms.\
        CharField(label=_("Confirmação de senha"), widget=forms.PasswordInput)
    avatar = forms.ImageField(label=_("Avatar"))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password', 'avatar']

    def clean(self):
        cleaned_data = super(UserProfileCreateForm, self).clean()

        # Password validation
        password = cleaned_data.get('password')
        password_validation = cleaned_data.get('password_validation')

        password_error_message = _("A senha deve ser igual à confirmação \
de senha.")
        if password and password_validation:
            if password != password_validation:
                password_error = forms.ValidationError(password_error_message)
                self.add_error('password', password_error)

        # Username UNIQUE constraint validation
        username = cleaned_data.get('username')

        username_error_message = _("Este nome de usuário não está disponível.")
        if User.objects.filter(username=username).exists():
            raise ValidationError(username_error_message)

        return cleaned_data
