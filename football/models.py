from django.db import models
from django.utils import timezone
from users.models import CustomUser



class Category(models.Model):
    libelle = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True, blank=True, null=True)



class Product(models.Model):
    STATUS_CHOICES = (
        ('nouveau', 'Nouveau'),
        ('ancien', 'Ancien'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    status = models.CharField(max_length=15, choices = STATUS_CHOICES, default='nouveau')
    reduction = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True, blank=True, null=True)



class Competition(models.Model):
    TYPE_COMPETITION_CHOICES = (
        ('elite 1', 'Elite 1'),
        ('coupe du cameroun', 'Coupe du cameroun'),
        ('CAN', 'CAN'),
        ('coupe du monde', 'Coupe du monde'),
    )

    type_competition = models.CharField(max_length=18, choices = TYPE_COMPETITION_CHOICES, default='elite 1')



class Match(models.Model):
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    day = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)



class Team(models.Model):
    CATEGORY_CHOICES = (
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('professionnel', 'Professionnel'),
    )

    GENDER_CHOICES = (
        ('masculin', 'Masculin'),
        ('feminin', 'Feminin'),
    )

    SPORT_CHOICES = (
        ('football', 'Football'),
        ('basketball', 'Basketball'),
        ('handball', 'Handball'),
        ('volleyball', 'Volleyball'),
        ('tennis', 'Tennis'),
    )

    name = models.CharField(max_length=255)
    number_players = models.IntegerField()
    category = models.CharField(max_length=15, choices = CATEGORY_CHOICES, default='junior')
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES, default='masculin')
    sport = models.CharField(max_length=10, choices = SPORT_CHOICES, default='football')



class MatchTeam(models.Model):
    match = models.ManyToManyField('Match', blank=True)
    team = models.ManyToManyField('Team', blank=True)



class Article(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField()
    link = models.URLField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True, blank=True, null=True)



class News(models.Model):
    SPORT_CHOICES = (
        ('football', 'Football'),
        ('basketball', 'Basketball'),
        ('handball', 'Handball'),
        ('volleyball', 'Volleyball'),
        ('tennis', 'Tennis'),
    )

    title = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField()
    sport = models.CharField(max_length=10, choices = SPORT_CHOICES, default='football')
    link = models.URLField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True, blank=True, null=True)



class PostTweet(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField()
    link = models.URLField(blank = True)
    source = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True, blank=True, null=True)



class Favorite(models.Model):
    FAVORITES_CHOICES = (
        ('article', 'Article'),
        ('produits', 'Produits'),
        ('posts & tweets', 'Posts & tweets'),
        ('actualités', 'Actualités'),
        ('matchs', 'Matchs'),
        ('evenements', 'Evenements'),
    )

    type = models.CharField(max_length=15, choices = FAVORITES_CHOICES, default='article')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)



class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)