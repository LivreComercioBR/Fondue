# Generated by Django 5.0.1 on 2024-02-08 17:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_pedido_cupom_alter_pedido_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]