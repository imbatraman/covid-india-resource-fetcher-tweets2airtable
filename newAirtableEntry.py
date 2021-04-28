import uuid
import airtable

BASE_ID = "<YOUR AIRTABLE BASE ID>"
API_KEY = "<YOUR AIRTABLE API KEY>"
TABLE_NAME = "Donors"

at = airtable.Airtable(BASE_ID, API_KEY)

class newAirtableEntry:
    def __init__(self, name, description, state, number, category):
        self.id = str(uuid.uuid1())
        self.name = name
        self.description = description
        self.state = state
        self.number = number
        self.category = category
        self.createAirtableEntry()

    def createAirtableEntry(self):
        entry_dict = {
            'uuid': self.id,
            'Name': self.name,
            'Description': self.description,
            'State': self.state,
            'Category': self.category,
            'Phone Number': self.number
        }

        print(entry_dict)
        at.create(TABLE_NAME, entry_dict)

