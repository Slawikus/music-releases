from django.urls import path
from playlists import views


urlpatterns = [
	path("", views.PlaylistListView.as_view(), name="playlist_list"),
	path("create/", views.PlaylistCreateView.as_view(), name="playlist_create"),
	path("<int:pk>/detail", views.ShowPlaylistView.as_view(), name="playlist_show")
]