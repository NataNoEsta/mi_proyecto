# Generated by Django 4.0.6 on 2022-09-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(default='default', max_length=255),
        ),
    ]
