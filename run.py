from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import requests
import json

url = "https://app.shipentegra.com/auth/login"
output_file = "sample.pdf"
gtip = "830629009000"
orders = [{"order_id":  2934849572 , "package": "small", "phone_number": "+15246985285"}]

f = open('mydata.json')
orders = json.load(f)

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Open the website
driver.get(url)

time.sleep(1)
# Find the email input field by its ID and enter the email
email_input = driver.find_element("id", "email")
email_input.send_keys("info@liviqon.com")

pass_input = driver.find_element("css selector", "#app > div.grid.lg\:grid-cols-2.overflow-hidden.h-full.text-\[\#2f3667\].dark\:text-ship-dark.dark\:bg-dark-bg > div.border-r.overflow-scroll.dark\:border-r-dark-border.lg\:ml-auto > div > div > div:nth-child(2) > form > div:nth-child(2) > div > input")
pass_input.send_keys("Sifre123")

time.sleep(1)
# Find the "Sign In" button by CSS selector and click it
sign_in_button = driver.find_element("css selector", "#app > div.grid.lg\:grid-cols-2.overflow-hidden.h-full.text-\[\#2f3667\].dark\:text-ship-dark.dark\:bg-dark-bg > div.border-r.overflow-scroll.dark\:border-r-dark-border.lg\:ml-auto > div > div > div:nth-child(2) > form > button")
sign_in_button.click()

# Wait for the page to load after signing in
time.sleep(5)

# Visit the desired URL
desired_url = "https://app.shipentegra.com/orders?page=1&status=2&limit=100"
driver.get(desired_url)

for order in orders:
    time.sleep(7)
    pass_order_id = driver.find_element("css selector", ".pr-4")
    pass_order_id.clear()
    pass_order_id.send_keys(f'{order["order_id"]}')


    search_order_id = driver.find_element("css selector", "button.duration-200:nth-child(9)")
    search_order_id.click()

    time.sleep(5)

    getinto_order = driver.find_element("css selector", ".link")
    getinto_order.click()
    time.sleep(3)
    edit_order = driver.find_element("css selector", ".tab")
    edit_order.click()

    enter_phone = driver.find_element("css selector", "#ship_to_phone")
    enter_phone.send_keys(f'{order["phone_number"]}')

    enter_content = driver.find_element("css selector", "#description")
    enter_content.send_keys("metal decor sample")

    if (order["package"] == "small"):
        enter_weight = driver.find_element("css selector", "#my_weight")
        enter_weight.send_keys("0.5")

        enter_width = driver.find_element("css selector", "#my_w")
        enter_width.send_keys("50")

        enter_height = driver.find_element("css selector", "#my_h")
        enter_height.send_keys("18")

        enter_length = driver.find_element("css selector", "#my_l")
        enter_length.send_keys("2")

        save_button = driver.find_element("css selector", "button.capitalize:nth-child(2)")
        save_button.click()

        time.sleep(3)
        checkbox_order_id = driver.find_element("css selector", "#check-body > div:nth-child(1) > input:nth-child(1)")
        checkbox_order_id.click()

        generate_label = driver.find_element("css selector", ".bg-teal-400")
        generate_label.click()

        carrier = driver.find_element("css selector", "div.py-3 > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
        carrier.send_keys("eco plus")
        carrier.send_keys(Keys.ENTER)
    else:
        enter_weight = driver.find_element("css selector", "#my_weight")
        enter_weight.send_keys("1")

        enter_width = driver.find_element("css selector", "#my_w")
        enter_width.send_keys("99")

        enter_height = driver.find_element("css selector", "#my_h")
        enter_height.send_keys("35")

        enter_length = driver.find_element("css selector", "#my_l")
        enter_length.send_keys("2")

        save_button = driver.find_element("css selector", "button.capitalize:nth-child(2)")
        save_button.click()

        time.sleep(3)
        checkbox_order_id = driver.find_element("css selector", "#check-body > div:nth-child(1) > input:nth-child(1)")
        checkbox_order_id.click()

        generate_label = driver.find_element("css selector", ".bg-teal-400")
        generate_label.click()

        carrier = driver.find_element("css selector", "div.py-3 > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
        carrier.send_keys("ups")
        carrier.send_keys(Keys.ENTER)
    enter_gtip = driver.find_element("css selector", "#gtip_number")
    enter_gtip.send_keys(gtip)
    enter_gtip.send_keys(Keys.SHIFT)
    time.sleep(6)
    create_label = driver.find_element("css selector", "button.capitalize:nth-child(2)")
    create_label.click()



    time.sleep(2)
    dropdown_order_id = driver.find_element("css selector", ".filter-actions > div:nth-child(3) > button:nth-child(1)")
    dropdown_order_id.click()

    time.sleep(1)
    pdf_link = driver.find_element("css selector", "button.dropdown-item:nth-child(1)")
    pdf_link.click()


    time.sleep(5)
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        print(driver.current_url)
        if driver.current_url.endswith(".pdf"):
            response = requests.get(driver.current_url)
            output_file = f'{order["name"]}.pdf'
            with open(output_file, "wb") as file:
                file.write(response.content)
            #os.startfile(output_file, "print")

    #obtain parent window handle
    p= driver.window_handles[0]
    #obtain browser tab window
    c = driver.window_handles[1]
    #switch to tab browser
    driver.switch_to.window(c)
    print("Page title :")
    print(driver.title)
    #close browser tab window
    driver.close()
    #switch to parent window
    driver.switch_to.window(p)
    print("Current page title:")
    print(driver.title)

    # Wait for the page to load after signing in
    time.sleep(5)

    # Visit the desired URL
    desired_url = "https://app.shipentegra.com/orders?page=1&status=2&limit=100"
    driver.get(desired_url)

# Close the browser
#driver.quit()
