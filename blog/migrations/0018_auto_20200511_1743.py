# Generated by Django 2.1.2 on 2020-05-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200511_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtestcase',
            name='tag',
            field=models.ManyToManyField(blank=True, help_text='Select a tags for this test-case', related_name='tags', to='blog.Tag'),
        ),
    ]
