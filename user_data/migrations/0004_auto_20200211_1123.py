# Generated by Django 3.0.3 on 2020-02-11 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0003_auto_20200206_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='total_capital_flow',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dailycapitalflow',
            name='date',
            field=models.DateField(default='2020-02-11'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='user_level',
            field=models.IntegerField(choices=[(0, '未分层'), (1, '第一层'), (2, '第二层'), (3, '第三层'), (4, '第四层'), (5, '第五层'), (6, '第六层'), (7, '第七层'), (8, '第八层'), (9, '第九层'), (10, '第十二层'), (11, '宝马会大客层'), (12, '宝马会过渡层'), (13, '宝马会黑名单'), (14, '宝马会未分层'), (15, '电销首存无反水层级'), (16, '永利博第一层'), (17, '永利博第二层'), (18, '永利博第三层'), (19, '永利博第四层'), (20, '永利博第五层'), (21, '永利博第六层'), (22, '永利博第七层'), (23, '永利博未分层'), (24, '永利博黑名单'), (25, '永利博VIP'), (26, '永利博大客层')], default=0),
        ),
    ]