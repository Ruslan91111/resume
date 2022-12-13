from rest_framework.serializers import ModelSerializer

from .models import Movies


class MoviesSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'




# Comment Profile Category Staff UserMovieRelations