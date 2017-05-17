from django.conf.urls import url
from .views import IndexView, ProView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^album/$', ProView.as_view(), name='albumes'),
    url(r'^album/(?P<album>[-\w]+)/$', ProView.as_view(), name='in_albums'),
    # url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
]