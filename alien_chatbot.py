import re
import random

class RuleBot:
    negative_responses = ("no","nope","nah","naw","not a chance","sorry")
    exit_commands = ("quit","pause","exit","goodbye","bye","later")
    random_questions = (
        "Why are you here?",
        "Are there many human likes you?",
        "What do you consume for sustenance?",
        "Does earth have a leader?",
        "What planets have you visited?",
        "What technology do you have on this planet?"
    )

    def __init__(self):
        self.alienbabble = {'describe_planet_intent':r'.*\s*your planet.*',
                           'answer_why_intent':r'why\sare.*',
                           'about_intellipat':r'.*\s*intellipat'
                          }

    def greet(self):
        self.name = input("Hi, what's your name?   ")
       
        will_help = input(f"Hi {self.name}, I am Allien-Bot. I'm  from other planet .Will you help me learn about your planet? \n")
       
        if will_help in self.negative_responses:
            print("Ok, Have a Nice Earth Day!")
            return
       
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Okay, Have a Nice Day!")
                return True

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent =='describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_intellipat':
                return self.about_intellipat()
        if not found_match:
            return self.no_match_intent()

    def describe_planet_intent(self):
        responses = ("My planet is a utopia of diverse organisms and species.",
                    "I am from Opidipus, the capital of the wayward Galaxies")
        return random.choice(responses)

    def answer_why_intent(self):
        responses = ("I come in peace.",
                    "I am here to collect data on your planet and its inhabitants.",
                    "I heard the coffee is good.")
        return random.choice(responses)

    def about_intellipat(self):
        responses = ("Intellipaat is the world's largest Professional educational company.",
                    "Intellipaat will make you learn concepts in a way like never before.",
                    "Intellipaat is where your career and skills grow.")
        return random.choice(responses)

    def no_match_intent(self):
        responses = ("Please tell me more.",
                    "Tell me more!",
                    "Why do you say that?",
                    "I See. Can you elaborate?",
                    "Interesting. Can you tell me more?",
                    "I see. How do you think?",
                    "Why?",
                    "How do you think I feel when you say that?")
        return random.choice(responses)


AlienBot = RuleBot()
AlienBot.greet()
