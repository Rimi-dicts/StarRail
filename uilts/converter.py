import re

import jieba
import pypinyin


class Converter:
    def __init__(self, ifn, ofn, info):
        self.inputFile = ifn
        self.outputFile = ofn
        self.info = info
        self.defaultWeight = 999

    def readAndSplit(self, fp: str) -> list[str]:
        with open(fp, encoding="utf-8") as f:
            lines = f.read().split("\n")
            # res = []
            # for line in lines:
            #     if len(line) > 16:
            #         res += jieba.cut_for_search(line)
            #     else:
            #         res.append(line)
            return lines

    def getPinyinAndWeight(self, contents: list[str]):
        sentences: dict[str, tuple[str, int]] = {}
        for word in contents:
            if word := word.strip():
                if word not in sentences.keys():
                    if word.startswith("#"):
                        continue
                    pinyin = pypinyin.slug(word, separator=" ")
                    pattern1 = r"[^a-z\s]\s|\s[^a-z\s]|[^a-z\s]"
                    pinyin = re.sub(pattern1, "", pinyin)
                    sentences[word] = (pinyin, self.defaultWeight)
                sentences[word] = (sentences[word][0], sentences[word][1] + 1)
        return sentences

    def output(self, sentences: dict[str, tuple[str, int]], fp: str):
        print("共获取到{0}个词条".format(len(sentences.items())))
        with open(fp, "w", encoding="utf-8") as f:
            f.write("# Rime dictionary\n"
                    "# encoding: utf-8")
            f.write(
                "\n---"
                "\nname: {0}".format(self.info.get("name")) +
                "\nversion: \"{0}\"".format(self.info.get("version")) +
                "\nsort: {0}".format(self.info.get("sort")) +
                "\n...\n")
            f.write("\n".join(f"{i}\t{j}\t{k}" for i, (j, k) in sentences.items()))

    def generate(self):
        self.output(self.getPinyinAndWeight(self.readAndSplit(self.inputFile)), self.outputFile)
