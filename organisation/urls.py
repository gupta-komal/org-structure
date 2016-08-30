from django.conf.urls import url, patterns

urlpatterns = patterns(
    'organisation.views',
    url(r'^$', 'home'),
    url(r'^api/org/$', 'organisation_details', name='organisation'),
    url(r'^api/user/$', 'user_list', name='user'),
)
