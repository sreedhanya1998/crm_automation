# Generated by Django 3.1.6 on 2021-04-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_automation', '0026_auto_20210403_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='registration_status',
            field=models.CharField(choices=[('admitted', 'admitted')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='batch',
            name='batch_status',
            field=models.CharField(choices=[('yettobegin', 'yettobegin'), ('progress', 'progress'), ('completed', 'completed')], max_length=120),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='admission_status',
            field=models.CharField(choices=[('admitted', 'admitted'), ('notadmitted', 'notadmitted'), ('callback', 'callback')], max_length=120),
        ),
    ]