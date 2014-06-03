rom django.db import models

class Playlist(models.Model):
    title = models.CharField(max_length=512)
    fanart_url = models.CharField(max_length=256, blank=True)
    thumbnail_url = models.CharField(max_length=256, blank=True)

class Picture(models.Model):
    playlist = models.ForeignKey(Playlist)
    md5sum = models.CharField(max_length=256)
    file_url = models.CharField(max_length=256)
    title = models.CharField(max_length=512)
    fanart_url = models.CharField(max_length=256, blank=True)
    thumbnail_url = models.CharField(max_length=256, blank=True)

class Video(models.Model):
    playlist = models.ForeignKey(Playlist)
    md5sum = models.CharField(max_length=256)
    file_url = models.CharField(max_length=256)
    title = models.CharField(max_length=512)
    fanart_url = models.CharField(max_length=256, blank=True)
    thumbnail_url = models.CharField(max_length=256, blank=True)

class XBMCNode(models.Model):
    name = models.CharField(max_length=512)
    address = models.GenericIPAddressField()
    port = models.IntegerField()
    username = models.CharField(max_length=512, blank=True)
    password = models.CharField(max_length=512, blank=True)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

