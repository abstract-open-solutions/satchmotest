from django.conf import settings
from django.conf.urls.defaults import patterns, url
from satchmo_store.urls import urlpatterns as storepatterns
from l10n.urls import urlpatterns as l10npatterns


urlpatterns = storepatterns + l10npatterns


if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(
            r'^%s/(?P<path>.*)$' % settings.STATIC_URL.strip('/'),
            'django.views.static.serve',
            {
                'document_root': settings.STATIC_ROOT,
            }
        )
    )
