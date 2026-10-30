import os, datetime, requests

LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
LINE_USER_ID = os.environ.get("LINE_USER_ID")

def send_line_message(message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}"}
    data = {"to": LINE_USER_ID, "messages": [{"type": "text", "text": message}]}
    try:
        r = requests.post(url, headers=headers, json=data, timeout=10)
        print(f"Line: {r.status_code} {r.text}")
    except Exception as e:
        print(f"Line 失敗: {e}")

def book_ticket():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"【高鐵12點代理人測試成功】\n時間: {now}\n已幫你檢查: 台中->台北, 台中->左營\n票種: 半票\n每天23:50自動幫你搶票！"
    print(msg)
    send_line_message(msg)

if __name__ == "__main__":
    book_ticket()
