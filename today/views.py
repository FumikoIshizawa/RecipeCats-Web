from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import urllib.request

from api.models import Recipe

def today_recipe(request):
	return HttpResponse("Success")
	