from rest_framework.generics import ListAPIView

from .models import Video
from .serializers import VideoSerializer


class VideoListView(ListAPIView):
    queryset = Video.objects.all().order_by('-published_datetime')
    serializer_class = VideoSerializer
