import requests

parameters = {
    "amount":10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params= parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

#question_data = [
 #   {
  #      "category": "Science: Computers",
   # "correct_answer": "True",
       # "incorrect_answers": [
    #        "False"
     #   ]
    #},
    #{
     #   "category": "Science: Computers",
      #  "type": "boolean",
       # "difficulty": "medium",
        ##"correct_answer": "False",
       # "incorrect_answers": [
        #    "True"
        #]
   # },
    #{
     #   "category": "Science: Computers",
      #  "type": "boolean",
       # "difficulty": "medium",
        #"question": "FLAC stands for 'Free Lossless Audio Condenser'.",
       # "correct_answer": "False",
        #"incorrect_answers": [
         #   "True"
        #]
    #},
    #{
     #   "category": "Science: Computers",
      #  "type": "boolean",
       ##"question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
        #"correct_answer": "False",
        #"incorrect_answers": [
         #   "True"
        #
    #},
    #{
     #   "category": "Science: Computers",
      #  "type": "boolean",
       # "difficulty": "easy",
        #"question": "Linus Torvalds created Linux and Git.",
        #"correct_answer": "True",
        #"incorrect_answers": [
          #  "False"
        #]
    #},
    #{
     #   "category": "Science: Computers",
      #  "type": "boolean",
       # "difficulty": "easy",
        ##"correct_answer": "False",
     #   "incorrect_answers": [
     #       "True"
       # ]
 #   },
  #  {
  #      "category": "Science: Computers",
    #    "type": "boolean",
    #    "difficulty": "medium",
    #    "question": "AMD created the first consumer 64-bit processor.",
    #    "correct_answer": "True",
    #    "incorrect_answers": [
   #         "False"
    #    ]
   # },
 #   {
    #    "category": "Science: Computers",
    #    "type": "boolean",
    #    "difficulty": "easy",
    #    "question": "'HTML' stands for Hypertext Markup Language.",
     #   "correct_answer": "True",
     #   "incorrect_answers": [
     #       "False"
    #    ]
 #   },
  #  {
    #    "category": "Science: Computers",
    #    "type": "boolean",
   #     "difficulty": "easy",
   #     "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
    #    "correct_answer": "True",
    #    "incorrect_answers": [
      #      "False"
     #   ]
 #   },
 #   {
     #   "category": "Science: Computers",
    #    "type": "boolean",
    #    "difficulty": "hard",
    #    "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
    #    "correct_answer": "False",
    #    "incorrect_answers": [
     #       "True"
    #    ]
    #}
#]
