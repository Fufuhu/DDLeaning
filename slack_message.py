"""Slackにメッセージを送るためのクラス"""
import unittest
import xmlrunner
import slackweb


class SlackMessanger:
    """Slackにメッセージを送付するためのクラス"""

    def __init__(self, urls):
        self._urls = [] + urls
        self._slacks = []
        for url in self._urls:
            self._slacks.append(slackweb.Slack(url=url))

    def send_messege(self, message):
        """"Slackにメッセージを送信するメソッド"""
        for slack in self._slacks:
            slack.notify(text=message)

    def add_url(self, url):
        """メッセージ送付先のURLのリスト末尾にURLを追加"""
        self._urls = self.urls + [url]
        self._slacks.append(slackweb.Slack(url=url))

    def add_urls(self, urls):
        """メッセージ送付先のURLのちスト末尾に複数のURLを追加する"""
        self._urls = self.urls + urls
        for url in urls:
            self._slacks.append(slackweb.Slack(url=url))

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
        messanger = SlackMessanger(["null"])
        messanger.urls = url
        self.assertEqual(messanger.urls, url)

    def test_add_url(self):
        """add_urlメソッドのテスト"""
        url_to_add = "http://www.google.co.jp"
        messanger = SlackMessanger(["null"])
        messanger.add_url(url_to_add)
        urls = messanger.urls
        self.assertEqual(urls[0], "null")
        self.assertEqual(urls[1], url_to_add)


if __name__ == '__main__':
    # unittest.main()
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestSlackMessanger)
    testRunner = xmlrunner.XMLTestRunner()
    testRunner.run(suite)
