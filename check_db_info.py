#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyline_site.settings')
django.setup()

from django.db import connection

print(f"Database engine: {connection.vendor}")
print(f"Database name: {connection.settings_dict['NAME']}")
print(f"Database host: {connection.settings_dict['HOST']}")
print(f"Database port: {connection.settings_dict['PORT']}")
print(f"Database user: {connection.settings_dict['USER']}")
print(f"Database engine type: {connection.settings_dict['ENGINE']}")
