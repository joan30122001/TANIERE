import datetime
from django.shortcuts import render
from .models import Category, Product, Event, Article, News, PostTweet, Favorite, Like, KeyWord
from django.contrib.auth.models import User
# from .models import Competition, Match, Team, MatchTeam
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer, EventSerializer, ArticleSerializer, NewsSerializer, PostTweetSerializer, FavoriteSerializer, LikeSerializer, UserSerializer, KeyWordSerializer
# from .serializers import CompetitionSerializer, MatchSerializer, TeamSerializer, MatchTeamSerializer, 
from rest_framework.generics import GenericAPIView
from rest_framework import exceptions, status, generics, mixins, viewsets, permissions, serializers
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from django.http import HttpResponse
from rolepermissions.mixins import HasRoleMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
# from django_filters import rest_framework as filters




class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        category = Category.objects.get(id=pk)
        category.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class ProductViewSet(viewsets.ViewSet):
    
    def list(self, request):
        serializer = ProductSerializer(Product.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class EventViewSet(viewsets.ViewSet):
    
    def list(self, request):
        serializer = EventSerializer(Event.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(event)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(instance=event, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        event = Event.objects.get(id=pk)
        event.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



# class CompetitionViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         serializer = CompetitionSerializer(Competition.objects.all(), many=True)
#         return Response({
#             'data': serializer.data
#         })

#     def retrieve(self, request, pk=None):
#         competition = Competition.objects.get(id=pk)
#         serializer = CompetitionSerializer(competition)
#         return Response({
#             'data': serializer.data
#         })

#     def create(self, request):
#         serializer = CompetitionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'data': serializer.data
#         }, status=status.HTTP_201_CREATED)

#     def update(self, request, pk=None):
#         competition = Competition.objects.get(id=pk)
#         serializer = CompetitionSerializer(instance=competition, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

#     def destroy(self, request, pk=None):
#         competition = Competition.objects.get(id=pk)
#         competition.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)



# class MatchViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         serializer = MatchSerializer(Match.objects.all(), many=True)
#         return Response({
#             'data': serializer.data
#         })

#     def retrieve(self, request, pk=None):
#         match = Match.objects.get(id=pk)
#         serializer = MatchSerializer(match)
#         return Response({
#             'data': serializer.data
#         })

#     def create(self, request):
#         serializer = MatchSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'data': serializer.data
#         }, status=status.HTTP_201_CREATED)

#     def update(self, request, pk=None):
#         match = Match.objects.get(id=pk)
#         serializer = MatchSerializer(instance=match, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

#     def destroy(self, request, pk=None):
#         match = Match.objects.get(id=pk)
#         match.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)



# class TeamViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         serializer = TeamSerializer(Team.objects.all(), many=True)
#         return Response({
#             'data': serializer.data
#         })

#     def retrieve(self, request, pk=None):
#         team = Team.objects.get(id=pk)
#         serializer = TeamSerializer(team)
#         return Response({
#             'data': serializer.data
#         })

#     def create(self, request):
#         serializer = TeamSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'data': serializer.data
#         }, status=status.HTTP_201_CREATED)

#     def update(self, request, pk=None):
#         team = Team.objects.get(id=pk)
#         serializer = TeamSerializer(instance=team, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

#     def destroy(self, request, pk=None):
#         team = Team.objects.get(id=pk)
#         team.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)



# class MatchTeamViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         serializer = MatchTeamSerializer(MatchTeam.objects.all(), many=True)
#         return Response({
#             'data': serializer.data
#         })

#     def retrieve(self, request, pk=None):
#         matchteam = MatchTeam.objects.get(id=pk)
#         serializer = MatchTeamSerializer(matchteam)
#         return Response({
#             'data': serializer.data
#         })

#     def create(self, request):
#         serializer = MatchTeamSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'data': serializer.data
#         }, status=status.HTTP_201_CREATED)

#     def update(self, request, pk=None):
#         matchteam = MatchTeam.objects.get(id=pk)
#         serializer = MatchTeamSerializer(instance=matchteam, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

#     def destroy(self, request, pk=None):
#         matchteam = MatchTeam.objects.get(id=pk)
#         matchteam.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)



class KeyWordViewSet(viewsets.ViewSet):
    
    def list(self, request):
        serializer = KeyWordSerializer(KeyWord.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        keyword = KeyWord.objects.get(id=pk)
        serializer = KeyWordSerializer(keyword)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = KeyWordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        keyword = KeyWord.objects.get(id=pk)
        serializer = KeyWordSerializer(instance=keyword, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        keyword = KeyWord.objects.get(id=pk)
        keyword.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class ArticleViewSet(viewsets.ViewSet):
    
    def list(self, request):
        search_fields = ['name' ,'key_words', 'author', 'created_at']
        filter_backends = (filters.SearchFilter,)
        serializer = ArticleSerializer(Article.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(article)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(instance=article, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        article = Article.objects.get(id=pk)
        article.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['=name', '=key_words__name', 'author__username']
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('id', 'name', 'key_words__name', 'author__username')



class NewsViewSet(viewsets.ViewSet):
    
    def list(self, request):
        serializer = NewsSerializer(News.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        news = News.objects.get(id=pk)
        serializer = NewsSerializer(news)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        news = News.objects.get(id=pk)
        serializer = NewsSerializer(instance=news, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        news = News.objects.get(id=pk)
        news.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class PostTweetViewSet(viewsets.ViewSet):
    
    def list(self, request):
        serializer = PostTweetSerializer(PostTweet.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        posttweet = PostTweet.objects.get(id=pk)
        serializer = PostTweetSerializer(posttweet)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = PostTweetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        posttweet = PostTweet.objects.get(id=pk)
        serializer = PostTweetSerializer(instance=posttweet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        posttweet = PostTweet.objects.get(id=pk)
        posttweet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class FavoriteList(generics.ListCreateAPIView):
    """List all favorites"""
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    permission_classes = [IsAuthenticated]

    def pre_save(self, obj):
        obj.owner = self.request.user


class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    """List only authenticated user's favorites"""
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    permission_classes = [IsAuthenticated]

    def pre_save(self, obj):
        obj.owner = self.request.user



class LikeCreate(HasRoleMixin ,generics.CreateAPIView):
    allowed_roles='user'
    queryset=Like.objects.all()
    serializer_class=LikeSerializer



class DisLIke(generics.DestroyAPIView):
    allowed_role='user'
    queryset=Like.objects.all()
    serializer_class=LikeSerializer



class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]