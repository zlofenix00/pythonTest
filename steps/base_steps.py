from pages.bbc_page import BBCPage
from utils import classproperty


class BaseSteps:

    @classproperty
    def bbc_page(cls):
        return BBCPage
