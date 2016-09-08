from django.conf.urls import url
from core.views import home, node_api

urlpatterns = [
    url(r'^$', home, name='home'),
        url(r'^node_api/$', node_api, name='node_api'),

]
