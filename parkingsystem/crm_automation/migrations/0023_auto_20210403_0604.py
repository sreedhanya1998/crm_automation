# Generated by Django 3.1.6 on 2021-04-03 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_automation', '0022_auto_20210402_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='admission_status',
            field=models.CharField(choices=[('callback', 'callback'), ('notadmitted', 'notadmitted'), ('admitted', 'admitted')], max_length=120),
        ),
    ]
