from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from ctrlpi.serializers import UserSerializer, GroupSerializer
from ctrlpi.serializers import PlaylistSerializer, VideoSerializer, XBMCNodeSerializer
from ctrlpi.models import Playlist, Video, XBMCNode

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed
    or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class XBMCNodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = XBMCNode.objects.all()
    serializer_class = XBMCNodeSerializer

