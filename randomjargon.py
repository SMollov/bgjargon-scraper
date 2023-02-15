import requests
from bs4 import BeautifulSoup

def getJargon():
    url = "https://www.bgjargon.com/word/random"
    response = requests.get(url)
    response.raise_for_status()
    
    #Разчитаме HTML съдържанието с BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    #Извличаме думата и я принтираме
    word = soup.find("h2").text.strip()
    print(word)

    #Извличаме значенията и ги принтираме
    definitions = soup.find_all("article")
    for index, definition in enumerate(definitions, start=1):
        meaning = definition.find("p", class_="meaning").text.strip()
        example = definition.find("p", class_="example").text.strip()
        print(f"{index}. {meaning}\n{example}\n")

getJargon()