# Generated by Django 4.1.2 on 2022-10-27 16:52

from django.db import migrations
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('en_ucuz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category_name',
            field=djongo.models.fields.ArrayReferenceField(db_column='category_name', on_delete=django.db.models.deletion.CASCADE, to='en_ucuz.category'),
        ),
    ]
