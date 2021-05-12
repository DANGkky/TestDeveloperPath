import datetime
import json

import requests


class WeWork:
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corp_id = "wweee5d5707ac238a9"
    token = dict()

    @classmethod
    def get_token(cls, secret=None):
        # 避免重复请求，提高速度
        # if secret is None:
        #     return cls.token[secret]
        if secret not in cls.token.keys():
            r = requests.get(cls.token_url, params={"corpid": cls.corp_id, "corpsecret": secret})
            # assert r.json()["errcode"] == 0
            # print(r.json())
            # print(r.json()["expires_in"])
            # cls.fotmat(r)
            cls.token[secret] = r.json()["access_token"]
            # cls.token_time[secret] = datetime.now()
        return cls.token[secret]

    @classmethod
    def fotmat(cls, data):
        print(json.dumps(data.json(), indent=3))
