# Generated by Django 3.2.1 on 2021-05-05 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_alter_cmsslider_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс'),
        ),
    ]