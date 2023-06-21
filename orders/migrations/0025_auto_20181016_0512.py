

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20181015_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='extra',
            new_name='extras',
        ),
    ]
