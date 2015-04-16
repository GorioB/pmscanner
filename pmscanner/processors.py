from dateparser.date import DateDataParser
import re
class GetDate(object):
	def __call__(self,values):
		ddp = DateDataParser()
		values = ''.join(values)
		values = values.replace(u'\u00ab',"")
		values = values.replace(u'\u00bb',"")
		dateobj = ddp.get_date_data(values)['date_obj']
		return dateobj.strftime("%B %d, %Y, %H:%M:%S")

class SearchFromList(object):
	def __init__(self,choices):
		self.choices=choices

	def __call__(self,values):
		brands =[]
		values = ' '.join(values)
		for choice in self.choices:
			if re.search(self.choices[choice],values,re.IGNORECASE):
				brands.append(choice)

		if not brands:
			brands.append("Unknown")
		return brands

class GetStatus(object):
	def __call__(self,values):
		values=' '.join(values)
		r = []
		if re.search(u"SOLD|TRADED",values,re.IGNORECASE):
			r.append("Sold")
		if re.search(u"(FS|SALE)",values,re.IGNORECASE):
			r.append("For Sale")
		if re.search(u"(FT|TRADE)",values,re.IGNORECASE):
			r.append("For Trade")
		if not r:
			r.append("Unknown")
		return r