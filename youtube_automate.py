from selenium import webdriver
import time,os

##usrpssd=os.environ.get('')
usrpssd='yourpassword' ## set your password here
email='youremail@gmail.com' ## set your gmail here
driver_path='C:\\Users\\DILIP\\Downloads\\chromedriver_win32\\chromedriver.exe' ## set your chromedriver path

## opens YouTube
search=input('Search a video on YouTube:')
brows=webdriver.Chrome(driver_path)
brows.get('https://www.youtube.com/')

## Loggedin into account
sign_in_buttn=brows.find_element_by_css_selector('#text')
sign_in_buttn.click()
usr_name=brows.find_element_by_css_selector('#identifierId')
usr_name.send_keys(email)
nxt_buttn=brows.find_element_by_css_selector('#identifierNext > content > span')
nxt_buttn.click()
time.sleep(5)
pssd=brows.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
pssd.send_keys(usrpssd)
nxt_buttn2=brows.find_element_by_css_selector('#passwordNext > content > span')
nxt_buttn2.click()
time.sleep(1)

## search the videos and plays the first one
srch_vdos=brows.find_element_by_css_selector('#search')
srch_vdos.send_keys(search)
time.sleep(1)
enter_srch=brows.find_element_by_css_selector('#search-icon-legacy > yt-icon')
enter_srch.click()
time.sleep(10)
vdo=brows.find_element_by_css_selector('#contents > ytd-video-renderer:nth-child(1)')
vdo.click()


