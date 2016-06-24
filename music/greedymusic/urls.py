from django.conf.urls import url

from . import views


app_name = "greedymusic"
urlpatterns = [
				url(r'^$', views.index, name='index'),
				url(r'^track/(?P<track_id>[0-9]+)/$', views.detailTrack,name='detailTrack'),
				url(r'^tracks/(?P<pno>[0-9]+)/$', views.tracks, name='tracks'),
				url(r'^search/$', views.search,name='search'),
				url(r'^editTrack/(?P<track_id>[0-9]+)/$', views.editTrack,name='editTrack'),
				url(r'^addTrack/$', views.addTrack,name='addTrack'),
				url(r'^submitAdd/$', views.submitAdd,name='submitAdd'),
				url(r'^submitEdit/(?P<track_id>[0-9]+)/$', views.submitEdit,name='submitEdit'),
				url(r'^genres/$', views.genres, name='genres'),
				url(r'^editGenre/(?P<genre_id>[0-9]+)/$', views.editGenre,name='editGenre'),
				url(r'^addGenre/$', views.addGenre,name='addGenre'),
				url(r'^submitGenreAdd/$', views.submitGenreAdd,name='submitGenreAdd'),
				url(r'^submitGenreEdit/(?P<genre_id>[0-9]+)/$', views.submitGenreEdit,name='submitGenreEdit'),
				url(r'^genres/(?P<genre_id>[0-9]+)/$', views.detailGenre,name='detailGenre'),

			  ]