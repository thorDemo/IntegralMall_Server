from django.db import models
from datetime import datetime
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class DailyCapitalFlow(models.Model):
    proxy = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, default='Thor')
    bet = models.FloatField(help_text='有效总投注', default=0.0)
    rebate = models.FloatField(help_text='返水', default=0.0)
    sports = models.FloatField(help_text='体育赛事', default=0.0)
    live = models.FloatField(help_text='视讯直播', default=0.0)
    casino = models.FloatField(help_text='老虎机', default=0.0)
    lottery = models.FloatField(help_text='彩票', default=0.0)
    fish = models.FloatField(help_text='捕鱼机', default=0.0)
    card = models.FloatField(help_text='棋牌', default=0.0)
    update = models.DateField(auto_now=True)
    date = models.DateField(default=datetime.now().strftime('%Y-%m-%d'))

    def _proxy(self):
        if self.proxy == '' or self.proxy is None:
            return 'N/A'
        else:
            return self.proxy

    def _username(self):
        return self.username

    def _bet(self):
        return self.bet

    def _rebate(self):
        return self.rebate

    def _sports(self):
        return self.sports

    def _live(self):
        return self.live

    def _casino(self):
        return self.casino

    def _lottery(self):
        return self.lottery

    def _fish(self):
        return self.fish

    def _card(self):
        return self.card

    def _date(self):
        return self.update

    _proxy.short_description = '代理'
    _username.short_description = '用户名'
    _bet.short_description = '总流水'
    _rebate.short_description = '反水'
    _sports.short_description = '体育'
    _live.short_description = '视讯'
    _casino.short_description = '老虎机'
    _lottery.short_description = '彩票'
    _fish.short_description = '捕鱼'
    _card.short_description = '棋牌'
    _date.short_description = '日期'

    _bet.admin_order_field = '-bet'
    _sports.admin_order_field = '-sports'
    _live.admin_order_field = '-live'
    _casino.admin_order_field = '-casino'
    _lottery.admin_order_field = '-lottery'
    _fish.admin_order_field = '-fish'
    _card.admin_order_field = '-card'
    _date.admin_order_field = '-update'


class UserDetail(models.Model):
    level_choices = (
        (0, '未分层'),
        (1, '第一层'),
        (2, '第二层'),
        (3, '第三层'),
        (4, '第四层'),
        (5, '第五层'),
        (6, '第六层'),
        (7, '第七层'),
        (8, '第八层'),
        (9, '第九层'),
        (10, '第十二层'),
        (11, '宝马会大客层'),
        (12, '宝马会过渡层'),
        (13, '宝马会黑名单'),
        (14, '宝马会未分层'),
        (15, '电销首存无反水层级'),
        (16, '永利博第一层'),
        (17, '永利博第二层'),
        (18, '永利博第三层'),
        (19, '永利博第四层'),
        (20, '永利博第五层'),
        (21, '永利博第六层'),
        (22, '永利博第七层'),
        (23, '永利博未分层'),
        (24, '永利博黑名单'),
        (25, '永利博VIP'),
        (26, '永利博大客层'),
    )
    proxy = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, default='Thor')
    user_level = models.IntegerField(choices=level_choices, default=0)
    total_capital_flow = models.FloatField()
    month_capital_flow = models.FloatField()
    month_error_flow = models.FloatField()

    def _proxy(self):
        return self.proxy

    def _username(self):
        return self.username

    def _user_level(self):
        for line in self.level_choices:
            if line[0] == self.user_level:
                return line[1]
        return 'N/A'

    def _total_capital_flow(self):
        return self.total_capital_flow

    def _month_capital_flow(self):
        return self.month_capital_flow

    def _month_error_flow(self):
        return self.month_error_flow

    def _total_mall_points(self):    # 总商城积分
        ...
        return 0

    def _current_mall_points(self):  # 当前商城积分
        ...
        return 0

    def _total_sign_points(self):    # 总签到积分
        ...
        return 0

    def _current_sign_points(self):  # 当前签到积分
        ...
        return 0

    def _integral_mall_level(self):  #
        ...
        return 0

    _proxy.short_description = '代理'
    _username.short_description = '用户名'
    _user_level.short_description = '官网VIP等级'
    _total_capital_flow.short_description = '总流水'
    _month_capital_flow.short_description = '月流水'
    _month_error_flow.short_description = '月彩票流水'
    _total_mall_points.short_description = '总商城积分'
    _current_mall_points.short_description = '当前商城积分'
    _total_sign_points.short_description = '总签到积分'
    _current_sign_points.short_description = '当前签到积分'
    _integral_mall_level.short_description = '商城等级'
    _user_level.admin_order_field = '-user_level'
    _total_capital_flow.admin_order_field = '-total_capital_flow'
    _month_capital_flow.admin_order_field = '-month_capital_flow'
    _month_error_flow.admin_order_field = '-month_error_flow'


class IntegralMallHistory(models.Model):
    level_choices = (
        (0, '普通会员'),
        (1, '黄金会员'),
        (2, '铂金会员'),
        (3, '钻石会员'),
        (4, '至尊会员'),
        (5, '王者会员'),
        (6, '特邀会员'),
    )
    username = models.CharField(max_length=255, help_text='用户名')
    integral_mall_level = models.IntegerField(choices=level_choices, help_text='商城等级', default=0)
    current_level_up_money = models.IntegerField(help_text='当月晋级礼金', default=0)
    current_month_discount = models.FloatField(help_text='折扣比例', default=1.0)
    current_month_date = models.DateField(help_text='记录月份')

    def current_month_capital_flow(self):
        start_date = self.current_month_date
        end_date = self.current_month_date - timedelta()
        capital_flow_data = DailyCapitalFlow.objects.\
            filter(username=self.username).\
            filter(date__gte=start_date).\
            filter(date__lte=end_date)
        return 0

    panels = [
        MultiFieldPanel([
            FieldPanel('username', classname='col12'),
            FieldPanel('integral_mall_level', classname='col12'),
            FieldPanel('current_month_discount', classname='col12'),
            FieldPanel('current_month_date', classname='col12'),
        ], '积分商城用户历史')
    ]
