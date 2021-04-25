# Generated by Django 3.1.3 on 2021-04-23 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(db_column='pk', primary_key=True, serialize=False)),
                ('copyrighted', models.IntegerField(default=0, null=True)),
                ('updatemode', models.IntegerField(default=0, null=True)),
                ('release_date', models.DateField(null=True)),
                ('filemask', models.CharField(max_length=240)),
                ('gutindex', models.TextField()),
                ('downloads', models.IntegerField(default=0, null=True)),
                ('title', models.TextField(blank=True, default='', max_length=255, null=True)),
                ('nonfiling', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='Bookshelf',
            fields=[
                ('id', models.AutoField(db_column='pk', primary_key=True, serialize=False)),
                ('bookshelf', models.CharField(max_length=255)),
                ('downloads', models.IntegerField(default=0)),
                ('release_date', models.DateField(null=True)),
            ],
            options={
                'db_table': 'bookshelves',
            },
        ),
        migrations.CreateModel(
            name='BookshelfToBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_books', models.ForeignKey(db_column='fk_books', on_delete=django.db.models.deletion.CASCADE, to='mgmt.book')),
                ('fk_bookshelves', models.ForeignKey(db_column='fk_bookshelves', on_delete=django.db.models.deletion.CASCADE, to='mgmt.bookshelf')),
            ],
            options={
                'db_table': 'mn_books_bookshelves',
                'unique_together': {('fk_books', 'fk_bookshelves')},
            },
        ),
    ]
