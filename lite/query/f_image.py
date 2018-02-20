# -*- coding: utf-8 -*-
from lite.models import *
from lite.query.f_base import *

class F_Image(F_Base):
	# def _PackDict(self,query_get):
	# 	_dict = {
	# 		'logo':query_get.logo,
	# 		'nick_name':query_get.nick_name,
	# 	}
	# 	return _dict

	# 1 点击标签 —— 获取供求
	def Set(self,user_id,url):
		image = Image(
			user_id = user_id,
			url = url,
		)
		image.save()
		return True