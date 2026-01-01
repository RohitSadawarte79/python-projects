

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
from dotenv import load_dotenv





class ExpenseTracker:


    def __init__(self, filename = "data.json"):
        self.filename = filename
        self.data = self._load_data()
    


    def _load_data(self):
        data = {}
        try : 
            with open(self.filename, 'r') as file:
                data = json.loads(file.read())
                return data
            
        except FileNotFoundError:
            with open(self.filename, 'w') as file:
                json.dump(data, file)
            return data
        except Exception as e:
            print("Some Error occured: ", e)

    
    def _save_data(self):
        data = self.data

        with open(self.filename, 'w') as file:
            json.dump(data, file)

    
    def add_expense(self, category : str, amount : int, description : str):
        category = category.lower()

        if category in self.data:
            self.data[category].append({'amount': amount, 'description': description})
        else:
            self.data[category] = [{'amount': amount, 'description': description}]

    @staticmethod
    def gemini_summary(text):
        load_dotenv()
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        prompt = f"Provide a brief, professional financial summary of these expenses. Only give the summary: \n {text}"


        response = client.models.generate_content(
            model = 'gemini-2.5-flash',
            contents = prompt
        )

        return response.text
    
    @property
    def get_summary(self):

        data = self.data
        history = ""

        for category , value in data.items():
                li = value
                text = ""
                for dic in li:
                    text += f"Spent {dic["amount"]} on category {category} and description is {dic["description"]} \n"
                history += text
        
        return self.gemini_summary(history)

    @staticmethod
    def _clear_above_line():
        sys.stdout.write('\033[A\r\033[K')# this I search on chatgpt this is not my skill level
        sys.stdout.flush()

    @staticmethod
    def _temporary_msg(msg, sec):
        sys.stdout.write(msg)
        sys.stdout.flush()

        time.sleep(sec)

        sys.stdout.write('\r' + ' ' * len(msg) + '\r')
        sys.stdout.flush()
        


def main():

    expence_tracker = ExpenseTracker()

    print("Welcome to Your own Finance tracker!\nType: 'add' to add an expance.\nType: 'save' to save your expenses.\nType: 'summary' to know your expence summary.\nType: 'q' to quit \n")

    while (user_selection := input(">")) != 'q':

        if user_selection == 'add':
            expence_tracker._clear_above_line()
            amount = 0
            while True:
                try:
                    amount = int(input("Enter the amount you spent: "))
                    expence_tracker._clear_above_line()
                    break
                except ValueError:
                    expence_tracker._clear_above_line()
                    msg = "Enter the amount in digits not in characters :("
                    expence_tracker._temporary_msg(msg, 2)

            category = input("Enter the category of your spent: ")
            expence_tracker._clear_above_line()

            description = input("Enter a discription about this spent: ")
            expence_tracker._clear_above_line()

            expence_tracker.add_expense(category, amount, description)
            expence_tracker._save_data()

        elif user_selection == 'summary':
            expence_tracker._clear_above_line()
            response = expence_tracker.get_summary
            print(response)
        
        elif user_selection == 'save':
            expence_tracker._clear_above_line()
            expence_tracker._save_data()
        else:
            expence_tracker._clear_above_line()
            msg = "unknown command!"
            expence_tracker._temporary_msg(msg, 2)



main()
                
