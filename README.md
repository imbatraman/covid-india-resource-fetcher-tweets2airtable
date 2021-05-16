# covid-india-resource-fetcher-tweets2airtable
A Python GUI that uses the Twitter API to fetch the latest available Covid resources in India, and allows the user to upload them to an Airtable database.

Functionality of Twitter API
- Relies on certain keywords that form the query string to fetch the latest resources shared on Twitter (e.g. "Delhi Oxygen Verified Available")
-- Query string can be changed by the user
- Also obtains additional metrics about the returned tweets like retweets etc.

The GUI enables the user to select relavant information and enter them in a form so:
- The Tweet details can be upload to Airtable database: https://airtable.com/shruARk0fs3QycX75/tbl7w0JxelhKxwTeC
- The data from the Airtable can be exported in json files categorised by resource available
-- The json files can be used as a data source for: https://covidsupport.co.in/ (https://github.com/imbatraman/covid-resources)
