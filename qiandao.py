import datetime
import time
import random

import requests
from datetime import datetime, timedelta
import schedule


def days_difference():
    target_date = datetime(2023, 8, 25)
    current_date = datetime.now()
    difference = (current_date - target_date).days
    return difference


def signXiaoGuanJia():
    difference_days = days_difference()
    daily = 2106 + difference_days
    referer = 'https://servicewechat.com/wx23d8d7ea22039466/' + str(daily) + '/page-frame.html'
    daka_day = datetime.now().strftime('%Y-%m-%d')
    timess = datetime.now()
    print(timess)
    print(daka_day)
    times = current_timestamp_ms = int(time.time() * 1000)
    # 构建请求头
    headers = {
        "Host": "a.welife001.com",
        "Connection": "keep-alive",
        "Content-Length": "1914",
        "imprint": "oWRkU0RmtiMTvRRUMZHI30vTZCg0",
        "xweb_xhr": "1",
        "Authorization": "mock_oWRkU0RmtiMTvRRUMZHI30vTZCg0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8379",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": referer,
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh"
    }
    # 构建请求数据
    data = {
      "extra": 1,
      "id": "65d6f45ecb51c8555f311161",
      "daka_day": daka_day,
      "submit_type": "submit",
      "networkType": "wifi",
      "member_id": "64d8863e527beed503cb9b58",
      "op": "add",
      "invest": {
        "is_tmp": False,
        "is_private": True,
        "_id": "65d6f45d3df5895558437d65",
        "subject": [
          {
            "seq": 0,
            "cate": 0,
            "inputs_count": 0,
            "_id": "65d6f45d3df5895558437d66",
            "rule": None,
            "inputs": [],
            "title": "今日是否在校在寝",
            "required": True,
            "item_details": [
              {
                "seq": 0,
                "checks_count": 0,
                "rate": 0,
                "_id": "65d6f45d3df5895558437d67",
                "name": "是",
                "file": [],
                "checkedlist": [],
                "checked": True
              },
              {
                "seq": 1,
                "checks_count": 0,
                "rate": 0,
                "_id": "65d6f45d3df5895558437d68",
                "name": "否",
                "file": [],
                "checkedlist": [],
                "checked": False
              }
            ],
            "limitMaxSelect": None,
            "hasSplicing": None,
            "hasWaterMark": None,
            "valid": True
          },
          {
            "seq": 1,
            "cate": 4,
            "inputs_count": 0,
            "_id": "65d6f45d3df5895558437d69",
            "rule": None,
            "inputs": [],
            "title": "请上传地理位置",
            "required": True,
            "item_details": [
              {
                "seq": 0,
                "checks_count": 0,
                "rate": 0,
                "_id": "65d6f45d3df5895558437d6a",
                "name": "可在500米范围内微调",
                "file": [],
                "checkedlist": []
              }
            ],
            "limitMaxSelect": None,
            "hasSplicing": None,
            "hasWaterMark": None,
            "input": {
              "content": "{\"title\":\"大连海事大学网络信息中心\",\"address\":\"辽宁省大连市甘井子区凌海路1号\",\"location\":[121.533116,38.868265]}"
            },
            "valid": True
          },
          {
            "seq": 2,
            "cate": 0,
            "inputs_count": 0,
            "_id": "65d6f45d3df5895558437d6b",
            "rule": None,
            "inputs": [],
            "title": "是否有其他事宜与指导员沟通",
            "required": True,
            "item_details": [
              {
                "seq": 0,
                "checks_count": 0,
                "rate": 0,
                "_id": "65d6f45d3df5895558437d6c",
                "name": "无",
                "file": [],
                "checkedlist": [],
                "checked": True
              },
              {
                "seq": 1,
                "checks_count": 0,
                "rate": 0,
                "_id": "65d6f45d3df5895558437d6d",
                "name": "有，请联系18018980764/0411-84723389",
                "file": [],
                "checkedlist": [],
                "checked": False
              }
            ],
            "limitMaxSelect": None,
            "hasSplicing": None,
            "hasWaterMark": None,
            "valid": True
          }
        ],
        "create_at": "2024-02-22T07:14:37.632Z",
        "update_at": "2024-02-22T07:14:37.632Z",
        "__v": 0,
        "time": 1709042112160,
        "day": "daka_day"
      },
      "feedback_text": ""
    }

    # 发送 POST 请求
    url = "https://a.welife001.com/applet/notify/feedbackWithOss"
    response = requests.post(url, json=data, headers=headers)

    # 处理响应
    if response.status_code == 200:
        response_data = response.json()
        print("响应数据：", response_data)
    else:
        print("请求失败，状态码：", response.status_code)


if __name__ == "__main__":

    target_hour = random.randint(12, 16)  # 设置目标执行的小时
    target_minute = random.randint(0, 59)  # 设置目标执行的分钟
    target_second = random.randint(0, 59)
    target_now = datetime.now()
    target_time = datetime(target_now.year, target_now.month, target_now.day, target_hour, target_minute, target_second)
    signXiaoGuanJia()
    while True:
        now = datetime.now()
        if now >= target_time:
            signXiaoGuanJia()
            # 等待到明天同一时间点
            target_hour = random.randint(12, 16)  # 设置目标执行的小时
            target_minute = random.randint(0, 59)  # 设置目标执行的分钟
            target_second = random.randint(0, 59)
            target_now = datetime.now()
            target_time = datetime(target_now.year, target_now.month, target_now.day, target_hour, target_minute,
                                   target_second)
            target_time += timedelta(days=1)
            print(target_time)
        time.sleep(600)
