# PeiHuaVoter 全聯佩華投票機器人

## 設定
設定檔 `exe/setting/setting.yml`
```
---
url: 
  login: https://youthdream.phdf.org.tw/socialite/redirect/google/member.login?openExternalBrowser=1
  votes:
    - https://youthdream.phdf.org.tw/project/show?page=4
    - https://youthdream.phdf.org.tw/project/show?page=11

email:
  username1: password1
  username2: password2
```

### 投票頁面
votes放要投票的頁面
### 帳號密碼
email下可以放多組帳號密碼 `帳號:密碼`

## 啟動
執行`main.exe`
