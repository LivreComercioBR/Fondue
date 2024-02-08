# Generated by Django 5.0.1 on 2024-02-08 17:21

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_cupomdesconto_alter_pedido_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cupom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedido.cupomdesconto'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 17, 21, 20, 343352, tzinfo=datetime.timezone.utc)),
        ),
    ]
