from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Track, Genre
from django.db.models import Q
# Create your views here.
def index(request):
	return render(request, 'greedymusic/index.html')

def tracks(request,pno):
	track_list = Track.objects.order_by('id')
	for track in track_list:
		track.remaining = range(5-track.rating)
		track.rating = range(track.rating)
	if(len(track_list)%5==0):
		pages = len(track_list)/5
	else:
		pages = len(track_list)/5 + 1
	pno = int(pno)
	l = []
	if((pno-1)*5+5 > len(track_list)):
		for i in range((pno-1)*5, len(track_list)):
			l.append(track_list[i])	
	else:
		for i in range((pno-1)*5,(pno-1)*5 + 5):
			l.append(track_list[i])
	


	return render(request, 'greedymusic/tracks.html', {'track_list':l,'pages':range(1,pages+1)})

def detailTrack(request, track_id):
	t = Track.objects.get(pk=track_id)
	t.remaining = range(5-t.rating)
	t.rating = range(t.rating)
	return render(request, 'greedymusic/track.html', {'track':t})

def editTrack(request, track_id):
	q = Track.objects.get(pk=track_id)
	return render(request, 'greedymusic/editTrack.html', {'id':track_id,'title':q.title,'genre':q.genre,'rating':q.rating})

def submitEdit(request,track_id):
	if request.method=='POST':
		title = request.POST['title']
		genre = request.POST['genre']
		rating = request.POST['rating']
		t = Track.objects.get(pk=track_id)
		t.title = title
		genres = genre.split(",")
		t.genre = " | ".join(genres)
		t.rating = rating
		t.save()

		for gen in genres:
			ge = Genre.objects.filter(genre_name  = gen)
			if(len(ge)==0):
				g = Genre(genre_name=genre)
				g.save()


		track_list = Track.objects.order_by('id')
		for track in track_list:
			track.remaining = range(5-track.rating)
			track.rating = range(track.rating)
		return render(request, 'greedymusic/tracks.html', {'track_list':track_list})

def search(request):
	keyword = request.POST['keyword']
	results = Track.objects.filter(Q(title__icontains=keyword) | Q(genre__icontains=keyword)).order_by('id')
	for track in results:
		track.remaining = range(5-track.rating)
		track.rating = range(track.rating)
	return render(request, 'greedymusic/search.html', {'track_list':results}) 

def addTrack(request):
	return render(request, 'greedymusic/addTrack.html')

def submitAdd(request):
	if request.method == 'POST':
		title = request.POST['title']
		genre = request.POST['genre']
		rating = request.POST['rating']
		genres = genre.split(",")
		genre = " | ".join(genres)
		t = Track(title=title, genre=genre, rating=rating)
		t.save()

		for gen in genres:
			ge = Genre.objects.filter(genre_name  = gen)
			if(len(ge)==0):
				g = Genre(genre_name=gen)
				g.save()
				
		track_list = Track.objects.order_by('id')
		for track in track_list:
			track.remaining = range(5-track.rating)
			track.rating = range(track.rating)
		return render(request, 'greedymusic/tracks.html', {'track_list':track_list})



def addGenre(request):
	return render(request, 'greedymusic/addGenre.html')

def submitGenreAdd(request):
	if request.method == 'POST':
		name = request.POST['name']
		g = Genre(genre_name=name)
		g.save()
		genre_list = Genre.objects.order_by('id')
		return render(request, 'greedymusic/genres.html', {'genre_list':genre_list})

def submitGenreEdit(request,genre_id):
	if request.method == 'POST':
		name = request.POST['name']
		g = Genre.objects.get(pk=genre_id)
		cgname = g.genre_name
		g.genre_name = name
		g.save()
		track_list = Track.objects.all()
		for t in track_list:
			tgenre = t.genre.split(" | ")
			for i in range(0,len(tgenre)):
				if(tgenre[i]==cgname):
					tgenre[i] = name
			t.genre = " | ".join(tgenre)
			t.save()
		genre_list = Genre.objects.order_by('id')
		return render(request, 'greedymusic/genres.html', {'genre_list':genre_list})

def genres(request):
	genre_list = Genre.objects.order_by('id')
	return render(request, 'greedymusic/genres.html', {'genre_list':genre_list})

def editGenre(request, genre_id):
	q = Genre.objects.get(pk=genre_id)
	return render(request, 'greedymusic/editGenre.html', {'id':genre_id,'genre_name':q.genre_name})

def detailGenre(request, genre_id):
	g = Genre.objects.get(pk=genre_id)
	glist = []
	glist.append(g)
	return render(request, 'greedymusic/genres.html', {'genre_list':glist})
