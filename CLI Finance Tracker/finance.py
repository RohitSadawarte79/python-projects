

'''
I will be making today cli finance tracker operations it will provide 
add(), 
summary(),
total_spent() on categories
error handling

to store data I will be using dictionary and store a json file

{

 category : [{amount : 99, discription: "something"}]

}
'''


import time, sys, os, json
from google import genai

os.environ['GOOGLE_API_KEY'] = 'AIzaSyBxX9d71qZxPPXwsNNQSSXNug7YyaMfhH8'

# this function will store the data put by user into json file 
def store_input(amount, category : str, discription):
    category = category.lower()
    
    try:
        if os.path.getsize("data.json") != 0:
            with open("data.json", 'r') as file:
                data = json.loads(file.read())

                if category in data:
                    data[category].append({"amount" : amount, "discription": discription})
                else:
                    data[category] = [{"amount" : amount, "discription": discription}]
            
            with open("data.json", 'w') as file:
                json.dump(data, file)
        else:
            with open("data.json", 'w') as file:
                data = {category: [{"amount" : amount, "discription": discription}]}
                json.dump(data, file)

    except FileNotFoundError:
        with open("data.json", 'w') as file:
            data = {category: [{"amount" : amount, "discription": discription}]}
            json.dump(data, file)
    

def total_spent():
    try:
        if os.path.getsize("data.json") != 0:
            with open("data.json", 'r') as file:
                data = json.loads(file.read())
            result = []
            for category , value in data.items():
                li = value
                sum = 0
                for dic in li:
                    sum += dic["amount"]
                result.append({"category": category, "sum": sum})
            
            for dics in result:
                print(f"You spent {dics["sum"]} on {dics["category"]}.")
        else:
            print("No records found")
    
    except FileNotFoundError:
        print("No records found")



def gemini_summary(text):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"Provide a brief, professional financial summary of these expenses. Only give the summary: \n {text}"


    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = prompt
    )

    return response.text


def summary():
    try:
        if os.path.getsize("data.json") != 0:
            with open("data.json", 'r') as file:
                data = json.loads(file.read())
            history = ""
            for category , value in data.items():
                li = value
                text = ""
                for dic in li:
                    text += f"Spent {dic["amount"]} on category {category} and discription is {dic["discription"]} \n"
                history += text
            response = gemini_summary(history)
            print(response)
            
        else:
            print("No records found")
    
    except FileNotFoundError:
        print("No records found")
   
def clear_above_line():
    sys.stdout.write('\033[A\r\033[K')# this I search on chatgpt this is not my skill level
    sys.stdout.flush()

def temprary_msg(msg, sec):
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(sec)
    sys.stdout.write('\r' + ' ' * len(msg) + '\r')
    sys.stdout.flush()


def main():

    # interface
    print("Welcome to Your own Finance tracker!\nType: 'add' to add an expance.\nType: 'total expence' to know your total expences.\nType: 'summary' to know your expence summary.\nType: 'q' to quit \n")
    while (user_selection := input(">")) != 'q':

        if user_selection == 'add':
            while True:
                try:
                    amount = int(input("Write the amount you spent: "))
                    clear_above_line()
                    break
                except ValueError:
                    clear_above_line()
                    msg = "Write number, not spelling"
                    temprary_msg(msg, 2)
            #other inputs:

            category = input("Write the category of the spent: ")
            clear_above_line()

            discription = input("Write a discription about the spent: ")
            clear_above_line()

            try:
                store_input(amount, category, discription)
            except Exception as e:
                print("Some error occured: ", e)
                clear_above_line() 
        elif user_selection == 'total expence':
            try:
                total_spent()
            except Exception as e:
                print("Some error occured: ", e)
                clear_above_line()
        elif user_selection == "summary":
            print("Getting your summary ready....")
            try:
                summary()
            except Exception as e:
                print("Some error occured: ", e)
                clear_above_line()
        else:
            
            temprary_msg("This command does not exists in the system!", 2)   

main()      




