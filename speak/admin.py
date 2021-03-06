#coding:utf-8
from django.contrib import admin
from models import *
from lib.admin_config import *


# Register your models here.

class SpeakThemeAdmin(AppAdmin):
	list_display = ('id','title','content','voice','issue_time',)
	suit_form_tabs = (('content', u'拼读作业'),)
	raw_id_fields = ('voice',)
	fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ['title','content','voice','issue_time',]
		}),
    )
admin.site.register(SpeakTheme,SpeakThemeAdmin)


class SpeakUserAdmin(AppAdmin):
	list_display = ('id','user','voice','theme',)
	suit_form_tabs = (('content', u'提交作业'),)
	raw_id_fields = ('voice',)
	fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ['user','voice','theme',]
		}),
    )
admin.site.register(SpeakUser,SpeakUserAdmin)

#积分
class SpeakBonusAdmin(AppAdmin):
	list_display = ('id','user_self','user_other','theme','action','score',)
	suit_form_tabs = (('content', u'用户积分'),)
	# raw_id_fields = ('voice',)
	fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ['user_self','user_other','theme','action','score',]
		}),
    )
admin.site.register(SpeakBonus,SpeakBonusAdmin)
#积分
class SpeakSetScoreAdmin(AppAdmin):
	list_display = ('id','action','score',)
	suit_form_tabs = (('content', u'设置积分'),)
	fieldsets = (
		(u"分类", {
			'classes': ('suit-tab', 'suit-tab-content',),
			'fields': ['action','score',]
		}),
    )
admin.site.register(SpeakSetScore,SpeakSetScoreAdmin)



















