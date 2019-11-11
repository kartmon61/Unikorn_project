# Generated by Django 2.2.7 on 2019-11-11 18:11

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('post_hit', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(default=1, null=True, on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostingComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(default=1, max_length=200, null=True)),
                ('posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listBoardApp.Posting')),
            ],
        ),
    ]
