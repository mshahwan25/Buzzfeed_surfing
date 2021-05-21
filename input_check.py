def check_user_input(msg, answerlist):
    msg =msg.strip()+" \n"
    while True:
        print ("-"*50)
        answer = input (msg).lower()
        if answer in answerlist:
            return answer
            break
        else:
            print ('Not a valid answer.')            
    
    
def main():
    answer = check_user_input('enter',['y','n'])
    
    
if __name__ == '__main__':
    main()
