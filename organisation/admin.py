from django.apps import apps
from django.contrib import admin

# Register your models here.

organisation_app = apps.get_app_config('organisation')
for model in organisation_app.get_models():
    admin.site.register(model)
