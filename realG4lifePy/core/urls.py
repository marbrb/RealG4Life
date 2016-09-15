from django.conf.urls import url
from core.views import home, node_api, logout_view, loginWithForm

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^node_api/$', node_api, name='node_api'),
    url(r'^login/$', loginWithForm, name='login'),
    url(r'^logout/$', logout_view, name='logout')


]
