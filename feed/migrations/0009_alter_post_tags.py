# Generated by Django 3.2 on 2022-06-19 08:43

from django.db import migrations
import tagify.models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=tagify.models.TagField(default='Other', max_length=100, verbose_name='tags'),
        ),
    ]
