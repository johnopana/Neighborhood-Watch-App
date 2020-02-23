from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='hood_pic',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
