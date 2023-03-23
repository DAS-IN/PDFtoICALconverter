from PyPDF2 import PdfFileReader
import tabula
import pandas as pd

class PDFReader:

    def __init__(self, pathway_pdf: str):
        sample = open(pathway_pdf, mode = 'rb')
        self.inputpdf = PdfFileReader(sample)
        main_df = pd.DataFrame()
        self.main_df = PDFReader.analyzePage(self.inputpdf, sample, main_df)
        self.main_df = PDFReader.cleanDF(self.main_df)
        self.main_df = PDFReader.formatTime(self.main_df)

    def formatDate(date_column: str):
        '''
        This function formates a date column to a given format
            Input: data column in string format
            Output: column with date format
        '''
        return pd.to_datetime(date_column, format='%d.%m.%Y %H:%M')

    def analyzePage(inputpdf, sample, main_df: pd.DataFrame):
        '''
        This function analyze the pages of a PDF file
            Input: PDF file in binary format
            Output: pd.DataFrame with data from PDF
        '''
        for i in range(inputpdf.numPages):
            df = pd.DataFrame(tabula.read_pdf(sample.name, lattice = True, pages = i + 1, encoding = "cp1252", multiple_tables = True, pandas_options = {"header": None})[0])
            df = df.replace({"\r": " "}, regex=True)
            main_df = pd.concat([main_df,df])
        return main_df

    def cleanDF(main_df: pd.DataFrame):
        '''
        This function cleans the pd.Dataframe
            Input: pd.DataFrame with data from the PDF
            Output: pd.DataFrame with data from PDF (in a cleaned version)
        '''
        #set first row to column name
        main_df = main_df.rename(columns = {0: 'Datum / Zeit', 1: 'Bezeichnung', 2: 'Raum', 3: 'Dozent'})
        main_df = main_df.reset_index().drop(index = [0,1])

        #duplicate the 'datum / Uhrzeit' column
        main_df['Start_Time'] = main_df.loc[:,'Datum / Zeit']

        #sort the columns in right order
        main_df = main_df[['Start_Time', 'Datum / Zeit','Bezeichnung', 'Raum', 'Dozent']]

        #rename 'Datum / Zeit' column
        main_df = main_df.rename(columns={"Datum / Zeit": "End_Time"})

        return main_df

    def formatTime(main_df: pd.DataFrame):
        '''
        This function formats the time to be available as own columns.
            Input: pd.DataFrame with data from the PDF
            Output: pd.DataFrame with data from PDF (start and end time are available with the date format)
        '''
        #transfer datatype object to string
        main_df['Start_Time'] = main_df['Start_Time'].astype("string")
        main_df['End_Time'] = main_df['End_Time'].astype("string")

        #cut the endtime out of starttime
        main_df['Start_Time'] = main_df['Start_Time'].str[:16]

        #cut the starttime out of endtime
        main_df['End_Time'] = main_df['End_Time'].str[0:10] + main_df['End_Time'].str[-6:]

        #convert string to datetime64
        main_df['Start_Time'] =  PDFReader.formatDate(main_df['Start_Time'])
        main_df['End_Time'] =  PDFReader.formatDate(main_df['End_Time'])

        return main_df




     


