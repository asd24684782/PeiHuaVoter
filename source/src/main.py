import os

from model.Voter import Voter
from model.SettingManager import SettingManager


def main():
    SettingManager('./setting/setting.yml')
    settingMgr = SettingManager.getInstance()
    loginURL = settingMgr.setting['url']['login']
    voteURLs = settingMgr.setting['url']['votes']
    users    = settingMgr.setting['email']

    voter = Voter()
    for email, password in users.items():
        voter.loginPeiHua(
            url=loginURL, 
            email=email, 
            password=password
        )
        for url in voteURLs:
            voter.vote(url)

        voter.resetBrowser()


if __name__ == '__main__':
    main()