# Generated by Django 4.1.2 on 2022-10-27 16:42

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=255, unique=True)),
                ('item_brand', models.CharField(max_length=50)),
                ('item_model_number', models.CharField(max_length=100)),
                ('item_operating_system', models.CharField(max_length=50)),
                ('item_processor_type', models.CharField(max_length=50)),
                ('item_processor_gen', models.CharField(blank=True, max_length=50)),
                ('item_ram', models.CharField(max_length=50)),
                ('item_disk_type', models.CharField(max_length=50)),
                ('item_disk_size', models.CharField(max_length=50)),
                ('item_screen_size', models.CharField(max_length=50)),
                ('item_rating', models.FloatField()),
                ('item_price', models.FloatField()),
                ('item_site_name', models.CharField(max_length=50)),
                ('item_image_link', models.TextField()),
                ('item_link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='All',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=255, unique=True)),
                ('item_brand', models.CharField(max_length=50)),
                ('item_operating_system', models.CharField(max_length=50)),
                ('item_processor_type', models.CharField(max_length=50)),
                ('item_processor_gen', models.CharField(blank=True, max_length=50)),
                ('item_ram', models.CharField(max_length=50)),
                ('item_disk_type', models.CharField(max_length=50)),
                ('item_disk_size', models.CharField(max_length=50)),
                ('item_screen_size', models.CharField(max_length=50)),
                ('item_rating', models.FloatField()),
                ('item_price', models.FloatField()),
                ('item_site_name', models.CharField(max_length=50)),
                ('item_image_link', models.TextField()),
                ('item_link', models.TextField()),
                ('item_model_number', djongo.models.fields.ArrayReferenceField(db_column='item_model_number', on_delete=django.db.models.deletion.PROTECT, to='en_bilgisayar.product')),
            ],
        ),
    ]
