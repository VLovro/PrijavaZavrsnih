# Generated by Django 4.1.4 on 2022-12-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_kolegij_kolegij_nositelj'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_kolegiji',
            field=models.ManyToManyField(to='main.kolegij'),
        ),
    ]
