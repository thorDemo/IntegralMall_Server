from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from user_data.models import *
from wagtail.contrib.modeladmin.views import IndexView


class DailyCapitalFlowAdmin(ModelAdmin):
    model = DailyCapitalFlow
    menu_label = '流水数据'
    menu_icon = 'table'
    index_view_extra_css = ''
    list_display = (
        '_proxy', '_username', '_bet', '_rebate', '_sports',
        '_live', '_casino', '_lottery', '_fish', '_card', '_date'
    )
    # list_filter = ('date', )
    search_fields = ('proxy', 'username', 'date')


class UserDetailAdmin(ModelAdmin):
    model = UserDetail
    menu_label = '用户详情'
    menu_icon = 'table'
    list_display = (
        '_proxy', '_username', '_user_level', '_total_capital_flow', '_month_capital_flow', '_month_error_flow',
        '_total_mall_points', '_current_mall_points', '_total_sign_points', '_current_sign_points',
        '_integral_mall_level',
    )
    list_filter = ('user_level', )
    search_fields = ('username', )


class IntegralMallHistoryAdmin(ModelAdmin):
    model = IntegralMallHistory
    menu_label = '用户历史'
    menu_icon = 'table'
    list_display = (
        'username', 'integral_mall_level', 'current_month_discount',
        'current_month_capital_flow', 'current_month_date'
    )


class LibraryGroup(ModelAdminGroup):
    menu_label = '用户数据'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (DailyCapitalFlowAdmin, UserDetailAdmin, IntegralMallHistoryAdmin)


modeladmin_register(LibraryGroup)
