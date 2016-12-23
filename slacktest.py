"""Slack test script"""
import sys
import slackweb

ARGS = sys.argv
URL = ARGS[1]
MESSAGE = "This is a test message from (slacktest.py)"

SLACK = slackweb.Slack(url=ARGS[1])
SLACK.notify(text=MESSAGE)
