from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options
import argparse
import time
import os

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--wordlist", required=True, help="Provide a wordlist with email addresses or usernames you want to test.")
args = parser.parse_args()

firefox_options = Options()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(options=firefox_options)

successful_addresses = 0
total_attempts = 0

with open(args.wordlist, "r") as file:
    wordlist_lines = file.readlines()
    file.close()

try:
    for line in wordlist_lines:
        stripped_line = line.strip("\n")
        # Making the connection
        driver.get("https://login.microsoftonline.com/")
        # Locating the username input field and inserting the email address
        input_field = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "i0116")))
        input_field.send_keys(stripped_line)
        # Locating the "Next" button and clicking it after inserting the email address
        button = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "idSIButton9")))
        button.click()
        # After the click action wait 2 seconds to let the page load
        time.sleep(2)
        # Getting the response content after the action above has been executed
        page_response = driver.page_source
        # Keeping track of the total attempts tried
        total_attempts += 1
        # Checking account existence depending on the page response content
        if "This username may be incorrect." in page_response or "We couldn't find an account with that username." in page_response or "Enter a valid email address, phone number, or Skype name." in page_response:
            print(f"Account: {str(stripped_line).ljust(50)}Status: {Fore.RED +'DOES NOT EXIST!' + Style.RESET_ALL}")
        else:
            print(f"Account: {str(stripped_line).ljust(50)}Status: {Fore.GREEN +'EXISTS!' + Style.RESET_ALL}")
            if os.path.isfile("successful-usernames.txt"):
                with open("successful-usernames.txt", "a") as file:
                    file.write(f"{stripped_line}\n")
            else:
                with open("successful-usernames.txt", "x") as file:
                    file.close()
                with open("successful-usernames.txt", "a") as file:
                    file.write(f"{stripped_line}\n")
            successful_addresses += 1
    file.close()
    print("-"*82)
    print(f"Accounts found: {successful_addresses}/{total_attempts}")
except KeyboardInterrupt:
    file.close()
    print("\nUser interrupted quitting...")
    print("-"*82)
    print(f"Accounts found: {successful_addresses}/{total_attempts}")
except:
    print("Something happened, quitting.")
finally:
    driver.quit()
