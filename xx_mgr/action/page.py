# -*- coding: utf-8 -*-

from xx_mgr.query.tag import *
from xx_mgr.query.article import *

PID_YM_INDEX = 11
PID_YM_AMERICAN = 12


class ActionPage():
	def __init__(self):
		self.query_tag = QueryTag()
		self.query_article = QueryArticle()


	def GetNav(self,web_site):
		return  self.query_tag.FilterQuery(web_site = web_site,father = None)

	def GetYMIndex(self):
		one_tag_list = self.query_tag.FilterQuery(father__pid = PID_YM_INDEX,pid = 1)
		one_article_list = []
		for t in one_tag_list:
			if  self.query_article.IsExists(tag = t) is True:
				one_article_list.append( self.query_article.GetQuery(tag = t) )
			else:
				one_article_list.append({})



		two_tag = self.query_tag.GetQuery(father__pid = PID_YM_INDEX,pid = 2)
		two_article_list = self.query_article.FilterQuery(tag = two_tag)[0:8]


		three_tag = self.query_tag.GetQuery(father__pid = PID_YM_INDEX,pid = 3)
		three_article_list = self.query_article.FilterQuery(tag = three_tag)[0:9]


		four_tag = self.query_tag.GetQuery(father__pid = PID_YM_INDEX,pid = 4)
		four_article_list = self.query_article.FilterQuery(tag = four_tag)[0:8]


		return one_tag_list,one_article_list,\
			   two_tag,two_article_list ,\
				three_tag, three_article_list ,\
			   four_tag,four_article_list


	# 国家子类
	def GetYMCountryAd(self):
		return self.getOnly(PID_YM_AMERICAN,1)
	def GetYMCountryInfo(self):
		return self.queryOnly(PID_YM_AMERICAN,3,8)
	def GetYMCountryDetail(self):
		return self.queryMore(PID_YM_AMERICAN,4)

# 	#留学首页
# 	def GetLXIndex1(self):
# PID_LX_INDEX


	def getOnly(self,father_pid,pid):
		_tag = self.query_tag.GetQuery(father__pid = father_pid,pid = pid)
		_article = {}
		if  self.query_article.IsExists(tag = _tag):
			_article = self.query_article.GetQuery(tag = _tag)
		return _tag,_article

	def queryOnly(self,father_pid,pid,range):
		_tag = self.query_tag.GetQuery(father__pid = father_pid,pid = pid)
		_article_list = self.query_article.FilterQuery(tag = _tag)[0:range]
		return _tag,_article_list
	def queryMore(self,father_pid,pid):
		one_tag_list = self.query_tag.FilterQuery(father__pid = father_pid,pid = pid)
		one_article_list = []
		for tag in one_tag_list:
			if  self.query_article.IsExists(tag = tag) is True:
				one_article_list.append( self.query_article.GetQuery(tag = tag) )
			else:
				one_article_list.append({})
		return one_tag_list,one_article_list



	def GetArticleListByTagID(self,tag_id):
		_article_list = self.query_article.FilterQuery(tag = tag_id)
		return _article_list


	def GetArticleByID(self,article_id):
		if self.query_article.IsExists() is True:
			return self.query_article.GetQuery(id = article_id)
		else:
			return False





if __name__ == "__main__":
	import os,django
	django.setup()
	a = ActionPage()
	# print a.GetYMIndex()
	print a.GetYMNav()
	# a.pvpRoomDict