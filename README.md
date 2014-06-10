# DjangoCMS Carousel

This app needs:
- [django-cms](https://github.com/divio/django-cms) (obviously)
- [cmsplugin-filer](https://github.com/stefanfoulis/cmsplugin-filer)
- [django-orderedmodel](https://github.com/MagicSolutions/django-orderedmodel)

They should be automatically installed anyway, so no worries.


## SetUp

    pip install git+git://github.com/MagicSolutions/cmsplugin-carousel.git

You should have these in installed apps:

    INSTALLED_APPS = (
        .....
        'easy_thumbnails',
        .....
        'filer',
        'cmsplugin_filer_file',
        'cmsplugin_filer_folder',
        'cmsplugin_filer_image',
        'cmsplugin_filer_teaser',
        .....
        'orderedmodel',
        'cmsplugin_carousel',
    )

And these in THUMBNAIL_PROCESSORS

    THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    )

Run the migrations
    ./manage.py migrate filer
    ./manage.py migrate cmsplugin_carousel

And off you go...

## Demo and development
