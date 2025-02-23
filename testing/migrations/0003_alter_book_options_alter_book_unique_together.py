# Generated by Django 5.1.6 on 2025-02-16 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_book_delete_library'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['author']},
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('isbn', 'title')},
        ),
    ]
