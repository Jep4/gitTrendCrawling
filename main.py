# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import re
import csv
import requests
import urllib.request as ur
import numpy as np
from bs4 import BeautifulSoup as bs


def findName():
    url = 'https://github.com/trending'
    html = ur.urlopen(url)
    reformat = bs(html.read(), 'html.parser')
    j=""
    for i in reformat.find_all('h1', {"h3 lh-condensed"}):
        i = i.text
        i = str(i).replace("\n", "")
        j = j+i

    w = sen2word(j)
    print(w)

def findDesc():
    url = 'https://github.com/trending'
    html = ur.urlopen(url)
    reformat = bs(html.read(), 'html.parser')
    j=""
    for i in reformat.find_all('p', {"col-9 color-fg-muted my-1 pr-4"}):
        i = i.text
        i = str(i).replace("\n", "")
        j = j+i

    w = sen2word(j)
    print(w)


def sen2word(j):
    w = j.split()
    return w


def main():
    findName()
    findDesc()


if __name__ == "__main__":
    main()
