# Generated by Django 2.1.2 on 2020-04-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200407_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='steps',
            name='tags',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='steps',
            name='result',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='steps',
            name='step',
            field=models.CharField(max_length=1000),
        ),
    ]