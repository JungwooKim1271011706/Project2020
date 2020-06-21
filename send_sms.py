import pandas as pd
import tkinter
from tkinter import filedialog
from datetime import datetime, date, timedelta
from dateutil.parser import parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

vendorpia_url = "www.vendorpia.com"
driver = 