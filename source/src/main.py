import os

from model.Voter import Voter
from model.SettingManager import SettingManager


if __name__ == '__main__':
    SettingManager('./setting/setting.yml')
    settingMgr = SettingManager.getInstance()
    loginURL = settingMgr.setting['url']['login']
    voteURLs = settingMgr.setting['url']['votes']
    users    = settingMgr.setting['email']

    for email, password in users.items():
        voter = Voter()
        voter.loginGoogle(
            url=loginURL, 
            email=email, 
            password=password
        )
        for url in voteURLs:
            voter.vote(url)

        del voter