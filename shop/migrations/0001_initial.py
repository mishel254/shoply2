# Generated by Django 3.1.4 on 2020-12-09 07:08

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(default='comming soon', max_length=255, null=True)),
                ('Website', models.CharField(default='comming soon', max_length=255, null=True)),
                ('Facebook', models.CharField(default='comming soon', max_length=255, null=True)),
                ('Twitter', models.CharField(default='comming soon', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('review', models.IntegerField(blank=True, default=0, null=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telno', models.CharField(max_length=20)),
                ('social_sites', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.media')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('hours', models.DateTimeField()),
                ('price_range', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('other_details', models.TextField()),
                ('location', models.CharField(default='enter location details', max_length=255, null='False')),
                ('contactInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.contactinfo')),
            ],
        ),
    ]
