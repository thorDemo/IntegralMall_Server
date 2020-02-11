from datetime import datetime, timedelta
from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
import requests


class PlatformSetting(models.Model):
    set_cookies = models.TextField(help_text='登录信息配置，详情问赵四')
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('set_cookies'),
        ], heading="登录信息配置"),
    ]

    def check_cookie(self):
        tools = CommonBBinQueryTools()
        times = tools.query_user_save_times('wx5885', self.set_cookies)
        if times > 0:
            return 'cookie check success'
        else:
            return 'cookie check failed'
        

class CommonDateTools:
    """
    通用时间工具
    """
    @staticmethod
    def bbin_time_now():
        now = datetime.now()
        bbin_time = now - timedelta(hours=12)
        return bbin_time

    def bbin_time_today(self):
        now = self.bbin_time_now()
        return datetime(now.year, now.month, now.day)

    @staticmethod
    def compare_time(time1, time2):
        # type:(datetime, datetime) -> int
        """
        时间比较 返回timestamp时差
        :param time1:
        :param time2:
        :return:
        """
        stp_time_1 = int(time1.timestamp())
        stp_time_2 = int(time2.timestamp())
        return stp_time_1 - stp_time_2


class CommonBBinQueryTools:
    """
    BBIN 通用后台查询工具
    """
    def __init__(self):
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '',
            'Host': 'bm168.bm168168.com',
            'Origin': 'https://bm168.bm168168.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/75.0.3770.142 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

    def check_cookie(self, cookies):
        headers = self.headers
        headers['Cookie'] = cookies

    def query_user_save_money(self, user_name, start_time=None, end_time=None):
        # type:(str, datetime, datetime) -> int
        """
        :param user_name: 用户名 必填
        :param start_time:
        :param end_time:
        :return: >0 存款总额 =0 没有存款 <0 查询异常 多半是cookie错误
        """
        headers = self.headers
        url = 'https://bm168.bm168168.com/agv3/cl/?module=CashSystem&method=queryProject&sid='
        cookies = PlatformSetting.objects.first().set_cookies
        headers['Cookie'] = cookies
        if (start_time and end_time) is None:
            try:
                data = {
                    'current': 'RMB',
                    'sDate': CommonDateTools.bbin_time_today,
                    'eDate': CommonDateTools.bbin_time_now,
                    'MemNameSel': 'single',
                    'mem_name': user_name,
                    'betNum': '',
                    'page': '',
                    'Sort': '1',
                    'm': '',
                    'cid': '1,3,7,9,12,5,16',
                }
                response = requests.post(url, data=data, headers=headers)
                req = response.json()
                result = str(req['INFO']['total']).replace(',', '').split('.')[0]
                return int(result)
            except KeyError:
                return 0
            except requests.RequestException:
                return -1
        else:
            try:
                data = {
                    'current': 'RMB',
                    'sDate': start_time,
                    'eDate': end_time,
                    'MemNameSel': 'single',
                    'mem_name': user_name,
                    'betNum': '',
                    'page': '',
                    'Sort': '1',
                    'm': '',
                    'cid': '1,3,7,9,12,5,16',
                }
                response = requests.post(url, data=data, headers=headers)
                req = response.json()
                result = str(req['INFO']['total']).replace(',', '').split('.')[0]
                return int(result)
            except KeyError:
                return 0
            except requests.RequestException:
                return -1

    def query_user_save_times(self, user_name, set_cookies=None):
        """
        查询BBIN后台 用户的存款次数
        :param user_name:  用户名
        :param set_cookies:
        :return: -2 查询异常多半是cookie过期 -1 官网不存在该用户 0 没有存款 >0 存款次数
        """
        cookies = set_cookies if set_cookies else PlatformSetting.objects.first().set_cookies
        url = 'https://bm168.bm168168.com/agv3/cl/index.php?module=Level&method=searchMemList'
        headers = self.headers
        headers['Cookie'] = cookies
        try:
            data = {
                'Users': user_name,
            }
            response = requests.post(url, data=data, headers=headers)
            req = response.json()
            if req['user_list']:
                return req['user_list'][0]['deposit_count']
            else:
                return -1
        except KeyError:
            return 0
        except requests.RequestException:
            return -2
