# Generated by Django 3.1.3 on 2020-12-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgmt', '0004_auto_20201201_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AlterField(
            model_name='book',
            name='gutindex',
            field=models.TextField(default='1', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='updatemode',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
