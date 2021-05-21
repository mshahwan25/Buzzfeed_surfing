import requests
from bs4 import BeautifulSoup
import pandas as pd
import webbrowser
import input_check #this module contains a function that inpsects user inputs
import done_now_weather

    
# this function is used to get the list of daily buzz news and saving them in to CSV file
def get_news_list():
    col = ['article_name','article_link'] #columns names
    df = pd.DataFrame(columns=col)
    #-------------------------------------------------------------
    website = requests.get('https://www.buzzfeed.com/')
    website_content = website.content
    soup = BeautifulSoup(website_content,'lxml')
    #-------------------------------------------------------------
    att = {'class':'js-card__link link-gray'} #news identification
    articles = soup.find_all('a',att)
    #-------------------------------------------------------------
    d = {'article_name': '','article_link':''}
    for i in articles:
        article_name = i.text #news title
        article_link = i['href'] #news link
        df.loc[len(df.index)] = [article_name,article_link] #adding the data into the dataframe
    #-------------------------------------------------------------
    df.to_csv('news_list.csv', index=False)
    return df

#this function is used to show the news title and open the news link upon user approval
def surf_news(counter,df):
    print (df.loc[counter]['article_name'])
    answer = input_check.check_user_input('Would you like to open the page? y/n',['y','n'])
    if answer == 'y':
        article_link = df.loc[counter]['article_link']
        webbrowser.open(article_link)  

def main():
    df = get_news_list()
    news_number = len(df.index) #getting the total number of news
    counter = 0 #to loop through news list
    weather_msg = done_now_weather.get_weather().replace('Currently: ',"")
    print ('-'*50)
    print ("Hi user, the weather now is {},\nI've download a list of {} news from {} website".format(weather_msg,news_number, 'buzzfeed'))
    answer = input_check.check_user_input('Would you like to surf the list? y/n',['y','n'])
     
    if answer =='y':
        surf_news(counter,df)
        # to loop through all list items
        while True:
            counter +=1
            if counter <= news_number:
                print ('\n')
                print ('-'*50)
                answer = input_check.check_user_input('Would you like to check the next topic? y/n',['y','n'])
                if answer =='y':
                    surf_news(counter,df)
                elif answer == 'n':
                    print ('Thanks for your time, bye')
                    break
            else:
                print ('End of list reached!, Thank you')
                break
    elif answer == 'n':
        print ('Thanks for your time, bye')


if __name__ == '__main__':
    main()

