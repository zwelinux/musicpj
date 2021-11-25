from django.urls import path 
from .import views 

app_name = 'musicapp'

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('<slug:artist_slug>/', views.song_list, name='song_list_by_artist'),
    path('artists/all', views.artists, name='artists'),
    path('artists/<str:name>/', views.artist_songs, name='artist_songs'),
    path('<int:id>/<slug:slug>/', views.song_detail, name='song_detail'),
    path('playlists/all', views.playlists, name='playlists'),
    path('playlists/<str:name>/', views.playlist_songs, name='playlist_songs'),
    path('albums/all', views.albums, name='albums'),
    path('albums/<str:name>/', views.album_songs, name='album_songs'),
]