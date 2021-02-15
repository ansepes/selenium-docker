from utils.selenium_util import SeleniumUtil
from utils.page_base import PageBase
# import sys


def handler(event, context):
  #   return 'Hello from AWS Lambda using Python' + sys.version + '!'
  selenium = None
  try:
    selenium = SeleniumUtil()

    # - ドライバーの初期化
    selenium.build_pc_driver()

    page = LoginPagePC(selenium)
    page.open()
    # print(selenium.driver().current_url)
    return selenium.driver().current_url

  finally:
    if selenium:
      selenium.dispose_driver()


class LoginPagePC(PageBase):
  def __init__(self, selenium):
    super().__init__(selenium,
                     url='http://mail.google.com/mail/?logout&hl=ja')
