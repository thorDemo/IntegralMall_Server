# Generated by Django 3.0.3 on 2020-02-06 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_cookies', models.TextField(help_text='登录信息配置，详情问赵四')),
            ],
        ),
    ]
