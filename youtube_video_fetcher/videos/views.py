from rest_framework.generics import ListAPIView

from .models import Video
from .serializers import VideoSerializer


class VideoListView(ListAPIView):
    queryset = Video.objects.all().order_by('-published_datetime')
    serializer_class = VideoSerializer


class VideoSearchView(ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return Video.objects.filter(title__icontains=query) | Video.objects.filter(description__icontains=query)
