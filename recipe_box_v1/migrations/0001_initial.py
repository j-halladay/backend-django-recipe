# Generated by Django 2.2.3 on 2019-07-30 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('bio', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('time_required', models.IntegerField(max_length=4)),
                ('instructions', models.TextField(max_length=800)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_box_v1.Author')),
            ],
        ),
    ]
