# Generated by Django 3.1.6 on 2021-03-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_automation', '0005_auto_20210327_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_status',
            field=models.CharField(choices=[('yettobegin', 'yettobegin'), ('progress', 'progress'), ('completed', 'completed')], max_length=120),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='admission_status',
            field=models.CharField(choices=[('admitted', 'admitted'), ('notadmitted', 'notadmitted')], max_length=120),
        ),
    ]