# Generated by Django 3.2.7 on 2022-08-30 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('football', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='key_words',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='posttweet',
            name='source',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('youtube', 'YouTube'), ('twitter', 'Twitter')], default='facebook', max_length=10),
        ),
    ]
