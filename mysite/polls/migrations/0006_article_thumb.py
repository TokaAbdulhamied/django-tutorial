# Generated by Django 2.1.2 on 2018-10-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
