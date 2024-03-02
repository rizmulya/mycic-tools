import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values
from cic_portal.utils.datenow import dn
from cic_portal.utils.exporter  import to_csv, to_img
import hashlib
import sys
import re