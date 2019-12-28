from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Squirrel',
        ),
    ]
