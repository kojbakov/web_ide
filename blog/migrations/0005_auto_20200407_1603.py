# Generated by Django 2.1.2 on 2020-04-07 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200406_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newtestcase',
            name='step_name',
        ),
        migrations.RemoveField(
            model_name='newtestcase',
            name='steps',
        ),
        migrations.AlterField(
            model_name='steps',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.NewTestCase'),
        ),
    ]
