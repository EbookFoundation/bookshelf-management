# Generated by Django 3.1.3 on 2020-11-30 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookshelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookshelf', models.CharField(max_length=255)),
                ('downloads', models.IntegerField(default=0)),
                ('release_date', models.DateField(null=True)),
            ],
            options={
                'db_table': 'bookshelves',
            },
        ),
    ]
