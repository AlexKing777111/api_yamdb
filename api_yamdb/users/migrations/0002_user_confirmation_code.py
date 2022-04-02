from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="confirmation_code",
            field=models.CharField(default="0000", max_length=4),
        ),
    ]
