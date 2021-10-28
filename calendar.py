import os
from PIL import Image
from splinter import Browser
from datetime import datetime
import time
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv('LOGIN')
PWD = os.getenv('PASSWORD')

def get_calendars():
    with Browser() as browser:
        browser.driver.set_window_size(1920, 1080)
        browser.visit("https://adecampus.univ-rouen.fr/direct/myplanning.jsp")

        # Login
        browser.fill('username', LOGIN)
        browser.fill('password', PWD)
        browser.find_by_css('button[class="mdc-button mdc-button--raised"]').click()

        # Navigation

        # Si weekend
        now = datetime.now()
        if now.weekday() == 5 or now.weekday() == 6:
            cell = browser.find_by_css('td[title="Today"]').first
            id = cell.__getitem__('id')
            next = id[:-2] + str(int(id[-2:]) + 2)
            browser.find_by_css(f'td[id={next}]').click()


        # Sinon

        browser.find_by_css('img[class=" x-tree3-node-joint"]').click()
        browser.find_by_css('img[class=" x-tree3-node-joint"]')[12].click()
        browser.find_by_css('img[class=" x-tree3-node-joint"]')[15].click()

        # L2 Informatique
        browser.find_by_css('img[class=" x-tree3-node-joint"]')[19].click()

        # Scrolling
        browser.execute_script('document.getElementsByClassName("x-livegrid-scroller")[0].scrollTo(0, 300)')

        # Image
        img_size = (260, 90, 1395, 660)
        td = {20: "1", 21: "2", 22: "3", 23: "4", 25: "1", 26: "2", 27: "3", 28: "sd"}
        #path = "/home/sedixed/licence/projets_perso/python/calendar_bot"
        path = "https://github.com/Sedixed/calendar-bot.git/imgs"
        for i in range(20, 29):
            if i != 24:
                browser.find_by_css('span[class="x-tree3-node-text"]')[i].click()
                time.sleep(1)
                licence = "2" if i < 24 else "3"
                img_path = browser.screenshot(f'{path}/l{licence}td{td[i]}.png')
                new = Image.open(img_path, 'r').crop(img_size)
                new.save(img_path[:len(img_path) - 16] + '.png')
                time.sleep(1)
                os.remove(img_path)
            else:
                browser.find_by_css('img[class=" x-tree3-node-joint"]')[i].click()

        browser.quit()

        # Screen L2

        # TD1
        # browser.find_by_css('span[class="x-tree3-node-text"]')[20].click()
        # time.sleep(1)
        # browser.screenshot('/home/sedixed/licence/projets_perso/python/calendar_bot/l2td1.png')
        #
        # TD2
        # browser.find_by_css('span[class="x-tree3-node-text"]')[21].click()
        # time.sleep(1)
        # browser.screenshot('/home/sedixed/licence/projets_perso/python/calendar_bot/l2td2.png')
        #
        # TD3
        # browser.find_by_css('span[class="x-tree3-node-text"]')[22].click()
        # time.sleep(1)
        # browser.screenshot('/home/sedixed/licence/projets_perso/python/calendar_bot/l2td3.png')
        #
        # TD4
        # browser.find_by_css('span[class="x-tree3-node-text"]')[23].click()
        # time.sleep(1)
        # browser.screenshot('/home/sedixed/licence/projets_perso/python/calendar_bot/l2td4.png')
        #
        # L3 Informatique
        # browser.find_by_css('img[class=" x-tree3-node-joint"]')[24].click()
        #
        # # Screen L3
        #
        # TD1
        # browser.find_by_css('span[class="x-tree3-node-text"]')[25].click()
        # time.sleep(1)
        # browser.screenshot('/home/sedixed/licence/projets_perso/python/calendar_bot/l3td1.png')
        #
        # TD2
        # browser.find_by_css('span[class="x-tree3-node-text"]')[26].click()
        # time.sleep(1)
        # browser.screenshot('/home/sedixed/licence/projets_perso/python/calendar_bot/l3td2.png')
        #
        # TD3
        # browser.find_by_css('span[class="x-tree3-node-text"]')[27].click()
        # time.sleep(1)
        # browser.screenshot('/home/sedixed/licence/projets_perso/python/calendar_bot/l3td3.png')
        #
        # TD SD
        # browser.find_by_css('span[class="x-tree3-node-text"]')[28].click()
        # time.sleep(1)
        # browser.screenshot('/home/sedixed/licence/projets_perso/python/calendar_bot/l3tdsd.png')