# Author(s): Jason Page
# Date: 5/10/2024
# Description: This file is the main file for the program. It will run the program and call the necessary functions to track social media sentiment.

import os, sys, time
from sentiment import Sentiment
from twitter import Twitter
from reddit import Reddit
from database import Database
from datetime import datetime

