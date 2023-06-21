

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20181015_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='customer',
        ),
    ]
