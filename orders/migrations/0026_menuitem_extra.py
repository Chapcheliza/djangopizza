

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20181016_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='extra',
            field=models.BooleanField(default=False),
        ),
    ]
