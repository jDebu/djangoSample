import requests,json

class Services:

	def get_data_dni(self,dni):
		url= 'http://edunegociosperu.com/reniec-ws/?dni='
		params = {'dni':dni}
		r=requests.get(url,params=params)
		datos=r.json()
		return datos


