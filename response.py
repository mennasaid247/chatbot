# when the chatbot don`t have the right response//the user writes something that is unknown
#so it will return one f these responses randomly
import random
def random_string():
    random_list=[ "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."]
    list_count=len(random_list) #5
    random_item=random.randrange(list_count) #select random num from 0to4(included)

    return random_list[ random_item] #return string from list of response


