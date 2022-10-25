from django.contrib import admin
from .models import Category, Product, Event, Article, News, PostTweet, Favorite, Like, KeyWord
# from .models import Competition, Match, Team, MatchTeam




class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'key_word', 'author')

    def key_word(self, obj):
        return "\n".join([p.name for p in obj.key_words.all()])

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'created_at', 'updated_at')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'reduction')

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'created_at', 'updated_at')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'sport')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'source')

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('type', 'user')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('article', 'user')




admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Event, EventAdmin)
# admin.site.register(Competition)
# admin.site.register(Match)
# admin.site.register(Team)
# admin.site.register(MatchTeam)
admin.site.register(KeyWord)
admin.site.register(Article, ArticleAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(PostTweet, PostAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Like, LikeAdmin)