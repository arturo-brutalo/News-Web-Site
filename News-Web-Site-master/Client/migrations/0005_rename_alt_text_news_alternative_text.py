# Generated by Django 5.0.3 on 2024-03-19 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0004_news_alt_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='alt_text',
            new_name='alternative_text',
        ),
    ]
