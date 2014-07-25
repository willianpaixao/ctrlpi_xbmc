from django.contrib import admin

from ctrlpi_xbmc.models import Playlist, Video, Node

admin.site.register(Playlist)
admin.site.register(Video)
admin.site.register(Node)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

