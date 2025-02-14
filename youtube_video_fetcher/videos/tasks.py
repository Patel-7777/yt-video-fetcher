import requests
from celery import shared_task
from django.utils.dateparse import parse_datetime

from videos.models import Video

# api key need to be stored in secret, but for the convenience directly assigning here.
YOUTUBE_API_KEYS = ['AIzaSyARRCkQhlTWec-4TZhsxM6PuqWrhGEKWuA', 'AIzaSyCI7wBKpUDIUJalCIi48xIWjg2osSJOmTU']
# keeping it static as mentioned in assignment document
SEARCH_QUERY = 'technology'


@shared_task(name="fetch_youtube_data")
def fetch_youtube_data():
    for api_key in YOUTUBE_API_KEYS:
        try:
            url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&order=date&q={SEARCH_QUERY}&type=video&key={api_key}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            for item in data['items']:
                Video.objects.get_or_create(
                    video_url=f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                    defaults={
                        'title': item['snippet']['title'],
                        'description': item['snippet']['description'],
                        'published_datetime': parse_datetime(item['snippet']['publishedAt']),
                        'thumbnail_url': item['snippet']['thumbnails']['high']['url'],
                    }
                )
            return
        except requests.exceptions.RequestException:
            print(f"API Key :{api_key} is exhausted!, Trying with new api key.")
            continue
    print("All API keys exhausted!")
