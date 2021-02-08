from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *
from django.db.models import Q
from  django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AddPhotoForm, AlbumForm
# from .forms import ImageUploadForm
# Create your views here.

def gallery(request):
    photos = Photos.objects.all()
    album = Album.objects.all()
    falbum = Album.objects.order_by('id').first()
    myform = AddPhotoForm()
    if request.method == 'POST':
        myform = AlbumForm(request.POST)
        if myform.is_valid():
            myform.save(commit=True)
            messages.success(request, 'Album Created successfully')
            return HttpResponseRedirect('/')
    diction = {'photos':photos, 'album':album, 'falbum':falbum, 'myform':myform }
    return render(request, 'gallery/index.html', context=diction)

def albums(request, id):
    photos = Photos.objects.all()
    photosal = Photos.objects.filter(album=id)
    this_album  = Album.objects.get(pk=id)
    album = Album.objects.all()
    falbum = Album.objects.order_by('id').first()
    myform = AddPhotoForm()
    if request.method == 'POST':
        myform = AlbumForm(request.POST)
        if myform.is_valid():
            myform.save(commit=True)
            messages.success(request, 'Album Created successfully')
            return HttpResponseRedirect('/')

    diction = {'photos':photos, 'album':album, 'falbum':falbum, 'photosal':photosal, 'this_album':this_album, 'myform':myform }
    return render(request, 'gallery/albums.html', context=diction)


def add_photo(request):
    if request.method == 'POST':
        myform = AddPhotoForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save(commit=True)
            messages.success(request, 'Photo added successfully')
            return HttpResponseRedirect('/')

        else:
            messages.success(request, 'Something Missing')
            return HttpResponseRedirect('/')
    else:
        myform = AddPhotoForm()
        return HttpResponseRedirect('/')


def add_photo_from_album(request, id):
    id =str(id)
    if request.method == 'POST':
        myform = AddPhotoForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save(commit=True)
            messages.success(request, 'Photo added successfully')
            return HttpResponseRedirect('/albums/'+id+'/')
        else:
            messages.success(request, 'Something Missing')
            return HttpResponseRedirect('/albums/'+id+'/')
    else:
        myform = AddPhotoForm()
        return HttpResponseRedirect('/albums/'+id+'/')



def delete_album(request, id):
    if request.method == 'POST':
        del_id = Album.objects.get(pk = id)
        del_id.delete()
        return redirect('gallery')

def delete_photos(request, id):
    if request.method == 'POST':
        del_id = Photos.objects.get(pk = id)
        del_id.delete()
        return redirect('gallery')



def delete_photos_from_album(request, id):
    if request.method == 'POST':
        del_id = Photos.objects.get(pk = id)
        album_id  = del_id.album.id
        del_id.delete()
        album_id = str(album_id)
        return HttpResponseRedirect('/albums/'+album_id+'/')