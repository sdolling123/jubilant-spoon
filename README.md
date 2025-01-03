# jubilant-spoon

## Requirements

Use the following command to install dependencies for this project:

```Python
pip install -r requirements.txt
```

## Project Setup

1. Create the project...

```Python
django-admin startproject projectName 
```

2. Create app...

```Python
python manage.py startapp app_name
```

3. Configure `settings.py`...
 - Add the app's name to `INSTALLED_APPS`.
 - In `TEMPLATES`, update `DIRS` to `'DIRS': [BASE_DIR / "templates"],`.
 - Add `STATICFILES_DIRS = [BASE_DIR / "static"]`.
4. Follow [instructions](https://django-cotton.com/docs/quickstart) on Django Cotton's site for configuring the project to use this package.