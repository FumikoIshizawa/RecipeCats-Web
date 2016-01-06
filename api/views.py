from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Recipe

@api_view(['GET', 'POST'])
def add(request):
	if request.method == 'GET':
		contents = {
			'title': 'This is Recipe',
			'url': 'urlurlurl',
		}
		return Response(contents)
	if request.method == 'POST':
		title = 'Recipe1'
		url = 'url1url1'
		recipe = Recipe(title=title, url=url)
		recipe.save()
		return Response(contents)
