from flet import *
import pandas as pd



def main(page:Page):

	# CREATE DATA TO EXPORT TO EXCEL
	# FORMAT DICT
	mydata = [
	{"name":"john","age":12,"food":"burger"},
	{"name":"anta","age":24,"food":"pizza"},
	{"name":"januar","age":34,"food":"milk"},
	{"name":"beny","age":56,"food":"cheese"},
	{"name":"usman","age":75,"food":"spagethi"},

	]

	# CREATE THE TABLE
	dt = DataTable(
		columns=[
			DataColumn(Text("name")),
			DataColumn(Text("age")),
			DataColumn(Text("food")),
		],
		rows=[]

		)

	# AND PUSH YOU DICT JSON TO YOU TABLE
	for x in mydata:
		dt.rows.append(
			DataRow(
			cells=[
				DataCell(Text(x['name'])),
				DataCell(Text(x['age'])),
				DataCell(Text(x['food'])),

				]

			)

			)

	# NOW PROCESS TO EXCEL

	def processtoexcel(e):
		# THIS FOR COLUMN IN YOU EXCEL
		data = {"name":[],"age":[],"food":[]}

		# NOW LOOP
		for x in mydata:
			data['age'].append(x['age'])
			data['name'].append(x['name'])
			data['food'].append(x['food'])

		df = pd.DataFrame(data)

		# AND FINALLY WRITE TO EXCEL FILE
		# AND FILE EXCEL LOCATION IN MAIN.PY
		df.to_excel("myfile.xlsx",index=False)



	page.add(
	Column([
	Text("DataTable export to EXCEl",
		size=30,weight="bold"
	),
	dt,
	ElevatedButton("Export to Excel",
	on_click=processtoexcel,
	bgcolor="blue",
	color="white"

	)



		])

		)


flet.app(target=main)
