
# Shrink-itt - A simple URL Shortner made with Django.

Check out the live demo at [https://shrink-itt.herokuapp.com/](https://shrink-itt.herokuapp.com/)


## How to run

```
# clone the repo
git clone https://github.com/raunaqness/shrink-itt.git
cd shrink-itt

# Make sure you have docker and docker-compose installed
docker-compose up
docker-compose exec web python manage.py migrate
```
App should be running now at [http://localhost:8000](http://localhost:8000)