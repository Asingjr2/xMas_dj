# xMas

Application allows user to create secret santa gift list with randomly generated pairings.  Can create different pairings.

## Installation

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver
```

## Testing

```bash
python manage.py test secret_santa/tests
```
