from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api.models import Recipe
from api.serializers import RecipeSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def add(request):
	if request.method == 'GET':
		recipe = Recipe.objects.get(id=2)
		serializer = RecipeSerializer(recipe)
		return Response(serializer.data)

	if request.method == 'POST':
		serializer = RecipeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)
