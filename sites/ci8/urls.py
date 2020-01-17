from django.conf.urls import url
from ci8 import views

urlpatterns = [
    url(r'^%s$' % views.home_page['path'], views.index),
    url(r'^%s$' % views.about_me_page['path'], views.about_me),
    url(r'^%s$' % views.haier_t32x_page['path'], views.haier_t32x),
    url(r'^%s$' % views.digipass_go_6_page['path'], views.digipass_go_6),
    url(r'^%s$' % views.multiple_choice_test_omr_page['path'], views.multiple_choice_test_omr),
    url(r'^%s$' % views.mod_wsgi_error_page['path'], views.mod_wsgi_error),
    url(r'^%s$' % views.tags_page['path'], views.tags),
    url(r'^%s$' % views.cookies_policy_page['path'], views.cookies_policy),
    url(r'^sitemap.xml$', views.sitemap),
]
