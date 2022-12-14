# Generated by Django 2.2.28 on 2022-08-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz_Green',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frage', models.CharField(max_length=200)),
                ('antwort1', models.CharField(max_length=50)),
                ('antwort2', models.CharField(max_length=50)),
                ('antwort3', models.CharField(max_length=50)),
                ('antwort4', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz_Red',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frage', models.CharField(max_length=200)),
                ('antwort1', models.CharField(max_length=50)),
                ('antwort2', models.CharField(max_length=50)),
                ('antwort3', models.CharField(max_length=50)),
                ('antwort4', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Quiz',
            new_name='Quiz_Black',
        ),
    ]
