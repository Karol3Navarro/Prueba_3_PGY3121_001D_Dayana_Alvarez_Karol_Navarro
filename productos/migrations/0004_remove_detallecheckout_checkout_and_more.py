# Generated by Django 5.0.6 on 2024-06-27 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_checkout_detallecheckout_itemcarrito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallecheckout',
            name='checkout',
        ),
        migrations.RemoveField(
            model_name='detallecheckout',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
        migrations.DeleteModel(
            name='DetalleCheckout',
        ),
    ]