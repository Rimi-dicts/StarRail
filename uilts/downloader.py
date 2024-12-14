from time import sleep

import requests
from bs4 import BeautifulSoup


def getSoup(url: str):
    sleep(1)
    html = requests.get(url, "lxml")
    html.encoding = "utf-8"
    return BeautifulSoup(html.text, features="lxml")


class Downloader:
    def __init__(self, fp):
        self.outFile = open(fp, "w", encoding="utf-8")

    def getAll(self):
        self.getCharacterName()
        self.getWeaponName()
        self.getEnemyName()
        self.getResourceName()
        self.getConsumablesName()
        self.getItemName()
        self.getDecorationName()
        self.getNPCName()
        self.getNounName()
        # self.getNounInfoName()
        self.outFile.close()

    def getCharacterName(self):
        resList = (
            getSoup("https://wiki.biligame.com/sr/%E8%A7%92%E8%89%B2%E5%9B%BE%E9%89%B4")
            .select("#CardSelectTr > div > div > div > div"))

        resList.extend(
            getSoup("https://wiki.biligame.com/sr/%E6%9C%AA%E5%AE%9E%E8%A3%85")
            .select("#mw-content-text > div > div > div > div > font > b"))

        print("获取光锥完毕")
        self.outFile.write("# 角色列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getWeaponName(self):
        resList = (
            getSoup("https://wiki.biligame.com/sr/%E5%85%89%E9%94%A5%E5%9B%BE%E9%89%B4")
            .select("#CardSelectTr > div > div > div.weapon-name > a"))

        print("获取光锥完毕")
        self.outFile.write("# 光锥列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getEnemyName(self):
        resList = (
            getSoup("https://wiki.biligame.com/sr/%E6%95%8C%E4%BA%BA%E7%AD%9B%E9%80%89")
            .select("#CardSelectTr > tbody > tr > td:nth-child(2) > a"))

        print("获取敌人完毕")
        self.outFile.write("# 敌人列表\n")
        for item in resList:
            text = item.text.replace("（完整）","")
            self.outFile.write("{0}\n".format(text))

    def getResourceName(self):
        resList = (
            getSoup("https://wiki.biligame.com/sr/%E6%9D%90%E6%96%99%E7%AD%9B%E9%80%89")
            .select("#CardSelectTr > tbody > tr > td:nth-child(2) > a"))

        print("获取材料完毕")
        self.outFile.write("# 材料列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getConsumablesName(self):
        resList = (
            getSoup("https://wiki.biligame.com/sr/%E6%B6%88%E8%80%97%E5%93%81%E7%AD%9B%E9%80%89")
            .select("#CardSelectTr > tbody > tr > td:nth-child(2) > a"))

        print("获取消耗品完毕")
        self.outFile.write("# 消耗品列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getItemName(self):
        resList = (
            getSoup("https://wiki.biligame.com/sr/%E9%81%93%E5%85%B7%E7%AD%9B%E9%80%89")
            .select("#CardSelectTr > tbody > tr > td:nth-child(2) > a"))

        print("获取道具完毕")
        self.outFile.write("# 道具列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getDecorationName(self):
        resList = (
            getSoup("https://wiki.biligame.com/sr/%E8%A3%85%E9%A5%B0%E4%B8%80%E8%A7%88")
            .select("#CardSelectTr > tbody > tr > td:nth-child(2) > a"))

        print("获取装饰完毕")
        self.outFile.write("# 装饰列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getNPCName(self):
        resList = (
            getSoup("https://wiki.biligame.com/sr/NPC")
            .select("#CardSelectTr > tbody > tr > td:nth-child(2) > a"))

        print("获取NPC完毕")
        self.outFile.write("# NPC列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getNounName(self):
        list = [
            "星海纪闻",
            "星穹列车",
            "空间站「黑塔」",
            "雅利洛-Ⅵ",
            "仙舟「罗浮」",
            "匹诺康尼",
            # "星神",
            "派系",
            "专有名词",
            # "互动文本",
            # "过场提示"
        ]

        resList = []

        for part in list:
            soup = getSoup("https://wiki.biligame.com/sr/{0}".format(part))
            resList.extend(soup.select("#mw-content-text > div > div.toc-sticky.row > div.col-lg-9.col-md-9.col-sm-8.col-xs-12 > h3 > span:nth-child(2)"))
            resList.extend(soup.select("#mw-content-text > div > div.toc-sticky.row > div.col-lg-9.col-md-9.col-sm-8.col-xs-12 > h4 > span:nth-child(2)"))


        print("获取专有名词完毕")
        self.outFile.write("# 专有名词列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getNounInfoName(self):
        resList = (
            getSoup("https://wiki.biligame.com/sr/%E4%B8%93%E6%9C%89%E5%90%8D%E8%AF%8D")
            .select("#mw-content-text > div > div.toc-sticky.row > div.col-lg-9.col-md-9.col-sm-8.col-xs-12 > table > tbody > tr > td"))

        print("获取专有名词介绍完毕")
        self.outFile.write("# 专有名词介绍列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))
