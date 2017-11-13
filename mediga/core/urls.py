from django.conf.urls import url
# from django.contrib.auth.decorators import login_required
from .views import HomepageView, SearchView


urlpatterns = [
    url(r'^$', HomepageView.as_view(),
        name='homepage'),
    url(r'^busca$', SearchView.as_view(),
        name='search'),
]
