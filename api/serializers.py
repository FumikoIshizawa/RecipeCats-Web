from rest_framework import serializers

from api.models import Recipe, Category

class RecipeSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	title = serializers.CharField(max_length=100)
	url = serializers.URLField()
	category = serializers.IntegerField(default=0)

	def create(self, validated_data):
		return Recipe.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.url = validated_data.get('url', instance.url)
		instance.category = validated_data.get('category', instance.category)
		instance.save()
		
		return instance
