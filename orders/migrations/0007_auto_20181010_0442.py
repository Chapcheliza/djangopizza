
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20181010_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='toppings',
        ),
        migrations.AddField(
            model_name='item',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='item', to='orders.Topping'),
        ),
    ]
