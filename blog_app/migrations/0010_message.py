# Generated by Django 5.0.4 on 2024-05-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_alter_comment_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
