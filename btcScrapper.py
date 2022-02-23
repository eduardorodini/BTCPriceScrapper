from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://finance.yahoo.com/quote/BTC-EUR/history/")

file = open("eur_btc_rates.csv", "w", encoding="utf-8", newline="")
write = csv.writer(file)
header = ["Date", "BTC Closing Value"]
write.writerow(header)

count=1
while (count <= 10):
	date = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[{}]/td[1]".format(count))
	close = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[{}]/td[5]".format(count))
	day = [date.text, close.text]
	write.writerow(day)
	count   = count + 1

driver.quit()   