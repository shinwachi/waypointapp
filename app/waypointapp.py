import os, collections, sqlite3
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from AsciiDammit import asciiDammit

app = Flask(__name__)
bootstrap = Bootstrap(app)

import util as wpu
configDict = {}
appDataDirDict = {}

appName = "waypointapp"

@app.route('/')
def index():
	appNames = appDataDirDict.keys()
	return render_template('index.html', appNames=appNames)

@app.route('/reportAppIndex/<appName>')
def reportAppIndex(appName):
	'''
	Lists the runs for the assay.
	'''
	answer = []
	for app_name, app_dir in appDataDirDict.items():
		if appName == app_name:
			dirname, dirnames, filenames = next(os.walk(app_dir))
			# ignore the folder named "scrap"
			answer.extend([(app_name, run_id) for run_id in [x for x in dirnames if x != "scrap"]])
	return render_template('reportAppIndex.html', app_name=appName, answer=answer)

@app.route('/report_app/<app_name>/<run_id>')
def report_app(app_name, run_id):
	return reportHelper(appDataDirDict[app_name], run_id, app_name)

def reportHelper(localAppDatadir, run_id, app_name):
	# list all files in the report folder
	dirname, dirnames, filenames = next(os.walk(localAppDatadir+'/'+run_id))
	filepaths = ["file://localhost/"+dirname+"/"+z for z in filenames ]

	# identify all png files in the directory and encode it into database
	images = [x for x in filenames if str(x).endswith('.png')]
	imagepaths = [dirname+"/"+x for x in images]
	imagetags = []
	for ipath in imagepaths:
		data_uri = open(ipath, 'rb').read().encode('base64').replace('\n', '')
		img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
		imagetags.append(img_tag)

	# identify waypoint databases in the folder
	databases = [dirname+'/'+x for x in filenames if str(x).endswith('waypoint.sqlite') ]

	dbTables = collections.OrderedDict()
	colnames = {}
	if databases:
		for db in databases:
			conn = sqlite3.connect(db)
			c = conn.cursor()
			c.execute("SELECT name FROM sqlite_master WHERE type='table';")
			tblNms = sorted([tblNm[0] for tblNm in c.fetchall()])

			# reorder tblNms according to tableOrder
			x = [d for d in configDict['applications'] if d['appName'] == app_name][0]
			if x and 'tableOrder' in x.keys():
				tableOrder = x['tableOrder']
				tn_in_db = []
				for tn in tableOrder:
					if tn in tblNms:
						tn_in_db.append(tn)
						tblNms.remove(tn)
				tblNms = tn_in_db + tblNms

			tblTags= ["#%s"%tblNm for tblNm in tblNms]

			# Iterate over individual tables and retrieve the row data for display
			for tblNm in tblNms:
				rowcount = [row for row in c.execute("SELECT count(*) row_count FROM %s"%tblNm)][0][0]
				if rowcount < 500:
					rows = c.execute('select * from %s'%tblNm)
					# force ascii conversion for display
					colnames[tblNm] = [asciiDammit(description[0]) for description in c.description]
					dbTables[tblNm] = [[wpu.renderHtmlTableCell(x) for x in row] for row in rows]
			conn.close()

	return render_template('report.html', dbpaths=databases, run_id=run_id, tableNames=tblTags, filenames=filenames, filepaths=filepaths, imagetags=imagetags, dbTables=dbTables, colnames=colnames, app_name=app_name)

if __name__ == '__main__':
	# read in the configuration file, then run the server
	configDict, appDataDirDict = wpu.loadConfig(configFile = 'appconfig.json')
	app.run(debug=True, host='0.0.0.0', port=5757)
