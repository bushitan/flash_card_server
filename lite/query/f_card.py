# -*- coding: utf-8 -*-
from lite.models import *
from lite.query.f_base import *

class F_Card(F_Base):
	def _PackDict(self,query_get):
		_dict = {
			'logo':query_get.logo,
			'nick_name':query_get.nick_name,
		}
		return _dict

	def _PackSubDict(self,query_get):
		_dict = {
			'card_id':query_get.id,
			'is_face':True,
			'face_title':query_get.face_title,
			'back_explain':query_get.back_explain,
		}
		return _dict
	# 1 点击标签 —— 获取供求
	def Set(self,user_id ,tag_id, level ,back_style , face_title , back_summary ,back_explain ,back_image_id):
		card = Card(
			user_id = user_id,
			tag_id = None if tag_id == "" else tag_id,
			level = level,
			face_title = face_title,
			back_style = back_style,
			back_summary = back_summary,
			back_explain = back_explain,
			back_image_id =  None if back_image_id == "" else back_image_id,
		)
		card.save()
		return True

	#临时使用的
	def GetListByAll(self):
		_query = Card.objects.all()
		return self._PackList(self._PackSubDict,_query)

	def GetListByUserID(self,user_id):
		_query = Card.objects.filter(user_id = user_id)
		return self._PackList(self._PackDict,_query)

	def SetByTagID(self,user_id,card_id ,tag_id):
		_card = Card.objects.get(user_id = user_id , card_id = card_id)
		_card.tag_id = tag_id
		_card.save()
		return True
	def SetByLevelID(self,user_id,card_id ,level_value):
		_card = Card.objects.get(user_id = user_id , card_id = card_id)
		_card.level = int(level_value)
		_card.save()
		return True


















