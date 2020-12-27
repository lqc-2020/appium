from page.app import App
import pytest
from page.basepage import BasePage
from testcases.conftest import get_datas


class TestAddMember:
    @pytest.mark.parametrize("name,phone,sex",get_datas()['add']['data'])
    def test_ccc(self,name,phone,sex):
        self.app = App()
        self.main = self.app.start().goto_index_page().goto_address_list().goto_add_member().goto_add_member_detail().save(name,phone,sex)
        self.result = BasePage()
        assert '添加成功' in self.result.res()