import json
from AsciiDammit import asciiDammit

def loadConfig(configFile = 'appconfig.json'):
	configDict = {}
	appDataDirDict = {}
	# configDict = yaml.load(open('appconfig.yaml'))
	configDict = json.load(open(configFile))

	if 'applications' in configDict.keys():
		for appDict in configDict['applications']:
			appDataDirDict[appDict['appName']] = appDict['analysisDir']
	return configDict, appDataDirDict



def renderHtmlTableCell(cellVal):
	if str(cellVal).startswith('\x89PNG'): # search for PNG blobs
		data_uri = str(cellVal).encode('base64').replace('\n','')
		zRowElem =  '<img src="data:image/png;base64,{0}" height="500">'.format(data_uri)
	else:
		# limit the precision to save space in table
		if isinstance(cellVal, float):
			cellVal = "%.3f"%cellVal


		zRowElem = asciiDammit(str(cellVal))
	return zRowElem

