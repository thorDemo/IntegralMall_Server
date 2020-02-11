from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from common_tools.models import PlatformSetting


class PlatformSettingAdmin(ModelAdmin):
    model = PlatformSetting
    menu_label = '平台设置'
    menu_icon = 'tag'
    list_display = ('check_cookie', )


modeladmin_register(PlatformSettingAdmin)
