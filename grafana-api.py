import requests
from urllib import parse
import pandas as pd

dashboard_url = ''
output_path = ''
cert = ''  # VPN cert if needed
tags = []  # tags to filter among anns

api_key = ''
server = ''
endpoint_path = "/api/annotations/"


def get_dashboard_id(uid):
    endpoint_path_for_dashboard = f"/api/dashboards/uid/{uid}"
    endpoint_dashboard = f'{server}{endpoint_path_for_dashboard}'
    get_dashboard = requests.get(endpoint_dashboard, auth=BearerAuth(api_key), verify=cert)
    return get_dashboard.json()['dashboard']['id']


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


url = dashboard_url
input_dict = parse.parse_qs(parse.urlsplit(url).query)

dashboard_uid = parse.urlsplit(url).path.split('/')[2]
dashboardId = get_dashboard_id(dashboard_uid)

from_p = input_dict['from'][0]
to_p = input_dict['to'][0]

endpoint = f'{server}{endpoint_path}?orgId=1&from={from_p}&to={to_p}&tags={tags[0]}&dashboardId={dashboardId}'
r = requests.get(endpoint, auth=BearerAuth(api_key), verify=cert)
ann = r.json()
