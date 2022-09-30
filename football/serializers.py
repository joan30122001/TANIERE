from rest_framework import serializers 
from .models import Category, Product, Event, Article, News, PostTweet, Favorite, Like, KeyWord
# from .models import Competition, Match, Team, MatchTeam
from rest_framework.serializers import SerializerMethodField
import datetime
from django.contrib.auth.models import User



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class CategoryRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return CategorySerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)



class ProductSerializer(serializers.ModelSerializer):
    category = CategoryRelatedField(queryset=Category.objects.all(), many=False)
    class Meta:
        model = Product
        fields = [
                    'id',
                    'name',
                    'description',
                    'price',
                    'image',
                    'status',
                    'reduction',
                    'created_at',
                    'updated_at',
                    'category',
                ]



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"



# class CompetitionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Competition
#         fields = "__all__"



# class CompetitionRelatedField(serializers.RelatedField):
#     def to_representation(self, instance):
#         return FiliereSerializer(instance).data

#     def to_internal_value(self, data):
#         return self.queryset.get(pk=data)



# class MatchSerializer(serializers.ModelSerializer):
#     competition = CompetitionRelatedField(queryset=Competition.objects.all(), many=False)
#     class Meta:
#         model = Match
#         fields = [
#                     'score1',
#                     'score2',
#                     'day',
#                     'time',
#                     'competition',
#                 ]



# class MatchRelatedField(serializers.RelatedField):
#     def to_representation(self, instance):
#         return FiliereSerializer(instance).data

#     def to_internal_value(self, data):
#         return self.queryset.get(pk=data)



# class TeamSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Team
#         fields = "__all__"



# class TeamRelatedField(serializers.RelatedField):
#     def to_representation(self, instance):
#         return FiliereSerializer(instance).data

#     def to_internal_value(self, data):
#         return self.queryset.get(pk=data)



# class MatchTeamSerializer(serializers.ModelSerializer):
#     match = MatchRelatedField(queryset=Match.objects.all(), many=True)
#     team = TeamRelatedField(queryset=Team.objects.all(), many=True)
#     class Meta:
#         model = MatchTeam
#         fields = [
#                     'match',
#                     'team',
#                 ]



class KeyWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = "__all__"



class KeyWordRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return KeyWordSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)



class ArticleSerializer(serializers.ModelSerializer):
    key_words = KeyWordRelatedField(queryset=KeyWord.objects.all(), many=True)
    class Meta:
        model = Article
        fields = "__all__"



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"



class PostTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTweet
        fields = "__all__"
    


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = [
                    'id',
                    'type',
                    'user',
                ]



class LikeSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    class Meta:
        model = Like
        fields = ('id', 'user', 'article')



class UserSerializer(serializers.ModelSerializer):
    """
    serializer for user that serialize :
    ('id', 'username', 'first_name', 'last_name', 'email', 'image',
    'is_staff', 'is_active', 'is_superuser')\nbased on default 'User' model

    """

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'image',
            'is_staff', 'is_active', 'is_superuser')

    image = serializers.ImageField(source='profile.image', required=False)