# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 03:36:08 2019

@author: Ellis_Pax
"""

question = { '1':"What is your favourite snack?",
                 
             '2':"What is your favourite 2019 movie?",
                 
             '3':"What is your fvourite holiday resort?",
                
             '4':"Who do you consider the best actor?"
            }
             
answer = { '1': ['chocolate', 'nuts', 'cream', 'chips'],
           '2': ['avengers', 'frozen', 'joker' ,'rundown'],
           '3': ['victoria', 'amsterdam', 'islands', 'beach'],
           '4': ['rambo', 'dwayne', 'smith', 'chan']
        
         }

 
def create_feud(question):  
    ply1 = 0
    ply2 = 0  
    while len(question) > 0:
        print(" ".join(question.keys()))
        x = input("Choose your question: ")
        if x not in question:
            print(f"Choice invalid! ")
            continue
        print(question[x])
        print(answer[x])
        answerA = input("Player 1 Please Enter your answer -->").lower()
        answerB = input("Player 2 Please Enter your answer -->").lower()
        
        if answerA != answerB:
            #for i in answer[x]:
        
            if (answerA == answer[x][0]):
                ply1 = ply1 + 50
                                    
            elif (answerA == answer[x][1]):
                ply1 = ply1 + 40
               
            elif (answerA == answer[x][2]):
                ply1 = ply1 + 30
            
            elif (answerA == answer[x][3]):
                ply1 = ply1 + 20
                
            if (answerB == answer[x][0]):
                ply2 = ply2 + 50
               
            elif (answerB == answer[x][1]):
                ply2 = ply2 + 40
            
            elif (answerB == answer[x][2]):
                ply2 = ply2 + 30
            
            elif (answerB == answer[x][3]):
                ply2 = ply2 + 20
            
            else:
                ("Invalid Input")
                    
        else:
            print("Player 1 and player 2 cannot choose the same answer! ")
            
        
        del question[x]
       
        
    print("Player 1 has ", ply1, "Points")
    print("Player 2 has ", ply2, "Ponits")
        
            
create_feud(question)

         