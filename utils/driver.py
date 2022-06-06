from selenium import webdriver
from selenium.common import JavascriptException
from selenium.webdriver.chrome.options import Options


class WebdriverSubWrapper:
    def cast_async_js(self, js_command, *args):
        response = self.execute_async_script(js_command, *args)
        return response

    def cast_js(self, js_command, *args):
        try:
            response = self.execute_script(js_command, *args)
        except JavascriptException as err:
            raise JavascriptException(f"Failed JS command: {js_command}\n{err}")
        except Exception as err:
            raise JavascriptException(f"Unexpected error in command: {js_command}\n{err}") from err
        return response

    def set_offline(self, offline):
        conditions = {"offline": offline, "latency": 0, "throughput": 500 * 1024}
        self.set_network_conditions(**conditions)


class WebdriverChromeWrapper(WebdriverSubWrapper, webdriver.Chrome):
    pass


class DriverCreator:
    _instance = None
    _test_name = None

    def __call__(self, settings=None):
        if DriverCreator._instance is None:
            DriverCreator._instance = self._create_driver(settings)
        return DriverCreator._instance

    @staticmethod
    def _create_driver(settings=None):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-site-isolation-trials")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-infobars")
        options.add_argument("--homepage=about:blank")
        desired_capabilities = {}
        desired_capabilities.update({"acceptSslCerts": True, "acceptInsecureCerts": True})
        desired_capabilities["goog:loggingPrefs"] = {"browser": "WARNING", "driver": "WARNING", "performance": "ALL"}
        instance = WebdriverChromeWrapper(desired_capabilities=desired_capabilities, options=options)
        return instance

    @classmethod
    def destroy_instance(cls):
        del cls._instance
        cls._instance = None

    @classmethod
    def assign_instance(cls, driver):
        cls._instance = driver

    @property
    def webdriver(self):
        return self._instance


Driver = DriverCreator()
