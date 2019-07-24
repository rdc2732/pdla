class point(lat, lon):
	"""
	Any geographic point
	"""
	










#----------------------------------------------------------------------
def main():
	""""""
	book = xlwt.Workbook()

	df = pd.read_excel('Temp2.xlsx')
	print("All Data", len(df.index))
	
	df2019 = df.loc[df['Exit'] == 2019].sort_values(by=['PartDesc'])
	print("2019 Data", len(df2019.index))
	
	suppliers = df2019.SupplierName.unique()
	print("Suppliers Data", len(suppliers))

	for idx, supplier in enumerate(suppliers):
		sheet_name = str(idx) + '-' + supplier[0:7]
		parts_data = df2019.loc[df['SupplierName'] == supplier]
		print("Parts Data", supplier, len(parts_data.index))
		add_product_sheet(book, sheet_name, parts_data)
	









#----------------------------------------------------------------------
if __name__ == "__main__":
    main()