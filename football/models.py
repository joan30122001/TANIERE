from django.db import models
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField



class Category(models.Model):
    libelle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True, blank=True, null=True)

    class Meta:
        # db_table = 'category'
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.libelle}'



class Product(models.Model):
    STATUS_CHOICES = (
        ('nouveau', 'Nouveau'),
        ('ancien', 'Ancien'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/')
    status = models.CharField(max_length=15, choices = STATUS_CHOICES, default='nouveau')
    reduction = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        # db_table = 'category'
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f'{self.name}'



class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    link = models.URLField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True, blank=True, null=True)

    class Meta:
        # db_table = 'category'
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f'{self.title}'



# class Competition(models.Model):
#     TYPE_COMPETITION_CHOICES = (
#         ('elite 1', 'Elite 1'),
#         ('coupe du cameroun', 'Coupe du cameroun'),
#         ('CAN', 'CAN'),
#         ('coupe du monde', 'Coupe du monde'),
#     )

#     type_competition = models.CharField(max_length=18, choices = TYPE_COMPETITION_CHOICES, default='elite 1')



# class Match(models.Model):
#     score1 = models.IntegerField()
#     score2 = models.IntegerField()
#     day = models.DateField(auto_now=False, auto_now_add=False)
#     time = models.TimeField(auto_now=False, auto_now_add=False)
#     competition = models.ForeignKey(Competition, on_delete=models.CASCADE)



# class Team(models.Model):
#     CATEGORY_CHOICES = (
#         ('junior', 'Junior'),
#         ('senior', 'Senior'),
#         ('professionnel', 'Professionnel'),
#     )

#     GENDER_CHOICES = (
#         ('masculin', 'Masculin'),
#         ('feminin', 'Feminin'),
#     )

#     SPORT_CHOICES = (
#         ('football', 'Football'),
#         ('basketball', 'Basketball'),
#         ('handball', 'Handball'),
#         ('volleyball', 'Volleyball'),
#         ('tennis', 'Tennis'),
#     )

#     name = models.CharField(max_length=255)
#     number_players = models.IntegerField()
#     category = models.CharField(max_length=15, choices = CATEGORY_CHOICES, default='junior')
#     gender = models.CharField(max_length=10, choices = GENDER_CHOICES, default='masculin')
#     sport = models.CharField(max_length=10, choices = SPORT_CHOICES, default='football')



# class MatchTeam(models.Model):
#     match = models.ManyToManyField('Match', blank=True)
#     team = models.ManyToManyField('Team', blank=True)



class KeyWord(models.Model):
    name = models.CharField(max_length = 255)

    class Meta:
        # db_table = 'category'
        verbose_name = "KeyWord"
        verbose_name_plural = "KeyWords"

    def __str__(self):
        return f'{self.name}'



class Article(models.Model):
    # KEYS_CHOICES = (
    #     ('fecafoot', 'FECAFOOT'),
    #     ('fifa', 'FIFA'),
    #     ("samuel eto'o", "Samuel Eto'o"),
    #     ('lions idomptables', 'Lions Idomptables'),
    #     ('afrique', 'Afrique'),
    #     ('cameroun', 'Cameroun'),
    #     ('monde', 'Monde'),
    #     ('elite one', 'Elite One'),
    #     ('stades', 'Stades'),
    #     ('tournois', 'Tournois'),
    #     ('crise', 'Crise'),
    #     ('jeune', 'Jeune'),
    #     ('transferts', 'Transferts'),
    #     ('évènements', 'Evènements'),
    #     ('CAN', 'CAN'),
    #     ('coupe du monde', 'Coupe du Monde'),
    #     ('matchs', 'Matchs'),
    # )

    name = models.CharField(max_length = 255, verbose_name = "Mame of the article")
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    link = models.URLField(blank = True)
    # key_words = MultiSelectField(choices = KEYS_CHOICES, default='fecafoot')
    key_words = models.ManyToManyField(KeyWord)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True, blank=True, null=True)

    class Meta:
        # db_table = 'category'
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return f'{self.name}'



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
    image = models.ImageField(upload_to='media/')
    sport = models.CharField(max_length=10, choices = SPORT_CHOICES, default='football')
    link = models.URLField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True, blank=True, null=True)

    class Meta:
        # db_table = 'category'
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return f'{self.title}'



class PostTweet(models.Model):
    SOURCE_CHOICES = (
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
        ('twitter', 'Twitter'),
    )

    title = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    link = models.URLField(blank = True)
    source = models.CharField(max_length=10, choices = SOURCE_CHOICES, default='facebook')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True, blank=True, null=True)

    class Meta:
        # db_table = 'category'
        verbose_name = "Post et Tweet"
        verbose_name_plural = "Posts et Tweets"

    def __str__(self):
        return f'{self.title}'



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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # db_table = 'category'
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"

    def __str__(self):
        return f'{self.type}'



class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)

    class Meta:
        # db_table = 'category'
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        return f'{self.user}'



def user_images(instance, filename):
    date_time = datetime.now().strftime("%Y_%m_%d,%H:%M:%S")
    saved_file_name = instance.user.username + "-" + date_time + ".jpg"
    return 'profile/{0}/{1}'.format(instance.user.username, saved_file_name)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # image = models.ImageField(upload_to=user_images, default='profile/default/default.png')
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.user.username



# @receiver(post_delete, sender=Profile)
# def profile_image_delete(sender, instance, **kwargs):
#     if instance.image:
#         instance.image.delete(True)