from django.db import models

from ctrlpi_xbmc.client import System

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

class Node(models.Model):
    name = models.CharField(max_length=512)
    address = models.GenericIPAddressField()
    port = models.IntegerField()
    mac = models.CharField(max_length=32)
    username = models.CharField(max_length=512, blank=True)
    password = models.CharField(max_length=512, blank=True)

    def __unicode__(self):
            return self.name

    def get_header(self):
        data = {}
        data["headers"] = {"content-type": "application/json"}
        data["payload"] = {"jsonrpc": "2.0", "id": 1}
        data["url"] = "http://" + self.address + ":" + str(self.port) + "/jsonrpc"
        return data
        
    def get_tasks(self):
        r = System(self.get_header())
        s = r.get_tasks()
        return s

    def get_uptime(self):
        r = System(self.get_header())
        s = r.get_uptime()
        return s

    def ping(self):
        r = System(self.get_header())
        s = r.ping()
        return s

    def hibernate(self):
        r = System(self.get_header())
        s = r.hibernate()
        return s

    def reboot(self):
        r = System(self.get_header())
        s = r.reboot()
        return s

    def shutdown(self):
        r = System(self.get_header())
        s = r.shutdown()
        return s

    def suspend(self):
        r = System(self.get_header())
        s = r.suspend()
        return s

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

