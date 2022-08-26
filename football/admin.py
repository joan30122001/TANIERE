from django.contrib import admin
from .models import Category, Product, Event, Article, News, PostTweet, Favorite, Like
# from .models import Competition, Match, Team, MatchTeam




admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Event)
# admin.site.register(Competition)
# admin.site.register(Match)
# admin.site.register(Team)
# admin.site.register(MatchTeam)
admin.site.register(Article)
admin.site.register(News)
admin.site.register(PostTweet)
admin.site.register(Favorite)
admin.site.register(Like)