from django.db import models
from django.urls import reverse 

class Artist(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    gender = models.CharField(max_length=255, db_index=True, blank=True)
    region = models.CharField(max_length=255, db_index=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='artist_images', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'artist'
        verbose_name_plural = 'artists'

    def __str__(self):
        return self.name  

    def get_absolute_url(self):
        return reverse('musicapp:song_list_by_artist', args=[self.slug])


class Song(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True, related_name='main')
    artist_two = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True, related_name='featuring')
    slug = models.SlugField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='songs_images', blank=True)
    track = models.FileField(upload_to='songs', blank=True)
    lyrics = models.TextField(blank=True)
    date = models.DateField()

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('musicapp:song_detail', args=[self.id, self.slug])


class Album(models.Model):
    name = models.CharField(max_length=255, blank=True)
    artist = models.ManyToManyField(Artist, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='playlist_images', blank=True)
    tracks = models.ManyToManyField(Song, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'album'
        verbose_name_plural = 'albums'

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='playlist_images', blank=True)
    tracks = models.ManyToManyField(Song)

    class Meta:
        ordering = ('name',)
        verbose_name = 'playlist'
        verbose_name_plural = 'playlists'

    def __str__(self):
        return self.name

