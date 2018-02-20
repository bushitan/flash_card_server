# -*- coding: utf-8 -*-
from django.contrib import admin
from lite.models import *

# class UserAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(User,UserAdmin)



class CardAdmin(admin.ModelAdmin):
    fieldsets = (
        (u"状态", {
            'classes': ('suit-tab', 'suit-tab-base',),
            'fields': ['face_title','back_explain',]}),
    )
    list_display = ('id','face_title','back_explain',)
    list_display_links = ('id', 'face_title','back_explain',) #点击图片进入
    # list_editable = ('face_title','back_explain',)
admin.site.register(Card,CardAdmin)