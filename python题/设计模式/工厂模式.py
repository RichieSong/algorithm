# coding:utf-8
import json
import xml.etree.ElementTree as etree

class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data
class XMLConnector:
    def __init__(self,fitepath):
        self.tree = etree