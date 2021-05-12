import requests

from test_requests.test_wework.api.wework import WeWork


class GroupChat(WeWork):
    secret = "vWd15kraOixlp5uq4dUbf9bTFRb7fcRjVrFh8bUga-8"

    def list(self, limit=50, **kwargs):
        json_data = {"limit": limit}
        # print(kwargs)
        # print(json_data)
        json_data.update(kwargs)
        # print(json_data)
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret)},
            json=json_data
        )
        WeWork.fotmat(r)
        # print(json.dumps(r.json(), indent=3))

        return r.json()

    def get(self, chat_id):
        detail_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get"
        r = requests.post(
            detail_url,
            params={"access_token": self.get_token(self.secret)},
            json={"chat_id": chat_id}
        )
        WeWork.fotmat(r)
        # print(json.dumps(r.json(), indent=3))
        return r.json()


