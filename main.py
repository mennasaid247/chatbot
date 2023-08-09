import json
import response
import re
def load_json(file): #load responses from chatbot to user
    with open(file) as bot_responses:
        return json.load(bot_responses)
responses_data=load_json("bot.json")
def get_response(input):
    sc_list = []

    split_message=re.split(r'\s+|[,;?!.-]\s*',input.lower())
    #change it to lower case as much easier to process lower case words
    for responses in responses_data:
        response_score = 0
        required_score = 0
        required_words = responses["required_words"]
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score=required_score+1
        if required_score==len(required_words):
            for word in split_message:
                if word in responses["user_input"]:
                    response_score = response_score + 1
        sc_list.append(response_score)
    best_response = max(sc_list)
    response_index = sc_list.index(best_response)
    if input == "":
        return "please type something"
    if best_response != 0:
        return responses_data[response_index]["bot_response"]
    return response.random_string()



while True:
    user_input=input("You:")
    print("Bot:",get_response(user_input))
