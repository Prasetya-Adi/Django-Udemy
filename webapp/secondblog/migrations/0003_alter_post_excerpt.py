# Generated by Django 3.2.4 on 2021-06-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondblog', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(max_length=500),
        ),
    ]