# -*- coding: utf-8 -*-
from lib.query_base import *
from pvp.models import *
class QueryBackground(QueryBase):
	def __init__(self):
		super(QueryBackground,self).__init__(Background)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"background_id":obj.id,
			# "im_num":obj.im_num,
			# "pusher_url":obj.pusher,
			# "player_url":obj.player,
			"user_id":obj.user_id,
			"url":obj.url,
			"create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	# import os,django
	# django.setup()
	q = QueryBackground()
	print q.Filter(	)
	# print query_user.GetDict(session = "12321321")