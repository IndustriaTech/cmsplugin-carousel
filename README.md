# DjangoCMS Carousel

This app needs:
- [django-cms](https://github.com/divio/django-cms) (obviously)
- [cmsplugin-filer](https://github.com/stefanfoulis/cmsplugin-filer)
- [django-orderedmodel](https://github.com/MagicSolutions/django-orderedmodel)

They will be automatically installed so no worries.


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

    python manage.py migrate filer
    python manage.py migrate cmsplugin_carousel

And off you go...

## Demo

If you want to see what the carousel looks like, I have made it really easy for you.
Open terminal and execute the following:

    git clone https://github.com/MagicSolutions/cmsplugin-carousel &&
    cd cmsplugin-carousel &&
    mkvirtualenv -a `pwd` -p /usr/bin/python2.7 cmsplugin_carousel_demo &&
    pip install -r example/requirements.txt &&
    ./example/manage.py syncdb --all --noinput &&
    ./example/manage.py migrate --fake &&
    ./example/manage.py loaddata example/loaddata.json &&
    ./example/manage.py runserver 0.0.0.0:8312

After all is set and done, [http://localhost:8312](http://localhost:8312) should load the demo.
