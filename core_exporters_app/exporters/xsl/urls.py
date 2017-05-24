""" XSLT exporter url
"""
from django.conf.urls import url
from views.admin import ajax as user_ajax


urlpatterns = [
    url(r'^add', user_ajax.add_xslt,
        name='core_exporters_app_exporters_xsl_selection'),
]
