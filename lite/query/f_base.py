#coding:utf-8
class F_Base():
	def _PackList(self,_pack_fun,query_filter):
		_list = []
		for q in query_filter:
			_list.append( _pack_fun(q) )
		return _list
