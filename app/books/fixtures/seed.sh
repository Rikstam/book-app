docker-compose exec books python manage.py loaddata authors.json
docker-compose exec books python manage.py loaddata countries.json
docker-compose exec books python manage.py loaddata books.json