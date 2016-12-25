"""Slackにメッセージを送るためのクラス"""
import unittest
import slackweb


class SlackMessanger:
    """Slackにメッセージを送付するためのクラス"""

    def __init__(self, urls):
        self._urls = [] + urls
        for url in self._urls:
            self._slacks = [] + slackweb.Slack(url=url)

    def send_messege(self, message):
        """"Slackにメッセージを送信するメソッド"""
        for slack in self._slacks:
            slack.notify(text=message)

    def add_url(self, url):
        """メッセージ送付先のURLのリスト末尾にURLを追加"""
        self._urls = self.urls + [url]

    def add_urls(self, urls):
        """メッセージ送付先のURLのちスト末尾に複数のURLを追加する"""
        self._urls = self.urls + [urls]

    def _get_urls(self):
        """メッセージ送付先のURLのリストを取得するメソッド"""
        return self._urls

    def _set_urls(self, urls):
        """メッセージ送付先のURLのリストを指定するメソッド"""
        self._urls = urls

    urls = property(_get_urls, _set_urls)


class TestSlackMessanger(unittest.TestCase):
    """SlackMessangerをテストするためのクラス"""

    def test_url(self):
        """URLが正しく設定可能かをチェックする。"""

        url = ["test_url"]
        messanger = SlackMessanger("null")
        messanger.urls = url
        self.assertEqual(messanger.urls, url)


if __name__ == '__main__':
    unittest.main()
