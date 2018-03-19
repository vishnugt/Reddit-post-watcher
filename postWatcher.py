import praw
import time
import requests
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

reddit = praw.Reddit(	client_id = 'jzqAK8qLxvZcLQ',
						client_secret = 'wd5Cv9Sko6tjdSWlqPOnztGkeB0',
						username = 'none',
						password = 'none',
						user_agent = 'TestingAPi')

id_list = []

subredditsName = []
subredditsName.append('GameDeals')
subredditsName.append('GiftOfGames')
#subreddit.add(reddit.subreddit('SteamGameSwap'))

def sendMail(submission, subredditsName):
	print ("init")
	return requests.post(
	"https://api.mailgun.net/v3/mg.melii.club/messages",
	auth=("api", "key-hidden"),
	data={"from": "Reddit Bot <mailgun@mg.melii.club>",
	"to": ["vishnugt95@gmail.com"],
	"subject": ("["+ subredditName + "] " + submission.title).encode('ascii', 'ignore').decode('ascii'),
	"text": submission.url + "\n\n" + submission.selftext})


while(True):
	for subredditName in subredditsName:
		subredditObj = reddit.subreddit(subredditName)
		topNew = subredditObj.new(limit=5)
		for submission in topNew:
			if not submission.stickied:
				if submission.id not in id_list:
					print(("["+ subredditName + "] " + submission.title).encode('ascii', 'ignore').decode('ascii'))
					sendMail(submission, subredditName)
					print "done"
					print "****\n"
					id_list.append(submission.id)
	time.sleep(30) #30 seconds





