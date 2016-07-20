from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from osgeo_importer.urls import urlpatterns as importer_urlpatterns
from tastypie.api import Api
from geonode.urls import *


importer_api = Api(api_name='importer-api')
#importer_api.register(UploadedLayerResource())

urlpatterns = patterns('',
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
   url(
        r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('img/favicon.ico'),
            permanent=False),
        name="favicon"
    ),
    (r'^djmp/', include('djmp.urls')),
    url(r'^mvt_example$',
        TemplateView.as_view(template_name='open-layers-example.html'),
        name='mvt_example'),
) + urlpatterns

urlpatterns += patterns("",
                        url(r'', include(importer_api.urls)))

urlpatterns += importer_urlpatterns
