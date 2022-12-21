from PDFReader import PDFReader
from GUI import GUI
from ICALConverter import ICALConverter

# Get window with GUI
InputData = GUI()

# Get PDF data
pdf_data = PDFReader(InputData.values['-LocInput-'])

# Convert into ICAL
ICALConverter(pdf_data.main_df, InputData.values)