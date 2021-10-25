from django.urls import path
from release_collections import views


urlpatterns = [
	path("", views.CollectionListView.as_view(), name="collection_list"),
	path("create/", views.CollectionCreateView.as_view(), name="collection_create"),
	path("<int:pk>/detail", views.ShowCollectionView.as_view(), name="collection_show")
]