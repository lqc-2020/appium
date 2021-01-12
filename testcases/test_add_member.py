
import pytest
from page.basepage import BasePage
from page.index_page import IndexPage
from page.pre_page import PrePage
from testcases.conftest import get_datas


class TestAddMember:


    @pytest.mark.parametrize("name,phone,sex",get_datas()['add']['data'],ids=get_datas()['add']['ids'])
    def test_ccc(self,name,phone,sex):
        basepage = BasePage()
        self.result = IndexPage(basepage)
        self.main = self.result.goto_address_list().goto_add_member().goto_add_member_detail().save(name,phone,sex)
        assert name == self.main