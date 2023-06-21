

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20181009_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='orders',
            new_name='cart',
        ),
    ]
