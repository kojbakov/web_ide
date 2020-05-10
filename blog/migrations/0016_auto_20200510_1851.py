# Generated by Django 2.1.2 on 2020-05-10 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200510_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newtestcase',
            name='text',
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]