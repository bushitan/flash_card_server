#coding:utf-8

import flash_card_server.settings  as SETTINGS
from lite.models import *
import json,urllib2

app_id = SETTINGS.APP_ID
app_secret = SETTINGS.APP_SECRET
class WeiXin():

    def _GetOpenID(self,js_code):
        _js_code = js_code
        _wx_url = "https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code "  %(app_id,app_secret,_js_code )
        req = urllib2.Request(_wx_url)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req)
        _json =  json.loads(response.read())
        return  _json

    def UserLoginCheckSession(self,js_code,session):
        _js_code = js_code
        _session = session

        if User.objects.filter( session = _session ).exists() is True:  #session存在，返回用户
            _user = User.objects.get( session = _session)
        else:#session不存在，获取open_id判断
            # _json = WxHttp(_js_code)
            _json = self._GetOpenID(_js_code)
            _open_id = _json["openid"]
            if User.objects.filter( wx_open_id = _open_id ).exists() is True: #open_id 存在，
                _user = User.objects.get( wx_open_id = _open_id)
            else: #open_id 不存在，增加用户
                _user = User(
                    wx_open_id = _json["openid"],
                    session =  _json["session_key"],
                )
                _user.save()
        return _user.session


# def WxHttp(js_code):
#     _js_code = js_code
#     _wx_url = "https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code "  %(app_id,app_secret,_js_code )
#     req = urllib2.Request(_wx_url)
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
#     response = opener.open(req)
#     _json =  json.loads(response.read())
#     return  _json
