

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20181015_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.OrderItem'),
        ),
    ]
