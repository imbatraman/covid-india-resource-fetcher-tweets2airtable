import airtable

BASE_ID = "<YOUR AIRTABLE BASE ID>"
API_KEY = "<YOUR AIRTABLE API KEY>"
TABLE_NAME = "Donors"

at = airtable.Airtable(BASE_ID, API_KEY)

category_list = ['remdesivir', 'beds', 'plasma', 'ventilator', 'oxygen', 'other']

def getAllData():
    data = at.get(TABLE_NAME)
    for _ in category_list:
        data_list = []
        for item in data['records']:
            item_data = item['fields']
            try:
                if item_data['Category'].lower() == _:
                    # print(_, item_data['Category'].lower())
                    item_dict = {
                        'uuid': item_data['uuid'],
                        'name': item_data['Name'],
                        'description': item_data['Description'],
                        'contact': item_data['Phone Number'],
                        'lastVerified': ""
                    }
                    data_list.append(item_dict)
            except KeyError as keyError:
                print("")
        with open(f"{_}.txt", 'w') as output_file:
            output_file.write(str(data_list))


