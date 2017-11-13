from user.views import UserBoxView, UserProfileCreateView, UserProfileView
from django.conf.urls import url
# from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', UserProfileCreateView.as_view(),
        name='registration'),
    url(r'^(?P<username>\w+)$', UserProfileView.as_view(),
        name='profile'),
    url(r'^(?P<username>\w+)/send_message$', UserProfileView.new_message,
        name='send_message'),
    url(r'^(?P<username>\w+)/delete_message/(?P<message_pk>[0-9]+)$',
        UserProfileView.delete_published_message,
        name='delete_published_message'),
    url(r'^(?P<username>\w+)/new_response/(?P<message_pk>[0-9]+)$',
        UserProfileView.new_response,
        name='new_response'),
    url(r'^(?P<username>\w+)/delete_response/(?P<response_pk>[0-9]+)$',
        UserProfileView.delete_response,
        name='delete_response'),
    url(r'^(?P<username>\w+)/box$', UserBoxView.as_view(),
        name='box'),
    url(r'^(?P<username>\w+)/box/delete_message/(?P<message_pk>[0-9]+)$',
        UserBoxView.delete_box_message,
        name='delete_box_message'),
    url(r'^(?P<username>\w+)/box/publish_message/(?P<message_pk>[0-9]+)$',
        UserBoxView.publish_message,
        name='publish_message'),
]
