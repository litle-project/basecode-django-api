**HOW TO RUN**
- run command *source env/bin/activate*
- run command *pipenv run python manage.py runserver*

**HOW TO CREATE A NEW MODULE**
- run command *pipenv run python manage.py startapp {module_name}*

**HOW TO CREATE MIGRATION**
- run command *pipenv run python manage.py makemigrations [your app name] --empty --name [migration name]*
- for example, check out the authentication app

**HOW TO RUN ALL MIGRATION**
- run command *pipenv run python manage.py migrate*

**HOW TO RUN ALL SEEDER**
- run command *pipenv run python manage.py seed*

**HOW TO TRUNCATE ALL TABLE**
- remove all data in table *django_seeding_appliedseeder*
- run command *pipenv run python manage.py truncate --apps [app name]*

**HOW TO EXIT FROM VIRTUAL ENV**
- run command *source deactivate*
