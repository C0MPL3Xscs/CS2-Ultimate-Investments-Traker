from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

## ---------------------------------------------------------------------------------------------------------------- ##
## -------------------------------------------------VARIABLES------------------------------------------------------ ##
## ---------------------------------------------------------------------------------------------------------------- ##

OBF = "0.00"
OR = "0.00"
RMR2020 = "0.00"
S10A = "0.00"
SA2022 = "0.00"
Skins = 29.56
knife = 310.00/2
gloves = 74.00
Cases = "0.00"
today = datetime.date.today()

## ---------------------------------------------------------------------------------------------------------------- ##
## ---------------------------------------------------PRICES------------------------------------------------------- ##
## ---------------------------------------------------------------------------------------------------------------- ##

# GETS CASES PRICES


def casesPrice():
    # Filter by cases
    casesFilter = driver.find_element(
        By.ID, "tag_filter_730_2_Type_CSGO_Type_WeaponCase")
    casesFilter.click()
    selectAll.click()

    # Wait for the "next page" button to become clickable, then click it
    for i in range(3):
        nextPage = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='sih_button next_page' and div]")))
        nextPage.click()
        selectAll.click()
        time.sleep(0.5)

    Cases = driver.find_element(By.CLASS_NAME, "select_price")
    Cases: str = str(Cases.text).replace("€", "")

    casesFilter.click()
    unselect = driver.find_element(
        By.CLASS_NAME, "sih_cancel_select_all_inventory_button")
    unselect.click()

    return Cases

# GETS RMR2020 STICKER PRICES


def RMR2020Price():
    # Filter by RMR2020
    RMR2020Filter = driver.find_element(
        By.ID, "tag_filter_730_2_StickerCapsule_crate_sticker_pack_rmr2020_challengers_collection")
    RMR2020Filter.click()
    RMR2020Filter1 = driver.find_element(
        By.ID, "tag_filter_730_2_StickerCapsule_crate_sticker_pack_rmr2020_contenders_collection")
    RMR2020Filter1.click()
    RMR2020Filter2 = driver.find_element(
        By.ID, "tag_filter_730_2_StickerCapsule_crate_sticker_pack_rmr2020_legends_collection")
    RMR2020Filter2.click()

    button = driver.find_element(By.CLASS_NAME, "sih_button.first_page")
    if "disabled" not in button.get_attribute("class"):
        button.click()

    selectAll.click()

    # Wait for the "next page" button to become clickable, then click it
    for i in range(3):
        nextPage = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='sih_button next_page' and div]")))
        nextPage.click()
        time.sleep(0.5)
        selectAll.click()
        time.sleep(0.5)

    RMR2020 = driver.find_element(By.CLASS_NAME, "select_price")
    RMR2020: str = str(RMR2020.text).replace("€", "")

    RMR2020Filter.click()
    RMR2020Filter1.click()
    RMR2020Filter2.click()
    unselect = driver.find_element(
        By.CLASS_NAME, "sih_cancel_select_all_inventory_button")
    unselect.click()

    return RMR2020

# GETS ANTWERP 2022 STICKR PRICES


def SA2022Price():
    # Filter by Antwerp 2022
    SA2022Filter = driver.find_element(
        By.ID, "tag_filter_730_2_StickerCapsule_crate_signature_pack_antwerp2022_group_players_collection")
    SA2022Filter.click()
    SA2022Filter1 = driver.find_element(
        By.ID, "tag_filter_730_2_StickerCapsule_crate_sticker_pack_antwerp2022_challengers_collection")
    SA2022Filter1.click()

    button = driver.find_element(By.CLASS_NAME, "sih_button.first_page")
    if "disabled" not in button.get_attribute("class"):
        button.click()

    time.sleep(0.5)
    selectAll.click()

    # Wait for the "next page" button to become clickable, then click it
    nextPage = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='sih_button next_page' and div]")))
    nextPage.click()
    time.sleep(0.5)
    selectAll.click()
    time.sleep(0.5)

    SA2022 = driver.find_element(By.CLASS_NAME, "select_price")
    SA2022: str = str(SA2022.text).replace("€", "")

    SA2022Filter.click()
    SA2022Filter1.click()
    unselect = driver.find_element(
        By.CLASS_NAME, "sih_cancel_select_all_inventory_button")
    unselect.click()

    return SA2022

# GETS OPERATION BROKEN FANG ITEMS PRICES


def OBFPrice():
    # Filter by Operation Broken Fang
    OBFFilter = driver.find_element(
        By.ID, "tag_filter_730_2_StickerCapsule_crate_sticker_pack_broken_fang_lootlist")
    OBFFilter.click()

    button = driver.find_element(By.CLASS_NAME, "sih_button.first_page")
    if "disabled" not in button.get_attribute("class"):
        button.click()

    selectAll.click()

    # Wait for the "next page" button to become clickable, then click it
    nextPage = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='sih_button next_page' and div]")))
    nextPage.click()
    time.sleep(0.5)
    selectAll.click()
    time.sleep(0.5)

    OBF = driver.find_element(By.CLASS_NAME, "select_price")
    OBF: str = str(OBF.text).replace("€", "")

    OBFFilter.click()
    unselect = driver.find_element(
        By.CLASS_NAME, "sih_cancel_select_all_inventory_button")
    unselect.click()

    return OBF

# GETS OPERATION RIPTIDE ITEMS PRICES


def ORPrice():
    # Filter by Operation Riptide
    ORFilter = driver.find_element(
        By.ID, "tag_filter_730_2_StickerCapsule_crate_sticker_pack_op_riptide_capsule_lootlist")
    ORFilter.click()
    ORFilter1 = driver.find_element(
        By.ID, "tag_filter_730_2_StickerCapsule_crate_sticker_pack_riptide_surfshop_lootlist")
    ORFilter1.click()

    button = driver.find_element(By.CLASS_NAME, "sih_button.first_page")
    if "disabled" not in button.get_attribute("class"):
        button.click()

    selectAll.click()

    # Wait for the "next page" button to become clickable, then click it
    for i in range(2):
        nextPage = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='sih_button next_page' and div]")))
        nextPage.click()
        time.sleep(0.5)
        selectAll.click()
        time.sleep(0.5)

    OR = driver.find_element(By.CLASS_NAME, "select_price")
    OR: str = str(OR.text).replace("€", "")

    ORFilter.click()
    ORFilter1.click()
    unselect = driver.find_element(
        By.CLASS_NAME, "sih_cancel_select_all_inventory_button")
    unselect.click()

    return OR

# GETS 10 YEAR BIRTHDAY STICKER PRICES


def S10APrice():
    # Filter by 10 Year Birthday Stickers
    S10AFilter = driver.find_element(
        By.ID, "tag_filter_730_2_StickerCapsule_crate_sticker_pack_csgo10_capsule_lootlist")
    S10AFilter.click()

    button = driver.find_element(By.CLASS_NAME, "sih_button.first_page")
    if "disabled" not in button.get_attribute("class"):
        button.click()

    selectAll.click()

    time.sleep(0.5)
    selectAll.click()
    time.sleep(0.5)

    S10A = driver.find_element(By.CLASS_NAME, "select_price")
    S10A: str = str(S10A.text).replace("€", "")

    S10AFilter.click()
    unselect = driver.find_element(
        By.CLASS_NAME, "sih_cancel_select_all_inventory_button")
    unselect.click()

    return S10A

## ---------------------------------------------------------------------------------------------------------------- ##
## ----------------------------------------------AUXILIXAR METHODS------------------------------------------------- ##
## ---------------------------------------------------------------------------------------------------------------- ##

# GETS TOTAL ITEMS VALUE


def getTotal():
    total: float = float(OBF) + float(OR) + float(RMR2020) + float(S10A) + \
        float(SA2022) + float(Skins) + float(gloves) + \
        float(knife) + float(Cases)

    return total

# CHECKS IF ITS A WIN(🟢) OR A LOSE(🔴)


def checkProfit(paid, actual):
    if float(actual) < float(paid):
        return "🔴"
    else:
        return "🟢"

# GENERATES A TEXT FOR STEAM TEXTBOX SHOWCASE INVESTMENTS PORTFOLIO


def getText():
    TOTAL = getTotal()

    text = """[b] Resume [/b]
    -Operation Broken Fang -> [b]38,25€ [/b] (actual price: [b]""" + str(OBF) + """€ [/b]) [""" + checkProfit(38.25, OBF) + """]
    -Operation Riptide -> [b]12,75€ [/b] (actual price: [b]""" + str(OR) + """€ [/b]) [""" + checkProfit(12.75, OR) + """]
    -Stickers MMR 2020 -> [b]25€ [/b] (actual price: [b]""" + str(RMR2020) + """€ [/b]) [""" + checkProfit(25, RMR2020) + """]
    -Stickers 10 Year Birthday -> [b]5€ [/b] (actual price:[b]""" + str(S10A) + """€ [/b]) [""" + checkProfit(5, S10A) + """]
    -Stickers Antwerp 2022 ->[b]13,76€ [/b] (actual price: [b]""" + str(SA2022) + """€ [/b]) [""" + checkProfit(13.76, SA2022) + """]
    -Skins -> [b]11,94€  [/b](actual price: [b]""" + str(Skins) + """€ [/b]) [""" + checkProfit(11.94, Skins) + """]
    -Gloves-> [b]49€  [/b] [/b](actual price:[b]""" + str(gloves) + """€ [/b]) [""" + checkProfit(49, gloves) + """]
    -Knife-> [b]62.50€ [/b] (actual price: [b]""" + str(knife) + """€ [/b]) [""" + checkProfit(62.50, knife) + """]
    -Cases -> [b]15€ [/b](actual price: [b]""" + str(Cases) + """€ [/b]) [""" + checkProfit(15, Cases) + """]
    [🟢] -> WON MONEY [🔴] -> LOST MONEY

    (SOME OF THE [🔴] ARE LONG TERM INVESTMENTS SO I BELIEVE THEIR PRICE WILL SIGNIFICANTLY INCREASE WITH TIME TURNING INTO [🟢] )

    Total Spent: [b] ~278,38€ [/b]
    Total Actual Value: [b]~""" + str(TOTAL) + """€ [/b]
    Total Profit: [b]~""" + str(TOTAL - 278.38) + """€ [/b]

    [b] [LAST UPDATED """ + str(today) + """] [/b]"""

    text2 = """
    -Operation Broken Fang -> """ + str(OBF) + """€
    -Operation Riptide -> """ + str(OR) + """€
    -Stickers MMR 2020 -> """ + str(RMR2020) + """€
    -Stickers 10 Year Birthday ->""" + str(S10A) + """€
    -Stickers Antwerp 2022 ->""" + str(SA2022) + """€
    -Skins -> """ + str(Skins) + """€
    -Gloves-> """ + str(gloves) + """€
    -Knife-> """ + str(knife) + """€
    -Cases ->""" + str(Cases) + """€

    Total Spent:  ~278,38€
    Total Actual Value: ~""" + str(TOTAL) + """€ 
    Total Profit: ~""" + str(TOTAL - 278.38) + """€"""

    saveFile(text, text2)

# SAVES THE TEXT INTO A TEXT FILE


def saveFile(text, text2):
    with open("Steam\\[" + str(today) + "].txt", "w", encoding="utf-8") as file:
        file.write(text)

    with open("Statistics\\[" + str(today) + "].txt", "w", encoding="utf-8") as file:
        file.write(text2)

# EXECUTES ALL THE NEEDED FUNCTIONS FOR THE COMPLETE INVENTORY PRICE UPDATE


## ---------------------------------------------------------------------------------------------------------------- ##
## --------------------------------------------------- MAIN ------------------------------------------------------- ##
## ---------------------------------------------------------------------------------------------------------------- ##


if __name__ == "__main__":
    # Define the path to Chrome user data directory:
    user_data_dir = "C:\\Users\\Samuel Sampaio\\AppData\\Local\\Google\\Chrome\\User Data"
    profile_name = "Default"

    # Create a new ChromeOptions object and add the user data and profile arguments:
    options = Options()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument(f"--profile-directory={profile_name}")
    options.add_argument('--disable-dev-shm-usage')

    # Create a new web driver instance for Chrome with the specified profile:
    driver = webdriver.Chrome(options=options)

    # Navigate to the URL
    url = "https://steamcommunity.com/profiles/XXXXXXXXXXXX/inventory/#730"
    driver.get(url)

    time.sleep(1)

    # Open filters tab
    filters = driver.find_element(By.ID, "filter_tag_show")
    filters.click()
    time.sleep(1)

    # Open show more
    collection_label = driver.find_element(
        By.XPATH, "//div[@class='econ_tag_filter_category_label'][contains(text(), 'Sticker Collection')]")
    show_more_link = collection_label.find_element(
        By.XPATH, "following-sibling::div[@class='econ_tag_filter_collapsable_tags_showlink whiteLink'][contains(text(), '+ Show more')]")
    show_more_link.click()

    selectAll = driver.find_element(
        By.CLASS_NAME, "sih_button_2.sih_select_all_inventory_button")

    Cases = casesPrice()
    OBF = OBFPrice()
    OR = ORPrice()
    RMR2020 = RMR2020Price()
    S10A = S10APrice()
    SA2022 = SA2022Price()
    getText()
