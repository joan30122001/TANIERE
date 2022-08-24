from rest_framework import serializers 
from .models import Category, Product, Event, Competition, Match, Team, MatchTeam, Article, News, PostTweet, Favorite, Like
from rest_framework.serializers import SerializerMethodField
import datetime
from users.models import CustomUser
from users.serializers import UserSerializer



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class CategoryRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return FiliereSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)



class ProductSerializer(serializers.ModelSerializer):
    category = CategoryRelatedField(queryset=Category.objects.all(), many=False)
    class Meta:
        model = Product
        fields = [
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



class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = "__all__"



class CompetitionRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return FiliereSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)



class MatchSerializer(serializers.ModelSerializer):
    competition = CompetitionRelatedField(queryset=Competition.objects.all(), many=False)
    class Meta:
        model = Match
        fields = [
                    'score1',
                    'score2',
                    'day',
                    'time',
                    'competition',
                ]



class MatchRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return FiliereSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)



class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"



class TeamRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return FiliereSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)



class MatchTeamSerializer(serializers.ModelSerializer):
    match = MatchRelatedField(queryset=Match.objects.all(), many=True)
    team = TeamRelatedField(queryset=Team.objects.all(), many=True)
    class Meta:
        model = MatchTeam
        fields = [
                    'match',
                    'team',
                ]



class ArticleSerializer(serializers.ModelSerializer):
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
                    'type',
                    'user',
                ]



class LikeSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    class Meta:
        model = Like
        fields = ('id', 'user', 'article')