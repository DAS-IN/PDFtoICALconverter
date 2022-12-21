import pandas as pd
from icalendar import Calendar, Event

class ICALConverter:
    def __init__(self, df: pd.DataFrame, values: dict):
        self.ical_file = values['-LocICAL-'] #input directory to save the ics file to here
        self.df = df
        self.values = values # true and false values for the radio buttons

        # create calendar
        self.cal = ICALConverter.createCalendar(self.df, self.values)

        # write calendar
        ICALConverter.ICALWriter(self.ical_file, self.cal)

    def createCalendar(df: pd.DataFrame, values):  
        '''
        This function creates a icalendar
            Input:  df = dataframe with data from PDF
                    values = from radio buttons (GUI)
            Output: calendar data
        ''' 
        cal = Calendar()

        cal.add('prodid', '-//My Calendar//mxm.dk//')
        cal.add('version', '2.0')

        #over rows of dataframe
        for index, row in df.iterrows():
            subject = row['Bezeichnung']
            start_time = row['Start_Time']
            end_time = row['End_Time']
            location = row['Raum']
            description = row['Dozent']
                
            # Create an event
            event = Event()
            
            # Set the event properties
            event.add('summary', subject)
            event.add('dtstart', start_time)
            event.add('dtend', end_time)
            if values['-RadioAll-']:
                event.add('location', location)
                event.add("description", description)
            if values['-RadioLectureName-']:
                event.add("description", description)
            if values['-RadioRoom-']:
                event.add('location', location)
            
            # Add event to the calendar
            cal.add_component(event)
        
        return cal

    def ICALWriter(pathway_ical, cal):
        '''
        This function writes the ical 
            Input:  pathway_ical = where to write
                    cal = calendar data
            Output: ical 
        '''
        # write to iCal file
        with open(pathway_ical, 'wb') as f:
            f.write(cal.to_ical())

