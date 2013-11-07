from rest_framework import serializers
from posts.models import Post
<<<<<<< HEAD


class PostSerializer(serializers.HyperlinkedModelSerializer):
=======
from tags.serializers import TagSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.Field(source='author.username')
    tags_details = TagSerializer(source='tags', read_only=True)
>>>>>>> master
    api_url = serializers.SerializerMethodField('get_api_url')

    class Meta:
        model = Post
<<<<<<< HEAD
        fields = ('id', 'title', 'description', 'created_on', 'url', 'api_url')
=======
        fields = ('id', 'title', 'description', 'created_on', 'author', 'tags',
                  'tags_details', 'url', 'api_url')
>>>>>>> master
        read_only_fields = ('id', 'created_on')

    def get_api_url(self, obj):
        return "#/post/%s" % obj.id
