from django.shortcuts import render
from .models import youtube_video
# Create your views here.
def home(request):
    video = youtube_video.objects.all()
    return render(request, 'home.html', {'videos': video})
