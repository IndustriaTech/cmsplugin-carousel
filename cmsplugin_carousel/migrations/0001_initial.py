# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField(default=1, blank=True, db_index=True)),
                ('alt_tag', models.CharField(verbose_name='Alt tag', max_length=255, blank=True)),
                ('text', models.TextField(verbose_name='Text over image', blank=True)),
                ('url', models.CharField(verbose_name='URL', max_length=500, blank=True, null=True)),
                ('open_in_tab', models.BooleanField(verbose_name='Open in new window')),
                ('image', filer.fields.image.FilerImageField(verbose_name='Image', to='filer.Image', related_name='+')),
                ('page', cms.models.fields.PageField(null=True, blank=True, verbose_name='Page', to='cms.Page')),
            ],
            options={
                'abstract': False,
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='CarouselPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to='cms.CMSPlugin')),
                ('interval', models.PositiveIntegerField(verbose_name='Interval', default=1)),
                ('title', models.CharField(verbose_name='Title', max_length=255, default='', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='carouselpicture',
            name='plugin',
            field=models.ForeignKey(to='cmsplugin_carousel.CarouselPlugin', related_name='pictures'),
        ),
    ]
