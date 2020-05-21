# Generated by Django 2.2 on 2020-05-19 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_auto_20200519_1707'),
        ('comments', '0002_auto_20200519_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发表时间')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='点赞者')),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.Post', verbose_name='文章')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
