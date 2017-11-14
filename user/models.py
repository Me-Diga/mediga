from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='static/images/user/avatars/')
    unread_messages = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('Perfil de usuário')
        verbose_name_plural = _('Perfis de usuário')

    def __str__(self):
        return (self.user.username)
