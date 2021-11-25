from django.db.models.fields import SlugField
from django.shortcuts import get_object_or_404, render
from .models import Artist, Song, Playlist, Album
# Create your views here.

def song_list(request, artist_slug=None):
    artist = None
    artists = Artist.objects.all() 
    songs = Song.objects.all()
    playlists = Playlist.objects.all()
    albums = Album.objects.all()
    latest_songs = Song.objects.order_by('-date')[:5]

    if artist_slug:
        artist = get_object_or_404(Artist, slug=artist_slug)
        songs = songs.filter(artist=artist)
    
    context = {
        'artist' : artist,
        'artists' : artists,
        'songs' : songs,
        'playlists' : playlists,
        'albums' : albums,
        'latest_songs' : latest_songs
    }

    return render(request, 'musicapp/song/song_list.html', context)

def artists(request):
    artists = Artist.objects.all()
    context = {
        'artists' : artists,
    }
    return render(request, 'musicapp/song/artists.html', context)

def artist_songs(request, name):
    songs = Song.objects.filter(artist__name=name).distinct()
    context = {
        'name':name,
        'songs':songs
    }
    return render(request, 'musicapp/song/artist_songs.html', context)


def playlists(request):
    playlists = Playlist.objects.all()
    context = {
        'playlists':playlists
    }
    return render(request, 'musicapp/song/playlists.html', context)

def playlist_songs(request, name):
    songs = Song.objects.filter(playlist__name=name).distinct()
    context = {
        'name':name,
        'songs':songs
    }
    return render(request, 'musicapp/song/playlist_songs.html', context)

def albums(request):
    albums = Album.objects.all()
    context = {
        'albums':albums
    }
    return render(request, 'musicapp/song/albums.html', context)



def album_songs(request, name):
    songs = Song.objects.filter(album__name=name).distinct()
    context = {
        'name':name,
        'songs':songs
    }
    return render(request, 'musicapp/song/album_songs.html', context)


def song_detail(request, id, slug):
    song = get_object_or_404(Song, id=id, slug=slug)
    
    context = {
        'song' : song,
    }

    return render(request, 'musicapp/song/song_detail.html', context)
