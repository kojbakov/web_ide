# Generated by Django 2.1.2 on 2020-04-23 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200423_1146'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestCaseTags',
            new_name='TestCaseTag',
        ),
        migrations.AlterModelOptions(
            name='testcasetag',
            options={'ordering': ['tag']},
        ),
        migrations.RenameField(
            model_name='testcasetag',
            old_name='tags',
            new_name='tag',
        ),
    ]
