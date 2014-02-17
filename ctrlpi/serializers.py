from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ctrlpi.models import Playlist, Video, XBMCNode

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "username", "first_name", "last_name", "email",
        "groups", "is_staff", "is_active")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("url", "name")

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = ("title", "fanart_url", "thumbnail_url")

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ("url", "playlist", "md5sum", "file_url", "title",
                "fanart_url", "thumbnail_url")

class XBMCNodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = XBMCNode
        fields = ('url', 'name', 'address', 'port', 'username', 'password')

