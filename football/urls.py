from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet, EventViewSet, ArticleViewSet, NewsViewSet, PostTweetViewSet, LikeCreate, DisLIke
# from .views import CompetitionViewSet, MatchViewSet, TeamViewSet, MatchTeamViewSet
from football import views
from rest_framework import routers




router = routers.DefaultRouter()
router.register('user', views.UserView)

urlpatterns = [
    path('', include(router.urls)),
    path("category" ,  CategoryViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('category/<str:pk>',  CategoryViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("product" , ProductViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('product/<str:pk>', ProductViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("event" , EventViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('event/<str:pk>', EventViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    # path("competition" , CompetitionViewSet.as_view({
    #     "get":"list",
    #     "post":"create"
    # })),
    # path('competition/<str:pk>', CompetitionViewSet.as_view({
    #     'get': "retrieve",
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
    # path("match" , MatchViewSet.as_view({
    #     "get":"list",
    #     "post":"create"
    # })),
    # path('match/<str:pk>', MatchViewSet.as_view({
    #     'get': "retrieve",
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
    # path("team" , TeamViewSet.as_view({
    #     "get":"list",
    #     "post":"create"
    # })),
    # path('team/<str:pk>', TeamViewSet.as_view({
    #     'get': "retrieve",
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
    # path("matchteam" , MatchTeamViewSet.as_view({
    #     "get":"list",
    #     "post":"create"
    # })),
    # path('matchteam/<str:pk>', MatchTeamViewSet.as_view({
    #     'get': "retrieve",
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
    path("article" , ArticleViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('article/<str:pk>', ArticleViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("news" , NewsViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('news/<str:pk>', NewsViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("posttweet" , PostTweetViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('posttweet/<str:pk>', PostTweetViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path('favorites/', views.FavoriteList.as_view(), name='favorite-list'),
    path('favorites/(?P<pk>[0-9]+)/', views.FavoriteDetail.as_view(), name='favorite-detail'),
    path('userLikeArticle/',LikeCreate.as_view()),
    path('userDislike/<int:pk>',DisLIke.as_view())
]