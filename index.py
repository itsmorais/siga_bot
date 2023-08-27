from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()
login_siga = os.getenv("LOGIN_SIGA")
senha_siga = os.getenv("SENHA_SIGA")
email_outlook = os.getenv("EMAIL_OUTLOOK")
senha_outlook = os.getenv("SENHA_OUTLOOK")



driver = webdriver.Chrome()

 # Página de login SIGA
driver.get("https://siga.cps.sp.gov.br/aluno/login.aspx?")
driver.maximize_window()

driver.find_element(By.XPATH,'//input[@id="vSIS_USUARIOID"]').send_keys(login_siga)
driver.find_element(By.XPATH,'//input[@id="vSIS_USUARIOSENHA"]').send_keys(senha_siga)
driver.find_element(By.XPATH,'//input[@class="Button"]').click()
sleep(3)

driver.find_element(By.XPATH,'//span[@id="ygtvlabelel11Span"]').click()
sleep(10)
frequencia = []


for i in range(1,7):
    materia = (driver.find_element(By.XPATH,f'//span[@id="span_vACD_DISCIPLINANOME_000{i}"]').text)
    presenca = (driver.find_element(By.XPATH,f'//span[@id="span_vPRESENCAS_000{i}"]').text)
    ausencia = (driver.find_element(By.XPATH,f'//span[@id="span_vAUSENCIAS_000{i}"]').text)
    frequencia.append([materia,presenca,ausencia])


  
formatted_data = ""
for i in range(6):
    formatted_data += f"Nome matéria: {frequencia[i][0]}\n"
    formatted_data += f"Presenças: {frequencia[i][1]}\n"
    formatted_data += f"Faltas: {frequencia[i][2]}\n"
    formatted_data += f"Total de faltas possíveis: 20\nPosso faltar: {20 - int(frequencia[i][2])}\n"
    pp = int(frequencia[i][1]) / (int(frequencia[i][1]) + int(frequencia[i][2])) * 100
    formatted_data += f"Porcentagem de presença: {pp:.2f}%\n\n"

driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=16&ct=1693155186&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3da5116be2-4f8f-32c9-5eb5-eca0d55a07a0&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
sleep(5)
driver.find_element(By.XPATH,'//input[@id="i0116"]').send_keys(email_outlook)
driver.find_element(By.XPATH,'//input[@id="idSIButton9"]').click()
sleep(5)
driver.find_element(By.XPATH,'//input[@id="i0118"]').send_keys(senha_outlook)
driver.find_element(By.XPATH,'//input[@id="idSIButton9"]').click()
sleep(10)

driver.find_element(By.XPATH,'//button[@class="splitPrimaryButton root-191"]').click()
sleep(10)
driver.find_element(By.XPATH,'//div[@class="Z4n09 VbY1P T6Va1 EditorClass aoWYQ"]').send_keys("moraisdpm@Outlook.com")

driver.find_element(By.XPATH,'//div[@class="dFCbN dPKNh DziEn"]').send_keys(formatted_data)
sleep(15)
driver.find_element(By.XPATH,'//button[@type="button" and @title="Enviar (Ctrl+Enter)"]').click()
sleep(3)
driver.find_element(By.XPATH,'//button[@id="ok-1"]').click()
sleep(10)
