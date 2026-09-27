from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='budget',
            field=models.DecimalField(max_digits=14, decimal_places=2, default=0),
        ),
    ]
