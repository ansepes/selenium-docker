

from utils.page_base import PageBase
from utils.selenium_util import SeleniumUtil


class TestApp:

  def test_login_pc(self):
    selenium = None
    try:
      selenium = SeleniumUtil()

      # - ドライバーの初期化
      selenium.build_pc_driver()

      page = LoginPagePC(selenium)
      page.open()
      print(selenium.driver().current_url)

    finally:
      if selenium:
        selenium.dispose_driver()


class LoginPagePC(PageBase):
  def __init__(self, selenium):
    super().__init__(selenium,
                     url='http://mail.google.com/mail/?logout&hl=ja')
