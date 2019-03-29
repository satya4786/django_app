# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Movie 
import pdb

# Create your views here.

def test(request):
    movies=Movie.objects.all()
    #output=','.join([m.tittle for m in movies])
    return render(request,'movies/index.html',{'movies':movies})
    #return HttpResponse(output)

def detail(request,movie_id):
    movies=get_object_or_404(Movie,pk=movie_id)
    return render(request,'movies/detail.html', {'movie':movies})
    # return HttpResponse(movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404()