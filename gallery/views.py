from django.shortcuts import render, HttpResponseRedirect
from .models import *
from django.db.models import Q
from  django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from .forms import ImageUploadForm
# Create your views here.

def gallery(request):
    diction = {}
    return render(request, 'gallery/index.html', context=diction)