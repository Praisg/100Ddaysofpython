class QuizBrain:
    
    def __init__(self, lis_t):

        self.question_number= 0
        self.question_list = lis_t
        self.score = 0
    
    def still_has_que(self):
        return self.question_number < len(self.question_list)# return true if we still have questions 
        

    def next_que(self):

        que_num = self.question_list[self.question_number] # more like getting the index list[2] myQ[1]
        self.question_number += 1
        user_answ = input(f"Q.{self.question_number} :{que_num.text } (True/False): ") #que_num is Question(text, answer) therfore we are accessing text attribute
        self.check_answ(user_answ, que_num.answer) #check user answer against the corect answer

    def check_answ(self, user_answ, correct):
        if user_answ.lower() == correct.lower():
            self.score += 1
            print("You got it right")
            
        else:
            print("That's wrong")    
        print(f"The correct answer is : {correct}") 
        print(f"Your current score is {self.score}/{self.question_number}\n")


        