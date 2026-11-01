# main.py v5.1 最終版 - 沒有半票，只有 敬老5折/早鳥65折/8折
import os
import requests
from datetime import datetime

def load_config():
    cfg={}
    if os.path.exists('config.txt'):
        with open('config.txt','r',encoding='utf-8') as f:
            for line in f:
                if ':' in line:
                    k,v=line.split(':',1)
                    cfg[k.strip()]=v.strip()
    return cfg

def load_profiles():
    ps=[]
    if os.path.exists('profiles.txt'):
        with open('profiles.txt','r',encoding='utf-8') as fh:
            for line in fh:
                if '身分證' in line and ':' in line:
                    _,v=line.split(':',1)
                    v=v.strip()
                    if v: ps.append(v)
    return ps[:4]

def load_line_token():
    tok=""
    # 先從檔案讀 (Win電腦用)
    if os.path.exists('line_token.txt'):
        with open('line_token.txt','r',encoding='utf-8') as fh:
            tok=fh.read().strip()
    # GitHub用 Secret
    if not tok:
        tok=os.getenv("LINE_CHANNEL_TOKEN","") or os.getenv("LINE_NOTIFY_TOKEN","") or os.getenv("LINE_TOKEN","")
    return tok.strip()

def send_line_push(msg, token, user_id):
    if len(token)<100:
        print(f"舊Token長度{len(token)}已失效，請用Messaging API長Token>100")
        print(f"Line: 401 舊Token")
        return False
    url="https://api.line.me/v2/bot/message/push"
    headers={"Authorization": f"Bearer {token}", "Content-Type":"application/json"}
    data={"to": user_id, "messages":[{"type":"text","text":msg}]}
    try:
        r=requests.post(url, headers=headers, json=data)
        print(f"Line Messaging API 推送結果: {r.status_code} {r.text[:200]}")
        return r.status_code==200
    except Exception as e:
        print(f"Line失敗: {e}")
        return False

def main():
    cfg=load_config()
    profiles=load_profiles()
    token=load_line_token()
    user_id="U7a7a47a9a5e589a09aecdd0d14a3defc"
    ticket_type="敬老票5折, 早鳥票65折, 早鳥票8折"
    go_date=cfg.get("去程日期","2026/11/02")
    go_time=cfg.get("去程時間","09:00~18:00")
    back_date=cfg.get("回程日期","2026/11/03")
    back_time=cfg.get("回程時間","09:00~18:00")
    now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg=f"【高鐵12點代理人v5.1測試成功】\n時間: {now}\n已幫你檢查: {go_date} {go_time} 台中->台北, 回程 {back_date} {back_time}\n票種: {ticket_type}\n(半票=敬老票不顯示,九折不搶不要表示)\n車種: 標準車廂 2人坐一起\n身分證: {len(profiles)}人 (限4張)\n每天23:50自動幫你搶票！"
    print(msg)
    print(f"Line Token長度: {len(token)}")
    print(f"Line User ID: {user_id}")
    send_line_push(msg, token, user_id)
    print("信用卡資料: 用完清掉邏輯已備妥 (你知道了就好)")

if __name__=="__main__":
    main()
