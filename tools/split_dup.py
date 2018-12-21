import codecs
import sys


def load_file(file):
    f = codecs.open(file, "r", "utf-8")
    content = f.read()
    f.close()
    return content


def save_file(file, content, encoding="utf8"):
    file = open(file, 'w', encoding=encoding)
    file.write(content)
    file.close()


def get_value_name(value, loc, remove=[]):
    key_list = []
    for key in loc:
        if loc[key] == value:
            if key not in remove:
                key_list.append(key)
    if len(key_list) == 1:
        return key_list[0]
    elif len(key_list) == 0:
        return None
    else:
        return key_list


def find_all(str, char, n=0):
    n = str.find(char, n)
    char_list = []
    if n != -1:
        map_next = find_all(str, char, n+1)
        return map_next + [n]
    return char_list


def split(s, t):
    uni_s = ""
    uni_t = ""
    dis_s = ""
    dis_t = ""
    for n in range(0, len(s)):
        s_char = s[n]
        t_char = t[n]
        s_char_list = find_all(s, s_char)
        t_char_list = find_all(s, s_char)
        if len(s_char_list) == 1 and len(t_char_list) == 1:
            uni_s += s_char
            uni_t += t_char
        else:
            dis_s += s_char
            dis_t += t_char
    return (uni_s, uni_t, dis_s, dis_t)


def save_txt(s, t, uni_s, uni_t, dis_s, dis_t):
    qty = 0
    for value in [uni_s, uni_t, dis_s, dis_t]:
        if len(value) > 0:
            varname = get_value_name(value, locals(), ["value"])
            if isinstance(varname, str):
                qty += 1
                save_file(varname + ".txt", value)
                print(varname + ".txt created")
    if qty == 0:
        print("do nothing")


def main():
    s = load_file("s.txt")
    t = load_file("t.txt")
    print("len:", len(s), len(t))

    (uni_s, uni_t, dis_s, dis_t) = split(s, t)
    print("uni_len:", len(uni_s), len(uni_t))
    print("dis_len:", len(dis_s), len(dis_t))

    save_txt(s, t, uni_s, uni_t, dis_s, dis_t)


if __name__ == '__main__':
    main()
