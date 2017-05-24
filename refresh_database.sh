find . -path "/djangazon/website/migrations/*.py" -not -name "__init__.py" -delete; #deletes all of the .py files in the migrations directory except for the __init__.py file.
find . -path "/djangazon/website/migrations/*.pyc"  -delete; #deletes all of the .pyc files in the migrations directory.
rm db.sqlite3; #deletes the database file.
python manage.py makemigrations website; #creates the migration.
python manage.py migrate; #runs the migration.  This will delete all of the data in your database.
python manage.py loaddata user.json profile.json category.json product.json order.json payment_type.json  #loads the data from each .json file in sequential order.