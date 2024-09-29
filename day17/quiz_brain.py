class QuizBrain:
    def __init__(self, lis_t):

        self.question_number= 0
        self.question_list = lis_t
    
    def next_que(self):
      
        que_num = self.question_list[self.question_number] # more like getting the index list[2] myQ[1]
        self.question_number += 1
        input(f"Q.{self.question_number} :{que_num.text } (True/False): ") 
