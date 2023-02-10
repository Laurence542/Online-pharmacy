# Generated by Django 4.1.5 on 2023-01-16 15:48

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('Clinic1', models.CharField(max_length=200, unique=True)),
                ('Clinic2', models.CharField(max_length=200, unique=True)),
                ('Clinic3', models.CharField(max_length=200, unique=True)),
                ('Clinic4', models.CharField(max_length=200, unique=True)),
                ('price1', models.CharField(max_length=200, unique=True)),
                ('price2', models.CharField(max_length=200, unique=True)),
                ('price3', models.CharField(max_length=200, unique=True)),
                ('price4', models.CharField(max_length=200, unique=True)),
                ('phone1', models.CharField(max_length=200, unique=True)),
                ('phone2', models.CharField(max_length=200, unique=True)),
                ('phone3', models.CharField(max_length=200, unique=True)),
                ('phone4', models.CharField(max_length=200, unique=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='picture')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]