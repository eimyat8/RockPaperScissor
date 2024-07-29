import random
rps =['R','P','S']
# robot_choice= random.choice(rps)
results=[]
while len(results)<3:
    user_choice=input("Rock for R,Paper for P,Sccisor for S: ")
    robot_choice= random.choice(rps)
    if robot_choice ==user_choice.upper():
        print(f'\nYour choice : {user_choice.upper()}\nRobot choice: {robot_choice}\nThe result is tie')
    elif user_choice.upper()=='R' and robot_choice=='P':
        result='R'
        results.append(result)
        print(f'\nYour choice : {user_choice.upper()}\nRobot choice: {robot_choice}\nRobot Win')
    elif user_choice.upper()=='R' and robot_choice=='S':
        result='U'
        results.append(result)
        print(f'\nYour choice: {user_choice.upper()}\nRobot choice: {robot_choice}\nYou Win')
    elif user_choice.upper()=='P' and robot_choice=='S':
        result='R'
        results.append(result)
        print(f'\nYour choice: {user_choice.upper()}\nRobot choice: {robot_choice}\nRobot Win')
    elif user_choice.upper()=='P' and robot_choice=='R':
        result='U'
        results.append(result)
        print(f'\nYour choice: {user_choice.upper()}\nRobot choice: {robot_choice}\nYou Win')
    elif user_choice.upper()=='S' and robot_choice=='P':
        result='U'
        results.append(result)
        print(f'\nYour choice: {user_choice.upper()}\nRobot choice: {robot_choice}\nYou Win')
    elif user_choice.upper()=='S' and robot_choice=='R':
        result='R'
        results.append(result)
        print(f'\nYour choice: {user_choice.upper()}\nRobot choice: {robot_choice}\nRobot Win')
    else:
        print('Please type only R,P,S')
        continue
u_score=results.count('U')
r_score=results.count('R')
if(u_score>r_score):
    print(f'Congratulation!! You win {u_score} matches')
        
else:
    print(f'Sorry! You lose {r_score} matches')
