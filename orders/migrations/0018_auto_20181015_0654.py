

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20181015_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.OrderItem'),
        ),
    ]
