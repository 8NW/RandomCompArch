from xlrd import open_workbook

class TruthTableConverter():

	def __init__(self, TruthTableFileName):
		wb = open_workbook(TruthTableFileName)



		for sheet in wb.sheets():
		    number_of_rows = sheet.nrows
		    number_of_columns = sheet.ncols

		    items = []

		    rows = []
		    for row in range(1, number_of_rows):
		        values = []
		        for col in range(number_of_columns):
		            value  = (sheet.cell(row,col).value)
		            try:
		                value = str(int(value))
		            except ValueError:
		                pass
		            finally:
		                values.append(value)
		        item = Arm(*values)
		        items.append(item)

	def TableToEquation(self):
		equation = '('
		for i in items:

			if i == 0:
				i++

			else:
				for s in range(0, len(items[i]))
					if items[len(items[i])-1] == 1:
						if s == 0:
							equation.append('(')

						if items[i].index(s) != len(items[i]):

							if items[i].index(s) != (len(items[i])-1):
								if s == 1:

								else:
									equation.append
						else:

							equation.append(')')


		equation.append(')')

if __name__ == '__main__':
	