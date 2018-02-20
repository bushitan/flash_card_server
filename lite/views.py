#coding:utf-8

import json

from django.http import HttpResponse
from django.views.generic import ListView


from lib.message import *
from models import *
import datetime
from lite.lib.qi_niu import *
import  flash_card_server.settings  as SETTINGS
from lite.lib.util import *
from lite.lib.action import *
action = Action()
#1 首页文章初始化
# class Index( ListView):
#     def get(self, request, *args, **kwargs):
#         try:
#             print 11111
#             _dict = {
#                 'MSG':u'登录初始化成狗',
#             }
#             print _dict
#             return MESSAGE_RESPONSE_SUCCESS(_dict)
#         except Exception,e :
#             return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
#1

# 3 获取生词库
class CardGetAll( ListView):
    def get(self, request, *args, **kwargs):
        pass
    def post(self, request, *args, **kwargs):
        try:

            _card_list = action.CardGetListByAll()
            _dict = {
                'card_list':_card_list,
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

class MyExample( ListView):
    def get(self, request, *args, **kwargs):
        pass
    def post(self, request, *args, **kwargs):
        try:
            example = '''
<p>一张单词牌的完美记忆之旅是这样的：</p>
<ol>
<li>顺利通过第一次检测；</li>
<li>隔几小时，顺利通过第二次检测；</li>
<li>隔几天，顺利通过第三次检测；</li>
<li>隔几周，顺利通过第四次检测；</li>
<li>隔半年左右，顺利通过第五次检测。</li>
</ol>
<p>&nbsp; &nbsp; 假定这张单词牌在第四次检测没通过，那么将会被打回"陌生"栏，重新进行第二次、第三次、第四次和第五次检测。</p>
<br>
<p>一张单词牌，想要被翻出，必须要：</p>
<p><strong>连续（不能中断）顺利通过，3-5次，间隔时间越来越长的，识记检测。</strong></p>
<br>
<p>&nbsp; &nbsp; 那些顽固的单词，可能要被三个栏目折磨得往复数十遍。它会总是在你面前打转转，知道被你下<strong>定决心，下足功夫，记住它。</strong></p>
<p>毫不例外，它最终也要连续顺利通过3-5次间隔时间越来越长的检测。</p>
<br>
<p>&nbsp; &nbsp; 此时，我们完全有理由相信：一年以后的高考/考研/司法考试/注会考试/托福雅思GRE考试，这道题目你肯定会做（这个单词肯定认识）。</p>
<p>&nbsp;</p>
<br>
<p>当然，记忆其他的知识点也一样受用，希望能给你带来帮助</p>
             '''
            _dict = {
                'example':example,
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


class TagAdd( ListView):
    def get(self, request, *args, **kwargs):
        try:
            _session = request.GET.get('session',"")
            _user = User.objects.get(session = _session)
            _tag_name = request.GET.get('tag_name',"")
            _r = action.TagAdd(_user.id,_tag_name)
            _dict = {
                'msg':u'增加标签成功',
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
# 2
class CardAddChar( ListView):
    def get(self, request, *args, **kwargs):
        try:
            _session = request.GET.get('session',"")
            _user = User.objects.get(session = _session)
            _tag_id = request.GET.get('tag_id',"")
            _face_title = request.GET.get('face_title',"")
            # _back_style = request.GET.get('back_style',"")
            _back_summary = request.GET.get('back_summary',"")
            _back_explain = request.GET.get('back_explain',"")

            _r = action.CardAddChar( _user.id,_tag_id , _face_title ,_back_summary ,_back_explain)
            _dict = {
                'msg':u'增加闪卡成功',
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

# 3 获取所有闪卡
class CardGetListByUserID( ListView):
    def get(self, request, *args, **kwargs):
        try:
            _session = request.GET.get('session',"")
            _user = User.objects.get(session = _session)
            _card_list = action.CardGetListByUserID( _user.id )
            _dict = {
                'card_list':_card_list,
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )



# 4 设置闪卡分类
class CardSetByTagID( ListView):
    def get(self, request, *args, **kwargs):
        try:
            _session = request.GET.get('session',"")
            _user = User.objects.get(session = _session)
            _card_id = request.GET.get('card_id',"")
            _tag_id = request.GET.get('tag_id',"")

            action.CardSetByTagID( _user.id ,_card_id ,_tag_id )
            _dict = {
                 'msg':u'闪卡添加标签成功',
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

# 5 设置闪卡分类
class CardSetByLevelID( ListView):
    def get(self, request, *args, **kwargs):
        try:
            _session = request.GET.get('session',"")
            _user = User.objects.get(session = _session)
            _card_id = request.GET.get('card_id',"")
            _level_value = request.GET.get('level_value',"")

            action.CardSetByLevelID( _user.id ,_card_id ,_level_value )
            _dict = {
                'msg':u'闪卡分类成功',
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


from lib.weixin import WeiXin
#1 首页文章初始化
class UserLogin( ListView):
    def get(self, request, *args, **kwargs):
        try:
            _js_code = request.GET.get('js_code',"")
            _session = request.GET.get('session',"")
            _wx = WeiXin()
            _check_session = _wx.UserLoginCheckSession(_js_code,_session)
            return MESSAGE_RESPONSE_SUCCESS({"session":_check_session })
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )






# 1 Day首页 -- 初始化
class DayIndex( ListView):
    def get(self, request, *args, **kwargs):
        try:
            _session = request.GET.get('session',"")
            _user = User.objects.get(session = _session)
            _upload_list = []
            _upload_query = Image.objects.filter(user_id = _user.id)
            #_upload_query = File.objects.all()
            for d in _upload_query:
                #计算第几天上传
                dt =  datetime.datetime(2018, 1, 1).replace(tzinfo=None)
                _create_time = d.create_time.replace(tzinfo=None)
                create_day = (_create_time - dt).days
                _upload_list.append({
                    "url":d.url,
                    "style":d.style,
                    "content":d.content,
                    "create_day": create_day,
                    "create_time":d.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "create_date":d.create_time.strftime("%Y-%m-%d"),
                    "create_hour":d.create_time.strftime("%H:%M:%S"),
                })
            _dict = {
                "today_date":datetime.datetime.now().strftime("%Y年%m月%d日"),
                "today_id":(datetime.datetime.now().replace(tzinfo=None) -  datetime.datetime(2018, 1, 1).replace(tzinfo=None)).days ,
                # "today_id":(datetime.datetime.now().replace(tzinfo=None) -  datetime.datetime(2018, 1, 1).replace(tzinfo=None)).days ,
                # "today_id":1 ,
                "file_list":_upload_list,
            }
            # print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )



#1 首页文章初始化
class MyIndex( ListView):
    def get(self, request, *args, **kwargs):
        try:
            _session = request.GET.get('session',"")
            _user = User.objects.get( session = _session)

            _ad_list = [
                {
                    'title': "谢谢老板",
                    'img_url': "https://www.12xiong.top/day365/static/zan_qr.jpg",
                    'description':u"功能当然都是免费的啦，能支持当然很开心啦，能开更多存储",
                },
                {
                    'title': "一起坚持吧",
                    'img_url': "https://www.12xiong.top/day365/static/fengxiong_qr.jpg",
                    'description':u"我喜欢画画，今年剩下的时间已经不多了，你我共勉",
                },
                {
                    'title': "押韵ZONE",
                    'img_url': "http://img.12xiong.top/help_day365_qr_yayun.jpg",
                    'description':u"坚持诗歌、歌词创作，它能帮您快速找到韵脚",
                },
                # {
                #     'title': "Rap的押韵搜索",
                #     'img_url': "http://img.12xiong.top/help_huaxun_4.jpg",
                #     'description':u"描述描述描述描述述",
                # },
                # {
                #     'title': "Rap的押韵搜索",
                #     'img_url': "../../images/qr_yayun.jpg",
                #     'description':u"描述描述描述描述描述描述",
                # }
            ]
            _clock = {
                "is_open":True,
                "alarm_time":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            _dict = {
                "user_id":_user.id,
                'logo':_user.logo,
                'nick_name':_user.nick_name,
                "clock":_clock,
                'ad_list':_ad_list,
                # 'article_list':_article_list
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )



#1 首页文章初始化
class MySetClock( ListView):
    def get(self, request, *args, **kwargs):
        try:
            _dict = {
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )



#1 首页文章初始化
class MySetLogo( ListView):
    def get(self, request, *args, **kwargs):
        try:
            _session = request.GET.get('session',"")
            _logo_url = request.GET.get('logo_url',"")
            _nick_name = request.GET.get('nick_name',"")
            # if  User.objects.filter( session = _session).exists() is False:
            #     return MESSAGE_RESPONSE_LOGIN_OUT()
            _user = User.objects.get( session = _session)
            _user.logo = _logo_url
            _user.nick_name = _nick_name
            _user.save()
            print _user
            print _logo_url,_nick_name
            # return HttpResponse(json.dumps({"status":"true","msg":u"登陆成功"}),content_type="application/json")
            _dict = {
                "msg":u"登陆成功"
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

FILE_KEY_HASH = {} #内存，key-session对应表
#1 首页文章初始化
class UploadGetToken( ListView):
    def get(self, request, *args, **kwargs):
        try:

            _user = User.objects.get(session = request.GET.get('session',""))
            _style = request.GET.get('style',"")
            _suffix = request.GET.get('suffix',"")  #后缀

            #按照当前时间和用户生成名字
            _file_name = "day365_" + str(_user.id) + "_" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "." + _suffix

            _qn = QiNiu()
            token,key =_qn.getToken(_file_name)
            FILE_KEY_HASH[key] = {
                "user_id":_user.id,
                "file_name":_file_name,
                "style":_style,
            }
            _dict = {
                "token":token,
                "key":key,
                "FILE_KEY_HASH":FILE_KEY_HASH,
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

#1 上传成功 -- 保存图片网址
class UploadCallback( ListView):
    def get(self, request, *args, **kwargs):
        print 232
    def post(self, request, *args, **kwargs):
        try:
            print 12321
            key = request.POST['key']
            _hash = request.POST['hash']
            w = request.POST['w']
            h = request.POST['h']
            duration = request.POST['duration']
            fsize = request.POST['fsize']
            vw = request.POST['vw']
            vh = request.POST['vh']


            if FILE_KEY_HASH.has_key(key):
                _user_id = FILE_KEY_HASH[key]["user_id"]
                _style = FILE_KEY_HASH[key]["style"]
                _file_name = FILE_KEY_HASH[key]["file_name"]

                _file = Image(
                    user_id = _user_id,
                    file_name = _file_name,
                    style = _style,
                    url = SETTINGS.QINIU_HOST + key,
                )
                print _file
                _file.save()

                #当前距离2017年的时间
                dt =  datetime.datetime(2018, 1, 1).replace(tzinfo=None)
                _create_time = _file.create_time.replace(tzinfo=None)
                create_day = (_create_time - dt).days
                _dict = {
                    "url":_file.url,
                    "style":_file.style,
                    "content":_file.content,
                    "create_day": create_day,
                    "create_time":_file.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "create_date":_file.create_time.strftime("%Y-%m-%d"),
                    "create_hour":_file.create_time.strftime("%H:%M:%S"),
                }
            else :
                raise # name不存在如果没有，直接返回网络错误
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

