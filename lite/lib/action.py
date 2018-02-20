# -*- coding: utf-8 -*-

from lite.lib.util import *
from lite.query.f_card import *
from lite.query.f_image import *
from lite.query.f_tag import *
from lite.query.f_user import *
tag = F_Tag()
image = F_Image()
card = F_Card()
class Action():
    def TagAdd(self,user_id , tag_name):
        tag.Set(user_id,tag_name)
        return True

    def CardAddChar(self,user_id,tag_id , face_title ,back_summary ,back_explain):
        card.Set(user_id,tag_id ,STRANGER,CHAR,face_title ,back_summary ,back_explain ,"")
        return True
    def CardAddImage(self,user_id,tag_id , face_title ,image_url):
        card.Set(user_id,tag_id ,STRANGER,IMAGE,face_title ,'' ,'' ,image_url)
        return True

    def CardGetListByUserID(self,user_id):
        return card.GetListByUserID(user_id)

    def CardSetByTagID(self,user_id,card_id ,tag_id):
        return card.SetByTagID(user_id ,card_id ,tag_id)

    def CardSetByLevelID(self,user_id,card_id ,level_value):
        return card.SetByLevelID(user_id ,card_id ,level_value)


    def CardGetListByAll(self):
        return card.GetListByAll()
