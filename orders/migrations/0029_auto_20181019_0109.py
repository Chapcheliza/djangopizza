

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0028_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
