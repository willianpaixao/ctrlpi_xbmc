from django.contrib import admin

from ctrlpi.models import Playlist, Video, XBMCNode

admin.site.register(Playlist)
admin.site.register(Video)
admin.site.register(XBMCNode)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

