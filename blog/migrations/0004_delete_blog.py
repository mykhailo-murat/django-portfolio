# Generated by Django 5.0.6 on 2024-06-25 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
