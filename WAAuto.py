from selenium import webdriver
import time
import sys
from selenium.common.exceptions import NoSuchElementException


Link = "https://web.whatsapp.com/"      #predefine the whatsapp web URL

# Function for getting user from
def new_chat(user_name):
    # Selecting the new chat search textbox
    new_chat = chrome_browser.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')
    new_chat.click()

    # Enter the name of chatzzzzz
    new_user = chrome_browser.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')
    new_user.send_keys(user_name)

    time.sleep(1)

    try:
        # Select for the title having user name
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        # Close the browser
        chrome_browser.close()
        print(e)
        sys.exit()



if __name__ == '__main__':


    print("*** Enter the number of contacts you want to send your automated message to: ***")
    n = int(input())
    user_name_list = []
    print("*** Enter the name of person(s) you want to send the automated message to: ***")
    for i in range(0, n):
        ele = input()
        user_name_list.append(ele)  # adding the element

    print("You want to send message to following people: ")
    print(user_name_list)

    #Entering a whole paragraph or a single line as a message
    print("Enter the message and use the symbol '~' to end the message:\nFor example: Hi, this is a test message~\n\nYour message: ")
    message = []
    temp = ""
    done = False

    while not done:
        temp = input()
        if len(temp) != 0 and temp[-1] == "~":
            done = True
            message.append(temp[:-1])
        else:
            message.append(temp)
    message = "\n".join(message)
    print()
    print("The message is: ")
    print(message)

    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=Users/adity/AppData/Local/Google/Chrome/User Data/Default')
    options.add_argument('--profile-directory=Default')

    # Register the drive
    chrome_browser = webdriver.Chrome(executable_path='C:/Program Files/webdrivers/ChromeDriver/chromedriver.exe', options=options)  # Change the path as per your local dir.
    print("Scan your QR code if not logged in already!" )
    chrome_browser.get(Link)  # open whatsapp web
    time.sleep(15)  # time given to user to scan QR code and fully load the whatsapp home page
    print("QR Code scanned")

    for user_name in user_name_list:

        try:
            # Select for the title having user name
            user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user.click()
        except NoSuchElementException as se:
            new_chat(user_name)

        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()

        #Typing message into message box
        message_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        message_box.send_keys(message)

        # Click on send button
        message_box = chrome_browser.find_element_by_xpath('//button[@class="_35EW6"]')
        message_box.click()

        print("Message sent successfully!")
    time.sleep(5)
    chrome_browser.close()
