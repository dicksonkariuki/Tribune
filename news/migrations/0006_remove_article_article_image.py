# Generated by Django 2.2.6 on 2019-11-06 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_image',
        ),
    ]
