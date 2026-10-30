
import os, time, datetime, requests
from apscheduler.schedulers.blocking import BlockingSchedule

# ========= 你的兩個鑰匙貼在這裡 =========
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
LINE_USER_ID = os.environ.get("LINE_USER_ID")

CONFIG = {
    "routes": ["台中->台北", "台中->左營"],
    "passengers": 1,
    "discount": "半票",
    "time_range": "07:00-10:00"
}

def send_line_message(message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}"}
    data = {"to": LINE_USER_ID, "messages": [{"type": "text", "text": message}]}
    try:
        r = requests.post(url, headers=headers, json=data, timeout=10)
        print(f"Line通知結果: {r.status_code}")
        return r.status_code == 200
    except Exception as e:
        print(f"Line發送失敗: {e}")
        return False

def check_and_book():
    now = datetime.datetime.now()
    print(f"[{now}] 12點代理人啟動，開始檢查高鐵票...")
    target_date = now.date() + datetime.timedelta(days=28)
    for route in CONFIG["routes"]:
        print(f"正在查詢 {route} {target_date} {CONFIG['time_range']} 優惠票...")
        has_ticket = True
        if has_ticket:
            message = f"🎉 幫你搶到了！\n路線：{route}\n日期：{target_date}\n時間：{CONFIG['time_range']} \n張數：{CONFIG['passengers']}張\n票種：{CONFIG['discount']}\n\n訂位代號：123456 (範例)\n請在今日10:00前至超商付款"
            send_line_message(message)
            break
    print("本輪搶票結束")

if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone="Asia/Taipei")
    scheduler.add_job(check_and_book, 'cron', hour=23, minute=59, second=50)
    print("已排程：每天23:59:50 自動搶票")
    scheduler.start()
CONFIG = {
    "routes": ["台中->台北", "台中->左營"],
    "passengers": 1,
    "discount": "半票",
    "time_range": "07:00-10:00"
}

def send_line_message(message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}"}
    data = {"to": LINE_USER_ID, "messages": [{"type": "text", "text": message}]}
    try:
        r = requests.post(url, headers=headers, json=data, timeout=10)
        print(f"Line通知結果: {r.status_code}")
        return r.status_code == 200
    except Exception as e:
        print(f"Line發送失敗: {e}")
        return False

def check_and_book():
    now = datetime.datetime.now()
    print(f"[{now}] 12點代理人啟動，開始檢查高鐵票...")
    target_date = now.date() + datetime.timedelta(days=28)
    for route in CONFIG["routes"]:
        print(f"正在查詢 {route} {target_date} {CONFIG['time_range']} 優惠票...")
        has_ticket = True
        if has_ticket:
            message = f"🎉 幫你搶到了！\n路線：{route}\n日期：{target_date}\n時間：{CONFIG['time_range']} \n張數：{CONFIG['passengers']}張\n票種：{CONFIG['discount']}\n\n訂位代號：123456 (範例)\n請在今日10:00前至超商付款"
            send_line_message(message)
            break
    print("本輪搶票結束")

if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone="Asia/Taipei")
    scheduler.add_job(check_and_book, 'cron', hour=23, minute=59, second=50)
    print("已排程：每天23:59:50 自動搶票")
    scheduler.start()
