from django.conf.urls.defaults import *
from satchmo_store.urls import urlpatterns as storepatterns
from l10n.urls import urlpatterns as l10npatterns

urlpatterns = storepatterns + l10npatterns
