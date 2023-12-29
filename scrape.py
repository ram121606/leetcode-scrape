from bs4 import BeautifulSoup
import requests

def scrape(url:str):
    print(url)
    data = requests.get(url)
    try:
        soup = BeautifulSoup(data.text , 'html')
        name = soup.find('div',class_='text-label-1 dark:text-dark-label-1 break-all text-base font-semibold').text
        rank = soup.find('span',class_='ttext-label-1 dark:text-dark-label-1 font-medium').text
        lan = soup.find('div',class_='mt-4 flex flex-col space-y-3')
        languages = []
        for i in lan.find_all('span',class_='inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3 notranslate'):
            languages.append(i.text)
        sk = soup.find_all('div',class_='mt-4 flex flex-col space-y-4')
        skills = []
        for i in sk[1].find_all('span',class_='inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full bg-fill-3 dark:bg-dark-fill-3 cursor-pointer transition-all hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2'):
            skills.append(i.text)
        contest_rating = soup.find('div',class_='text-label-1 dark:text-dark-label-1 flex items-center text-2xl').text
        global_ranking = soup.find('div',class_='text-label-1 dark:text-dark-label-1 font-medium leading-[22px]').text
        attend = soup.find_all('div',class_='text-label-1 dark:text-dark-label-1 font-medium leading-[22px]')
        attended = attend[1].text
        count = soup.find_all('span',class_='mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1')
        easy = count[0].text
        medium = count[1].text
        hard = count[2].text
        tot = int(easy)+int(medium)+int(hard)
        return {'Username':name, 'Rank':rank,  'Contest rating':contest_rating, 'Global_ranking':global_ranking, 'No of contests attended':attended, 'Easy solved':easy, 'Medium solved':medium, 'Hard solved':hard, 'Total no of problems solved':tot}
    except AttributeError:
        return {"Error": "Oops...Could not find an account!!!"}