from django.http import StreamingHttpResponse
from .services import open_file
from django.shortcuts import render, get_object_or_404
from .models import Video



def get_list_video(request): # шаблон для загрузки всех видеофайлов
    return render(request, 'video_hosting/home.html', {'video_list': Video.objects.all()})


def get_video(request, pk: int):  # приёмка нашего айди с видео
    _video = get_object_or_404(Video, id=pk) # 404 если видео не существует
    return render(request, "video_hosting/video.html", {"video": _video})

def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response
