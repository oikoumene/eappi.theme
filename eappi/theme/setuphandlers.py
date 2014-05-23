from collective.grok import gs
from eappi.theme import MessageFactory as _

@gs.importstep(
    name=u'eappi.theme', 
    title=_('eappi.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('eappi.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
