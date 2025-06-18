#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyline_site.settings')
import django
django.setup()

from django.db import connection

cursor = connection.cursor()

# Drop the table if it exists
try:
    cursor.execute('DROP TABLE IF EXISTS quotes_review;')
    print('Dropped existing quotes_review table if it existed')
except Exception as e:
    print(f'Error dropping table: {e}')

# Create the table manually
try:
    cursor.execute('''
    CREATE TABLE quotes_review (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL DEFAULT 'Anonymous',
        rating VARCHAR(4) NOT NULL DEFAULT 'none',
        description TEXT NOT NULL DEFAULT 'none',
        created_at DATETIME NOT NULL
    );
    ''')
    print('Created quotes_review table manually')
except Exception as e:
    print(f'Error creating table: {e}')

# Test the table
try:
    cursor.execute('SELECT COUNT(*) FROM quotes_review;')
    count = cursor.fetchone()[0]
    print(f'Table created successfully with {count} rows')
except Exception as e:
    print(f'Error testing table: {e}')

# Mark migration as applied
try:
    cursor.execute('''
    INSERT OR REPLACE INTO django_migrations (app, name, applied) 
    VALUES ('quotes', '0001_initial', datetime('now'));
    ''')
    print('Marked migration as applied')
except Exception as e:
    print(f'Error marking migration: {e}')
