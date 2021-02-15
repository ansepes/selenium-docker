
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

SP_UA = (
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) '
    'AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/85.0.4183.109 Mobile/15E148 Safari/604.1')
WAIT_TIMEOUT = 10


class SeleniumUtil:
  def __init__(self):
    self._driver = None

  def build_pc_driver(self):
    options = Options()
    self.__build_driver(options)

  def build_sp_driver(self):
    options = Options()
    # UAをスマホのUAに変更する
    options.add_argument(f'--user-agent={SP_UA}')
    self.__build_driver(options)

  def __build_driver(self, options):
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    # 証明書の警告をOFFにする
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptInsecureCerts'] = True

    # ファイルダウンロードディレクトリ設定、PDFは常にダウンロード設定
    # options.add_experimental_option("prefs", {
    #     "download.default_directory": os.environ['DIR_NAME'],
    #     "plugins.always_open_pdf_externally": True,
    #     "safebrowsing_for_trusted_sources_enabled": False,
    # })

    self._driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options,
        desired_capabilities=capabilities,
    )

    # headlessモードでのファイルダウンロード設定
    # self._driver.command_executor._commands["send_command"] = (
    #     "POST",
    #     '/session/$sessionId/chromium/send_command'
    # )
    # params = {
    #     'cmd': 'Page.setDownloadBehavior',
    #     'params': {
    #         'behavior': 'allow',
    #         'downloadPath': os.environ['DIR_NAME']
    #     }
    # }
    # self._driver.execute("send_command", params=params)

    # waitの初期化
    self._wait = WebDriverWait(self._driver, WAIT_TIMEOUT)

  def driver(self):
    if not self._driver:
      return None

    return self._driver

  def waiter(self):
    return self._wait

  def wait_time(self):
    return WAIT_TIMEOUT

  def dispose_driver(self):
    if not self._driver:
      return

    self._driver.quit()
    self._driver = None
