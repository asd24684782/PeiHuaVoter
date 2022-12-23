# -*- coding: UTF-8 -*-
import logging
import json
import util.YamlUtil


logger = logging.getLogger()

class SettingManager:

    __instance = None

    @staticmethod
    def getInstance():
        if SettingManager.__instance == None:
            SettingManager()
        return SettingManager.__instance
        
    def __init__(self, filePath):
        if SettingManager.__instance != None:
            raise Exception("SettingManager class is a singleton!")
        else:
            self.__setting = util.YamlUtil.parseYAML(filePath)
            SettingManager.__instance = self
            #print(json.dumps(self.setting,indent=4))
    
    @property
    def setting(self):
        return self.__setting