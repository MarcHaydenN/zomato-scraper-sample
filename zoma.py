import requests, bs4
import time

from selenium import webdriver

import pandas as pd

browser = webdriver.Firefox()
browser.get('http://zomato.com/mangalore/restaurants')

rests = browser.find_elements_by_css_selector("a[data-result-type='ResCard_Name']")

namelist = []
votelist = []
addresslist = []
ratinglist = []
categlist = []
costlist = []

sites = [webdriver.Firefox() for i in range(0,15)]
for i in range(0,15):
    sites[i].get(rests[i].get_attribute("href"))

    #name
    dump = sites[i].find_element_by_css_selector('.col-l-12 a')
    name = dump.text
    namelist.append(name)

    #votes
    dump = sites[i].find_element_by_css_selector("span[itemprop='ratingCount']")
    vote = dump.text
    votelist.append(vote)

    #address
    dump = sites[i].find_element_by_css_selector('.resinfo-icon > span')
    address = dump.text
    addresslist.append(address)

    #rating
    dump = sites[i].find_element_by_css_selector('.res-rating.pos-relative.clearfix.mb5 div')
    rating = dump.text[:3]
    ratinglist.append(rating)

    #category
    dump = sites[i].find_element_by_css_selector('.res-info-estabs.grey-text.fontsize3 a')
    categ = dump.text
    categlist.append(categ)

    #cost
    dump = sites[i].find_element_by_css_selector(".res-info-detail span[tabindex='0']")
    cost = dump.get_attribute('aria-label')[2:].split()[0]
    costlist.append(cost)
    
    
output = pd.DataFrame({'NAME': namelist, 'VOTES': votelist, 'ADDRESS': addresslist, 'RATING': ratinglist, 'CATEGORY': categlist, 'COST': costlist})
output.head()
output.index.name = 'id'
output.to_csv("data.csv", index=True)  

