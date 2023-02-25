import requests 
import smtplib
from bs4 import BeautifulSoup


#url of the product you want to monitor
url = 'https://www.bestbuy.ca/en-ca/product/benq-mobiuz-24-5-fhd-165hz-1ms-ips-lcd-freesync-gaming-monitor-ex2510s/15596019'


#maximum price you are willing to pay for said product
maxPrice = 245

#set up email parameters 
senderEmail = 'thepythonpricemonitor@gmail.com'
senderPassword = 'Russianvodka44'
receiverEmail = 'nicolas.a.vicente44@gmail.com'

#send an http request to the website and get the html
response = requests.get(url)

#use beautifulsoup to parse the html and find the element that contains the price
soup = beautifulsoup(response.content, 'html.parser')



#price element on the page your are attempting to monitor
priceElement = soup.find('div', {'class': 'price_2j8lL'})




# Extract the price from the HTML element and convert it to a float
price = float(priceElement.text.replace('$', '').replace(',', ''))

#check if the price is lower than the maximum price you are will to pay
if price < maxPrice:
    #set up the email message
    message = f'The price of the product is now ${price:.2f}!'
    subject = 'PRICE ALERT!'
    body = f'Subject: {subject}\n\n{message}'
    
    
    #log in to the sender email account and send the email\
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(senderEmail, senderPassword)
        server.sendmail(senderEmail, receiverEmail, body)

