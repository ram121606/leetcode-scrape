from bs4 import BeautifulSoup
import requests
from fastapi import HTTPException,status

def scrape(url:str):
    data = requests.get(url)
    if(data.status_code != 200):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Something gone wrong!!')
    else:
        soup = BeautifulSoup(data.text , 'lxml')
        # print(soup.find('h1').text)
        name = soup.find('div',class_='text-label-1 dark:text-dark-label-1 break-all text-base font-semibold').text
        rank = soup.find('span',class_='ttext-label-1 dark:text-dark-label-1 font-medium').text
        lan = soup.find('div',class_='mt-4 flex flex-col space-y-3')
        languages = []
        for i in lan.find_all('span',class_='inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3 notranslate'):
            languages.append(i.text)
        # print(languages)
        sk = soup.find_all('div',class_='mt-4 flex flex-col space-y-4')
        skills = []
        for i in sk[1].find_all('span',class_='inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full bg-fill-3 dark:bg-dark-fill-3 cursor-pointer transition-all hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2'):
            skills.append(i.text)
        contest_rating = soup.find('div',class_='text-label-1 dark:text-dark-label-1 flex items-center text-2xl').text
        # print(contest_rating.text)
        global_ranking = soup.find('div',class_='text-label-1 dark:text-dark-label-1 font-medium leading-[22px]').text
        attend = soup.find_all('div',class_='text-label-1 dark:text-dark-label-1 font-medium leading-[22px]')
        attended = attend[1].text
        count = soup.find_all('span',class_='mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1')
        easy = count[0].text
        medium = count[1].text
        hard = count[2].text
        tot = int(easy)+int(medium)+int(hard)
        return {'username':name, 'rank':rank, 'languages used':languages, 'skills':skills, 'contest_rating':contest_rating, 'global_ranking':global_ranking, 'no_of_contests_attended':attended, 'easy_solved':easy, 'medium_solved':medium, 'hard_solved':hard, 'total_no_of_problems_solved':tot}