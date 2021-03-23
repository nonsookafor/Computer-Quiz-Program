import random
import os
highscore_dict = {} # This is the dictionary that would have all highscorers from highest to lowest.
question_file_handle = open("question.txt", "r")
answer_file_handle = open("answer.txt", "r")# I have written my answers to all questions saved in a dictionary in answer.txt


def get_question(question_text_file):
    total = 0 # used to find the number of lines in question.txt
    starting_list = [] #This is the list that would contain all questions to be asked.
    for line in question_text_file:
        total += 1# Again, used to find the number of lines in the question file.
        if "\n" in line:
            structured_line = line[: len(line) - 1]
            list_str = structured_line.split(",")
            starting_list.append(list_str)
        else:
            list_str = line.split(",")
            starting_list.append(list_str)
    return starting_list, total

    
def choose_question(i_list, t):
    score = 0 # score increases by 5 marks for each question answered correctly.
    your_summary = {} # this is the dictionary that will tell you the questions you got right and those you got wrong.
    for _ in range(t):
        any_question = random.choice(i_list)
        print(any_question)
        print("Type A, B, C or D as your answer.")
        user_input = input(">") # the user should input only A, B, C or D which are letters standing for each option.
        question_number = int(any_question[0])
        answer_file_handle = open("answer.txt", "r")# I have written my answers to all questions saved in a dictionary in answer.txt
        for line in answer_file_handle: 
            str_line = line.split(",")
            for i in range(len(str_line[question_number - 1])):
                if str_line[question_number - 1][i] == " ":
                    s = str_line[question_number - 1][i+1 :]
                    if s == str(user_input):
                        your_summary[question_number] = "right"
                        score += 5
                        
                    else:
                        your_summary[question_number] = "wrong"
        for word in i_list:
            if word == any_question:
                i_list.remove(word)
        next_question_determiner = input("type enter to view next question: ")
        while next_question_determiner != "enter":
            print("sorry, type enter")
            next_question_determiner = input("type enter to view next question: ")
        else:
            pass
    print("Your score is: ", score, ".")
    print("Your response summary is: ", your_summary, ".")
    return your_summary, score
    
    
def know_highscore(name, s):
    highscore_benchmark = 20
    #This is used to determine if you made a high score.
    if s >= highscore_benchmark:
        print("You have made a high score.")
        highscore_file_handle = open("highscore.txt", "a+")
        highscore_file_handle.write("\n" + name + " " + str(s))
    else:
        print("You did not make a high score.")
    # This is used to convert the highscores from highscores.txt to a dictionary that the user can see after each game. Names and scores are seperated by a space. The first line in highscore.txt stands as a base in case the game is started from the very beginning. That is while it is removed from the highscore dictionary as it is not part of the highscore.
    highscore_file_handle = open("highscore.txt", "r") 
    for line in highscore_file_handle:
        linea = ""
        for something in line:
            if something != "\n":
                linea += something
        str_list = linea.split(" ")
        highscore_dict[str_list[0]] = str_list[1]
    if "Those" in highscore_dict:
        del highscore_dict["Those"]
    # making the high scores be from highest scores to lower ones.
    ordered_highscore_dict = {}
    inp_list = []
    for anything in highscore_dict:
        inp_list.append(highscore_dict[anything])
    inp_list.sort()
    inp_list.reverse()
    for num in inp_list:
        for word in highscore_dict:
            if highscore_dict[word] == num:
                ordered_highscore_dict[word] = num
    print("Those with highscores from highest to lowest are: ")
    print(ordered_highscore_dict)    
    return ordered_highscore_dict

        
        
def wrong_answers(summary):
    wrong_number_list = [] # this is just a list that would know the question numbers you get wrong.
    start_list = [] # will be a list of all failed questions.
    num = 0
    for x in summary:
        if summary[x] == "wrong":
            wrong_number_list.append(int(x))
    for row in question_file_handle:
        d = row.split(",")
        for numb in wrong_number_list:
            if numb == int(d[0]):
                num += 1# Again, used to find the number of lines in the question file.
                if "\n" in row:
                    structured_row = row[: len(row) - 1]
                    list_str = structured_row.split(",")
                    start_list.append(list_str)
                else:
                    list_str = row.split(",")
                    start_list.append(list_str)
    return start_list, num

    
def whether_to_retake():
    print("\nDo you want to retake the questions you failed? Type yes if you want to retake the exam otherwise type no. If you failed nothing, type no.") 
    u_input = input("Type either yes or no.")
    while u_input != "no" and u_input != "yes":
        print("sorry, type yes or no.")
        u_input = input("Type either yes or no.")
    if u_input == "no":
        print("You have finished taking the exam.")
        print("Thank you for taking this exam.")
        return "no"
    elif u_input == "yes":
        print("Type start to begin.")
        user_input = input(">")
        # the user can only type start to begin. Any other thing typed will yield sorry.
        while user_input != "start":
            print("sorry, you have to type start.")
            user_input = input(">")
        if user_input == "start":
            print("Make sure you are in a place free from distractions and your personal computer is connected to an electric source or properly charged. Your time still goes even when you log out so be sure to complete the exam in one sitting.")
            print("Type continue to continue.")
            user_input = input(">")
            #the user can only type continue to continue. He has only one chance to type the wrong thing.
            while user_input != "continue":
                print("sorry, type continue")
                user_input = input(">")
            if user_input == "continue":
                return None
    
def choose_retake_question(a_list, m):
    your_retake_summary = {} # this is the dictionary that will tell you the questions you got right and those you got wrong. It is a summary of your score.
    for _ in range(m):
        any_question = random.choice(a_list)
        print(any_question)
        print("Type A, B, C or D as your answer. Typing any other thing would mean you failed the question.")
        user_input = input(">") # the user should input only A, B, C or D which are letters standing for each option.
        question_number = int(any_question[0])# Due to my question pattern, this is always a number.
        answer_file_handle = open("answer.txt", "r")# I have written my answers to all questions saved in a dictionary in answer.txt
        for line in answer_file_handle: 
            str_line = line.split(",")# This is now a list of strings.
            for i in range(len(str_line[question_number - 1])):# This is because the first question now has index as 0 so the numbers had to match.
                if str_line[question_number - 1][i] == " ": # I structured my answers in such a way that the only thing that follows a space is an option.
                    s = str_line[question_number - 1][i+1 :]
                    if s == str(user_input):
                        your_retake_summary[question_number] = "right" #If correct, assign right to the number and increment the score.
                    else:
                        your_retake_summary[question_number] = "wrong"# If wrong, assign wrong to the number and no increment is necessary
        #I had to remove the question so that none repeats.
        for word in a_list:
            if word == any_question:
                a_list.remove(word)
        next_question_determiner = input("type enter to view next question: ")
        while next_question_determiner != "enter":
            print("sorry, type enter")
            next_question_determiner = input("type enter to view next question: ")
        else:
            pass
    print("You have retaken the exam.")
    print("Your response summary is: ", your_retake_summary, ".")
    return your_retake_summary
    
    
def quiz_program():
    name = input("Enter your name: ")
    #the user is to eneter his name first.
    print("Type start to begin.")
    user_input = input(">")
    # the user can only type start to begin. Any other thing typed yields sorry.
    while user_input != "start":
        print("sorry, type start")
        user_input = input(">")
    if user_input == "start":
        print("Make sure you are in a place free from distractions and your personal computer is connected to an electric source or properly charged. Your time still goes even when you log out so be sure to complete the exam in one sitting.")
        print("Type continue to continue.")
        user_input = input(">")
        #the user can only type continue to continue. Any other thing typed yields sorry.
        while user_input != "continue":
            print("sorry, type continue")
            user_input = input(">")
        if user_input == "continue":
            question_file_handle = open("question.txt", "r")
            answer_file_handle = open("answer.txt", "r")
            starting_list, total = get_question(question_file_handle)
            your_summary, score = choose_question(starting_list, total)
            ordered_highscore_dict = know_highscore(name, score)
            if whether_to_retake() != "no":
                retake_starting_list, retake_total = wrong_answers(your_summary)
                your_retake_summary = choose_retake_question(retake_starting_list, retake_total)
    
        
if __name__ == "__main__":
    quiz_program()