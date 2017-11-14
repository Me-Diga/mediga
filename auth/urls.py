from auth.views import UserLoginView, UserLogoutView
from django.conf.urls import url
# from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^login/$', UserLoginView.as_view(),
        name='login'),
    url(r'^logout/$', UserLogoutView.as_view(),
        name='logout'),
]
