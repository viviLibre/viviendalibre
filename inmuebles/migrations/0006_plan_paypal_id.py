# Generated by Django 4.2 on 2023-05-04 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0005_inmueble_lat_inmueble_lng_alter_inmueble_ubicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='paypal_id',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]