from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH) #Guardamos la ubicacion del DriverChrome.exe 

#driver.get("https://www.instagram.com/vladimirgutierrez7/")
driver.get('https://es.investing.com/crypto/bitcoin')

time.sleep(3) #Damos un lapso de tiempo por si la pagina tarda en cargar

#seguidores = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
precio_bitcoin = driver.find_element_by_xpath('//*[@id="last_last"]')


#print("Seguidores: ",seguidores.text) #Damos formato al resultado
print("Precio del Bitcoin hoy: ", precio_bitcoin.text)

driver.quit() #Luego de tener el resultado, cierro el navegador