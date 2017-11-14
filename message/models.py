from user.models import UserProfile
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    body = models.TextField(max_length=300)
    author = models.ForeignKey(
        UserProfile, related_name='sended_messages',
        on_delete=models.CASCADE, null=True
    )
    receiver = models.ForeignKey(
        UserProfile, related_name='received_messages',
        on_delete=models.CASCADE
    )
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Mensagem')
        verbose_name_plural = _('Mensagens')

    def __str__(self):
        return (self.body)


class Response(models.Model):
    body = models.TextField(max_length=300)
    author = models.ForeignKey(
        UserProfile, related_name='sended_responses',
        on_delete=models.CASCADE
    )
    message = models.ForeignKey(
        Message, related_name='received_responses',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Resposta')
        verbose_name_plural = _('Respostas')

    def __str__(self):
        return (self.body)
