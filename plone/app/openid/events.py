from zope.interface import implements

from Products.PluggableAuthService.events import PASEvent

from plone.app.openid.interfaces import IOpenIDUserLoggedInEvent

class OpenIDUserLoggedInEvent(PASEvent):
    implements(IOpenIDUserLoggedInEvent)

    def __init__(self, principal):
        super(OpenIDUserLoggedInEvent, self).__init__(principal)