import bs4 as bs
import urllib.request
from translate import Translator
from gtts import gTTS #For speech
import os             #For speech

bookTitle = ""

#Writes a text to a file
def saveBook(webpage, language, translate):
  global bookTitle

  source = urllib.request.urlopen(webpage).read()
  soup = bs.BeautifulSoup(source, 'lxml')

  file1 = open(soup.title.string+".txt","w")   #Opens the file
  bookTitle = soup.title.string+".txt"
  file1.write("\n")
  #Chinese version ---
  if (translate == 'y'):
    translator = Translator(to_lang=language)
    #Writes the title
    file1.write(translator.translate("TITLE OF BOOK:")+"\n")
    file1.write(translator.translate(soup.title.string)+"\n")
    file1.write("\n")

    #Writes all paragraphs
    file1.write(translator.translate("BOOK STORY:") + "\n")
    for paragraph in soup.find_all('p'):#p, dd
      file1.write(translator.translate(paragraph.text)+"\n")

  #English version ---
  else:
    #Writes the title
    if (language == 'en'):
      file1.write("TITLE OF BOOK:\n")
    else:
      file1.write("书籍名:\n")
    file1.write(soup.title.string+"\n")
    file1.write("\n")

    #Writes all paragraphs
    if (language == 'en'):
      file1.write("BOOK STORY:\n")
    else:
      file1.write("故事:\n")
    for paragraph in soup.find_all('p'):#p, dd
      file1.write(paragraph.text+"\n")

  file1.close()                   #Closes the file

#Reads the file and prints it to console
def readBook(book):
  file1 = open(book,"r+")         #Opening the file
  print (file1.read())            #Read from file
  file1.close()
  
#Make audio file of text
def textToSpeech(book, lan):
  print(book)
  file1 = open(book,"r+")
  text = file1.read()

  if lan == 'zh':
    language = 'zh-cn'
  elif (lan == 'en'):
    language = 'en'
  speech = gTTS(text = text, lang = language, slow = False)
  speech.save(bookTitle+".mp3")

#Execute code below this line
if __name__ == '__main__':
  #Introduction
  print("This program asks for a website and makes a text and mp3 files reading the websites text. This is intended for websites with book stories in them. You may choose to store the text and audio files in english or chinese.\n")
  
  #Language choice
  while True:
    translate = input("Will this file require translating? (type 'y' for yes and 'n' for no): ")
    if translate == 'y' or translate =='n':
      break
    print("Invalid input.\n")
    
  while True:
    language = input("What language do you prefer? English (type 'en') or Chinese (type 'zh'): ")
    if language == 'en' or language =='zh':
      break
    print("Invalid input.\n")

  webpage = input("Enter your webpage: ")
  saveBook(webpage, language, translate)

  #Reading from book via text
  readBook(bookTitle)

  #Text to speech
  textToSpeech(bookTitle, language)

#Chinese---
#https://baike.baidu.com/item/%E7%81%AF%E7%AC%BC/22354041?fr=aladdin
#https://www.zhenhunxiaoshuo.com/33871.html
#http://www.171xs.com/book/26419/chapter/2812944/

#English---
#https://en.wikisource.org/wiki/Translation:Ballad_of_Mulan

#https://www.nosweatshakespeare.com/shakespeares-plays/modern-romeo-juliet/act-1-scene-1/

#https://www.nosweatshakespeare.com/shakespeares-plays/modern-romeo-juliet/

# https://www.britannica.com/topic/To-Kill-a-Mockingbird
# https://en.wikipedia.org/wiki/Harry_Potter
# https://en.wikipedia.org/wiki/Fr%C3%A9d%C3%A9ric_Chopin
# https://en.wikipedia.org/wiki/The_Girl_on_the_Train_(2016_film)