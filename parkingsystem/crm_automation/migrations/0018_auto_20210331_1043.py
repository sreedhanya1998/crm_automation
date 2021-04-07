# Generated by Django 3.1.6 on 2021-03-31 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_automation', '0017_auto_20210331_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='admission_status',
            field=models.CharField(choices=[('notadmitted', 'notadmitted'), ('admitted', 'admitted')], max_length=120),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='enquiry_id',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
    ]
