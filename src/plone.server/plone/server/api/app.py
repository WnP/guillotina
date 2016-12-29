# -*- coding: utf-8 -*-
from plone.server import app_settings
from plone.server.configure import service
from plone.server.interfaces import IApplication
from plone.server.json.interfaces import IResourceSerializeToJson
from zope.component import getMultiAdapter

import logging


logger = logging.getLogger(__name__)


@service(context=IApplication, method='GET', permission='plone.AccessContent')
async def get(context, request):
    serializer = getMultiAdapter(
        (context, request),
        IResourceSerializeToJson)
    return serializer()


@service(context=IApplication, method='GET', permission='plone.GetPortals',
         name='@apidefinition')
async def get_api_definition(context, request):
    return app_settings['api_definition']
