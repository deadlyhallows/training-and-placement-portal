from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from resume import views as core_views
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^downloads/$', views.download, name='download'),
    url(r'^procedure/$', views.procedure, name='procedure'),
    url(r'^pdf/$', views.generate_view, name='pdf'),

    url(r'^resume/new/$', views.resume_new, name='resume_new'),

    url(r'^login/$', auth_views.LoginView.as_view(template_name='resume/login.html'), name='login'),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),




]

#if settings.DEBUG is False:
#urlpatterns += [url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), ]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)