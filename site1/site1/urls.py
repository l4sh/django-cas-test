"""site1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django_cas_ng import views as cas_ng_views

urlpatterns = [
    # CAS
    url(r'^admin/login/$', cas_ng_views.login, name='cas_ng_login'),
    url(r'^admin/logout/$', cas_ng_views.logout, name='cas_ng_logout'),
    url(r'^admin/callback/$', cas_ng_views.callback, name='cas_ng_proxy_callback'),

    # Admin
    url(r'^admin/', admin.site.urls),
]
