from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from user_data.models import DailyCapitalFlow, UserDetail, IntegralMallHistory
from common_tools.models import CommonDateTools
from datetime import datetime, timedelta
from django.db import transaction


class UserDetailFlushView(APIView):
    permission_classes = [IsAdminUser, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request):
        date_tools = CommonDateTools()
        end_date = date_tools.bbin_time_today()
        start_date = datetime(end_date.year, end_date.month, 1)
        # 计算所有用户的 总流水
        user_all = DailyCapitalFlow.objects.values('username', 'bet').all()
        total_user_total_flow = dict()
        for user in user_all:
            try:
                total_user_total_flow[user['username']] = total_user_total_flow[user['username']] + user['bet']
            except KeyError:
                total_user_total_flow[user['username']] = user['bet']
        # 计算所有用户的 当月流水 彩票
        user_all = DailyCapitalFlow.objects.values('username', 'bet', 'proxy', 'lottery').\
            filter(date__gte=start_date).filter(date__lte=end_date)
        total_user_month_flow = dict()
        total_user_month_error = dict()
        for user in user_all:
            try:
                total_user_month_flow[user['username']] = total_user_month_flow[user['username']] + user['bet']
            except KeyError:
                total_user_month_flow[user['username']] = user['bet']
            try:
                total_user_month_error[user['username']] = total_user_month_error[user['username']] + user['lottery']
            except KeyError:
                total_user_month_error[user['username']] = user['lottery']
        # 清空老数据
        UserDetail.objects.all().delete()
        # 批量导入数据库
        username_data = DailyCapitalFlow.objects.values('username', 'proxy').distinct()
        with transaction.atomic():
            for user in username_data:
                username = user['username']
                proxy = user['proxy']
                try:
                    data = UserDetail(
                        proxy=proxy,
                        username=username,
                        user_level=0,
                        total_capital_flow=round(total_user_total_flow[username], 2),
                        month_capital_flow=round(total_user_month_flow[username], 2),
                        month_error_flow=round(total_user_month_error[username], 2),
                    )
                    data.save()
                except KeyError:
                    data = UserDetail(
                        proxy=proxy,
                        username=username,
                        user_level=0,
                        total_capital_flow=round(total_user_total_flow[username], 2),
                        month_capital_flow=0,
                        month_error_flow=0,
                    )
                    data.save()
        return Response({'message': 'start'})
