release: python manage.py migrate && python manage.py create_sample_blog_posts
web: gunicorn config.wsgi --log-file -
