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

class GetBrand(object):
	def __init__(self,choices):
		self.choices=[]
		with open(choices,"r") as f:
			for line in f:
				self.choices.append(line.strip())

	def __call__(self,values):
		brands =[]
		values = ' '.join(values)
		for choice in self.choices:
			if re.search(choice,values,re.IGNORECASE):
				brands.append(choice)

		if not brands:
			brands.append("Unknown")
		return brands

class GetStatus(object):
	def __call__(self,values):
		values=' '.join(values)
		if re.search(u"SOLD",values,re.IGNORECASE):
			return "Sold"
		elif re.search(u"(FS|SALE)",values,re.IGNORECASE):
			return "For Sale"
		elif re.search(u"(FT|TRADE)",values,re.IGNORECASE):
			return "For Trade"
		else:
			return "Unknown"