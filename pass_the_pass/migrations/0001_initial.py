# Generated by Django 5.0.6 on 2024-07-04 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(choices=[('SP', 'Spring'), ('SU', 'Summer'), ('AU', 'Autumn'), ('WI', 'Winter')], max_length=50)),
                ('difficulty', models.CharField(choices=[('A1', 'Simple'), ('A2', 'Simple rocks'), ('2A', 'Rocky up to 50°'), ('2B', 'Cool over 45°'), ('3A', 'Cool from 45° to 65°'), ('ZB', 'Of great length')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('surname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Camping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('other_titles', models.CharField(max_length=255)),
                ('connect', models.CharField(max_length=100)),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('NW', 'New'), ('PD', 'Pending'), ('AC', 'Accepted'), ('AC', 'Rejected')], default='NW', max_length=2)),
                ('coord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_the_pass.coord')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_the_pass.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_the_pass.user')),
            ],
        ),
        migrations.CreateModel(
            name='CampingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_the_pass.camping')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_the_pass.image')),
            ],
        ),
    ]
