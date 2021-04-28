from getTweets import getOriginalTweetTextList
from tkinter import *
from newAirtableEntry import newAirtableEntry
from exportJSONfromAirtable import getAllData

tweets_data = getOriginalTweetTextList()


# ---------------------------- GUI FUNCTIONS ------------------------------- #
category = ''
tweet_list_len = len(tweets_data)
tweet_list_index = 0
# ---------------------------- get category option value ------------------------------- #
def categoryValue(selection):
    global category
    category = selection

def incrementTweet():
    global tweet_list_index
    if tweet_list_index >= tweet_list_len:
        print("End of tweets")
    else:
        tweet = tweets_data[tweet_list_index]
        tweet_stats = {
            'text': tweets_data[tweet_list_index]['text'],
            'retweets': tweets_data[tweet_list_index]['retweets']
        }
        print(f"{tweet}\n{tweet_stats}")
        tweet_list_index += 1

def submitEntry():
    name = name_entry.get()
    description = description_entry.get()
    if description == "":
        description = " "
    state = state_entry.get()
    phone = phone_entry.get()
    print(name, description, state, phone, category)
    newAirtableEntry(name, description, state, phone, category)

    # clearing entries after submit
    name_entry.delete(0, 'end')
    description_entry.delete(0, 'end')
    state_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')

    # call incrementTweet
    incrementTweet()

def exitGUI():
    window.destroy()

def exportData():
    getAllData()

# ---------------------------- GUI UI SETUP ------------------------------- #
window = Tk()
window.title('Covid Tweets 2 Airtable Entry')
window.config(padx=50, pady=50)

# Labels
name_label = Label(text='Donor Name:')
name_label.grid(column=0, row=1)
description_label = Label(text='Description:')
description_label.grid(column=0, row=2)
state_label = Label(text='State:')
state_label.grid(column=0, row=3)
category_label = Label(text='Category:')
category_label.grid(column=0, row=4)
phone_label = Label(text='Phone:')
phone_label.grid(column=0, row=5)

# Entry
name_entry = Entry(width=35)
name_entry.grid(column=1, row=1, columnspan=2)
name_entry.focus()
description_entry = Entry(width=35)
description_entry.grid(column=1, row=2, columnspan=2)
state_entry = Entry(width=35)
state_entry.grid(column=1, row=3, columnspan=2)
phone_entry = Entry(width=35)
phone_entry.grid(column=1, row=5, columnspan=2)

# Option Menu
category_list = ['remdesivir', 'beds', 'plasma', 'ventilator', 'oxygen', 'other']
variable = StringVar(window)
variable.set("Select Option")
category_option = OptionMenu(window, variable, *category_list, command=categoryValue)
category_option.grid(column=1, row=4, columnspan=2)

# Buttons
submit_button = Button(text='Submit Entry', width=17, command=submitEntry)
submit_button.grid(column=1, row=6)
next_button = Button(text='Next Tweet', width=17, command=incrementTweet)
next_button.grid(column=2, row=6)
export_data_button = Button(text='Export Airtable Data to Txt files', width=35, command=exportData)
export_data_button.grid(column=1, row=7, columnspan=2)
exit_gui_button = Button(text="Exit GUI", width=35, command=exitGUI)
exit_gui_button.grid(column=1, row=8, columnspan=2)


window.mainloop()