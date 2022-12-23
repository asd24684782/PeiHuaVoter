# -*- coding: UTF-8 -*-
import yaml #pyyaml package
import json
import logging

from pathlib import Path

logger = logging.getLogger()

def writeYAML(dataDict,filePath):
    # override existing file
    with open(filePath, 'w') as file:
        yaml.dump(dataDict, file)

def parseYAML(filePath):

    # Process Config Files
    conf = Path(filePath)
    if conf.exists():
        with open(filePath, 'r') as file:
            yamlConfig = yaml.load(file, Loader=yaml.FullLoader)
            return yamlConfig
    else:
        logger.warning(f'Config file :[{filePath}] does not exist')
        return None


def mergeYAML(userYamlFile, defaultYamlFile):
    userYaml = parseYAML(userYamlFile)
    deftYaml = parseYAML(defaultYamlFile)
    '''
    userYaml = {
        "a":3,
        "b":9,
        'D':'removed'
    }

    deftYaml = {
        "a":5,
        "b":{
            "z1" : "z12",
            "z2" : "z23"
        },
        "c": ['k','i','l','o']
    }
    '''
    print('userYaml')
    print(json.dumps(userYaml,indent=4))
    print("##########################")
    print('deftYaml')
    print(json.dumps(deftYaml, indent=4))
    print("##########################")
    print('merge yaml')
    fd = mergeDict(userYaml,deftYaml)
    print(json.dumps(fd, indent=4))



def mergeDict(userDict, deftDict):
    rtnDict = dict()
    for key, value in deftDict.items():
        userValue = userDict.get(key)
        if type(userValue) == type(value):
            if isinstance(value, dict):
                rtnDict[key] = mergeDict(userValue, value)
            rtnDict[key] = value
        else:
            rtnDict[key] = mergeValue(userValue, value)
    return rtnDict


def mergeValue(userValue, deftValue):
    if userValue == None:
        return deftValue
    if type(userValue) == type(deftValue):
        return userValue
    
    return deftValue



#mergeYAML("/home/ubuntu/projects/v4/maskengine/conf/config.yml","/var/lib/touchcloud/volumes/maskEngine/config.yml")


