from test_requests.test_wework.api.groupchat import GroupChat
from test_requests.test_wework.api.wework import WeWork


class TestWework:

    @classmethod
    def setup_class(cls):
        cls.groupchat = GroupChat()
        # cls.token = WeWork.get_token(cls.secret)


