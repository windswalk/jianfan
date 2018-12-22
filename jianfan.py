# coding=utf-8
import codecs
import sys


class JianFan(object):

    def load_file(self, file):
        f = codecs.open(file, "r", "utf-8")
        content = f.read()
        f.close()
        return content

    def map_all(self, src_str, dst_str, src_char, n_start=0):
        n = src_str.find(src_char, n_start)
        char_list = []
        if n >= 0:
            try:
                dst_str[n]
            except IndexError:
                pass
            else:
                dst_char = dst_str[n]
                map_next = self.map_all(src_str, dst_str, src_char, n+1)
                return map_next + [dst_char]
        return char_list

    def zi_fan(self, char):
        return self.map_all(self.s_dup(), self.t_dup(), char)

    def zi_jian(self, char):
        return self.map_all(self.t_dup(), self.s_dup(), char)

    def s_dup(self):
        return self.load_file("txt/s/s_dup_char.txt")

    def t_dup(self):
        return self.load_file("txt/t/t_dup_char.txt")

    def s(self):
        return self.load_file("txt/s/s.txt")

    def t(self):
        return self.load_file("txt/t/t.txt")

    def convert(self, str, src, dst):
        for n in range(0, len(src)):
            src_char = src[n]
            dst_char = dst[n]
            str = str.replace(src_char, dst_char)
        return str

    def fan(self, str):
        return self.convert(str, self.s(), self.t())

    def jian(self, str):
        return self.convert(str, self.t(), self.s())


def jian(str):
    return JianFan().jian(str)


def fan(str):
    return JianFan().fan(str)


def main():
    doc = '''jianfan.py
\t-fan\t简转繁\t\t如:jianfan.py -fan 简繁转换\t输出:簡繁轉換
\t-jian\t繁转简\t\t如:jianfan.py -jian 簡繁轉換\t输出:简繁转换
\t-zifan\t查单字繁体\t如:jianfan.py -zifan 你\t\t输出:[妳]
\t-zijian\t查单字简体\t如:jianfan.py -zijian 妳\t输出:[你]
'''
    try:
        mode = sys.argv[1]
    except IndexError:
        print(doc)
    else:
        try:
            str = sys.argv[2]
        except IndexError:
            print(doc)
        else:
            if mode == "-fan":
                print(JianFan().fan(str))
            elif mode == "-jian":
                print(JianFan().jian(str))
            elif mode == "-zijian":
                print(JianFan().zi_jian(str))
            elif mode == "-zifan":
                print(JianFan().zi_fan(str))
            else:
                print(doc)


if(__name__ == "__main__"):
    main()
