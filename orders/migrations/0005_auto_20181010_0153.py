
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20181010_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('completed', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(blank=True, related_name='orders', to='orders.Item')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=' ', max_length=254),
        ),
        migrations.RemoveField(
            model_name='customer',
            name='cart',
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='customer', to='orders.Order'),
        ),
        migrations.AddField(
            model_name='customer',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pending', to='orders.Order'),
        ),
    ]
