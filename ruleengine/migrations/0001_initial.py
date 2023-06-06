from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=200)),
            ],
        ),
    ]
