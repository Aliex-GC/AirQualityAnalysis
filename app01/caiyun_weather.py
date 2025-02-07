from __future__ import annotations

import json
import requests

city_centers = json.load(open('city_centers.json', 'r', encoding='utf-8'))
city_data = json.load(open('city_data.json', 'r', encoding='utf-8'))


def get_city_position_by_name(city_name: str) -> None | dict:
    res = list(filter(lambda city: city_name in city['city'], city_centers))
    if len(res) > 0:
        return res[0]
    return None


def get_comprehensive_url(token: str, longitude, latitude):
    return (
        f"https://api.caiyunapp.com/v2.6/TAkhjf8d1nlSlspN/{longitude},{latitude}/weather?"
        f"alert=true&"
        f"dailysteps=3&"
        f"hourlysteps=24&"
        f"token={token}"
    )


def get_weather(lon=120.35, lan=30.31) -> dict | int:
    """
    :return: dict 天气查询结果 , int 天气查询失败后的代码
    """
    response = requests.get(get_comprehensive_url("mkhvpq9w0AsN6gjl", lon, lan))
    if response.status_code == 200:
        resp_data = response.text
        return dict(json.loads(resp_data))
    return response.status_code
