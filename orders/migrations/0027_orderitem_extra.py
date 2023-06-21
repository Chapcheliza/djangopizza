

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_menuitem_extra'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='extra',
            field=models.BooleanField(default=False),
        ),
    ]
