from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('dojos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='create_at',
            field=models.DateTimeField(default=timezone.now),
        ),
        migrations.AddField(
            model_name='dojo',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dojo',
            name='update_at',
            field=models.DateTimeField(default=timezone.now),
        ),
    ]
