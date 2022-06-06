from steps.base_steps import BaseSteps


class BBCSteps(BaseSteps):

    @classmethod
    def open_main_page(cls):
        cls.bbc_page().open()
        cls.bbc_page().check_site_title()


