#!/usr/bin/python
# -*- coding: utf-8 -*-
# Julius for python convert by radiumproduction
# Copyright (c) 2007-2017 RadiumProduction

import sys
import os
import re

args = sys.argv
error=0
lineno=0

yomi = open("./config/"+args[1]+".yomi", 'r', encoding='utf-8')
voca = open("./config/"+args[1]+".dict", 'w')

for line in yomi:
    if re.match(u"^%",line):
        voca.write(line)#+"\n")
        continue;

    word=line.split()
    print(word)
    word[1]=word[1].rstrip(os.linesep)

# 3文字以上からなる変換規則（v a）
    word[1]=word[1].replace("う゛ぁ","b a ")
    word[1]=word[1].replace("う゛ぃ","b i ")
    word[1]=word[1].replace("う゛ぇ","b e ")
    word[1]=word[1].replace("う゛ぉ","b o ")
    word[1]=word[1].replace("う゛ゅ","by u ")

# 2文字からなる変換規則
    word[1]=word[1].replace("ぅ゛","b u ")

    word[1]=word[1].replace("あぁ","a a ")
    word[1]=word[1].replace("いぃ","i i ")
    word[1]=word[1].replace("いぇ","i e ")
    word[1]=word[1].replace("いゃ","y a ")
    word[1]=word[1].replace("うぅ","u: ")
    word[1]=word[1].replace("えぇ","e e ")
    word[1]=word[1].replace("おぉ","o: ")
    word[1]=word[1].replace("かぁ","k a: ")
    word[1]=word[1].replace("きぃ","k i: ")
    word[1]=word[1].replace("くぅ","k u: ")
    word[1]=word[1].replace("くゃ","ky a ")
    word[1]=word[1].replace("くゅ","ky u ")
    word[1]=word[1].replace("くょ","ky o ")
    word[1]=word[1].replace("けぇ","k e: ")
    word[1]=word[1].replace("こぉ","k o: ")
    word[1]=word[1].replace("がぁ","g a: ")
    word[1]=word[1].replace("ぎぃ","g i: ")
    word[1]=word[1].replace("ぐぅ","g u: ")
    word[1]=word[1].replace("ぐゃ","gy a ")
    word[1]=word[1].replace("ぐゅ","gy u ")
    word[1]=word[1].replace("ぐょ","gy o ")
    word[1]=word[1].replace("げぇ","g e: ")
    word[1]=word[1].replace("ごぉ","g o: ")
    word[1]=word[1].replace("さぁ","s a: ")
    word[1]=word[1].replace("しぃ","sh i: ")
    word[1]=word[1].replace("すぅ","s u: ")
    word[1]=word[1].replace("すゃ","sh a ")
    word[1]=word[1].replace("すゅ","sh u ")
    word[1]=word[1].replace("すょ","sh o ")
    word[1]=word[1].replace("せぇ","s e: ")
    word[1]=word[1].replace("そぉ","s o: ")
    word[1]=word[1].replace("ざぁ","z a: ")
    word[1]=word[1].replace("じぃ","j i: ")
    word[1]=word[1].replace("ずぅ","z u: ")
    word[1]=word[1].replace("ずゃ","zy a ")
    word[1]=word[1].replace("ずゅ","zy u ")
    word[1]=word[1].replace("ずょ","zy o ")
    word[1]=word[1].replace("ぜぇ","z e: ")
    word[1]=word[1].replace("ぞぉ","z o: ")
    word[1]=word[1].replace("たぁ","t a: ")
    word[1]=word[1].replace("ちぃ","ch i: ")
    word[1]=word[1].replace("つぁ","ts a ")
    word[1]=word[1].replace("つぃ","ts i ")
    word[1]=word[1].replace("つぅ","ts u: ")
    word[1]=word[1].replace("つゃ","ch a ")
    word[1]=word[1].replace("つゅ","ch u ")
    word[1]=word[1].replace("つょ","ch o ")
    word[1]=word[1].replace("つぇ","ts e ")
    word[1]=word[1].replace("つぉ","ts o ")
    word[1]=word[1].replace("てぇ","t e: ")
    word[1]=word[1].replace("とぉ","t o: ")
    word[1]=word[1].replace("だぁ","d a: ")
    word[1]=word[1].replace("ぢぃ","j i: ")
    word[1]=word[1].replace("づぅ","d u: ")
    word[1]=word[1].replace("づゃ","zy a ")
    word[1]=word[1].replace("づゅ","zy u ")
    word[1]=word[1].replace("づょ","zy o ")
    word[1]=word[1].replace("でぇ","d e: ")
    word[1]=word[1].replace("どぉ","d o: ")
    word[1]=word[1].replace("なぁ","n a: ")
    word[1]=word[1].replace("にぃ","n i: ")
    word[1]=word[1].replace("ぬぅ","n u: ")
    word[1]=word[1].replace("ぬゃ","ny a ")
    word[1]=word[1].replace("ぬゅ","ny u ")
    word[1]=word[1].replace("ぬょ","ny o ")
    word[1]=word[1].replace("ねぇ","n e: ")
    word[1]=word[1].replace("のぉ","n o: ")
    word[1]=word[1].replace("はぁ","h a: ")
    word[1]=word[1].replace("ひぃ","h i: ")
    word[1]=word[1].replace("ふぅ","f u: ")
    word[1]=word[1].replace("ふゃ","hy a ")
    word[1]=word[1].replace("ふゅ","hy u ")
    word[1]=word[1].replace("ふょ","hy o ")
    word[1]=word[1].replace("へぇ","h e: ")
    word[1]=word[1].replace("ほぉ","h o: ")
    word[1]=word[1].replace("ばぁ","b a: ")
    word[1]=word[1].replace("びぃ","b i: ")
    word[1]=word[1].replace("ぶぅ","b u: ")
    word[1]=word[1].replace("ふゃ","hy a ")
    word[1]=word[1].replace("ぶゅ","by u ")
    word[1]=word[1].replace("ふょ","hy o ")
    word[1]=word[1].replace("べぇ","b e: ")
    word[1]=word[1].replace("ぼぉ","b o: ")
    word[1]=word[1].replace("ぱぁ","p a: ")
    word[1]=word[1].replace("ぴぃ","p i: ")
    word[1]=word[1].replace("ぷぅ","p u: ")
    word[1]=word[1].replace("ぷゃ","py a ")
    word[1]=word[1].replace("ぷゅ","py u ")
    word[1]=word[1].replace("ぷょ","py o ")
    word[1]=word[1].replace("ぺぇ","p e: ")
    word[1]=word[1].replace("ぽぉ","p o: ")
    word[1]=word[1].replace("まぁ","m a: ")
    word[1]=word[1].replace("みぃ","m i: ")
    word[1]=word[1].replace("むぅ","m u: ")
    word[1]=word[1].replace("むゃ","my a ")
    word[1]=word[1].replace("むゅ","my u ")
    word[1]=word[1].replace("むょ","my o ")
    word[1]=word[1].replace("めぇ","m e: ")
    word[1]=word[1].replace("もぉ","m o: ")
    word[1]=word[1].replace("やぁ","y a: ")
    word[1]=word[1].replace("ゆぅ","y u: ")
    word[1]=word[1].replace("ゆゃ","y a: ")
    word[1]=word[1].replace("ゆゅ","y u: ")
    word[1]=word[1].replace("ゆょ","y o: ")
    word[1]=word[1].replace("よぉ","y o: ")
    word[1]=word[1].replace("らぁ","r a: ")
    word[1]=word[1].replace("りぃ","r i: ")
    word[1]=word[1].replace("るぅ","r u: ")
    word[1]=word[1].replace("るゃ","ry a ")
    word[1]=word[1].replace("るゅ","ry u ")
    word[1]=word[1].replace("るょ","ry o ")
    word[1]=word[1].replace("れぇ","r e: ")
    word[1]=word[1].replace("ろぉ","r o: ")
    word[1]=word[1].replace("わぁ","w a: ")
    word[1]=word[1].replace("をぉ","o: ")

    word[1]=word[1].replace("う゛","b u ")
    word[1]=word[1].replace("でぃ","d i ")
    word[1]=word[1].replace("でぇ","d e: ")
    word[1]=word[1].replace("でゃ","dy a ")
    word[1]=word[1].replace("でゅ","dy u ")
    word[1]=word[1].replace("でょ","dy o ")
    word[1]=word[1].replace("てぃ","t i ")
    word[1]=word[1].replace("てぇ","t e: ")
    word[1]=word[1].replace("てゃ","ty a ")
    word[1]=word[1].replace("てゅ","ty u ")
    word[1]=word[1].replace("てょ","ty o ")
    word[1]=word[1].replace("すぃ","s i ")
    word[1]=word[1].replace("ずぁ","z u a ")
    word[1]=word[1].replace("ずぃ","z i ")
    word[1]=word[1].replace("ずぅ","z u ")
    word[1]=word[1].replace("ずゃ","zy a ")
    word[1]=word[1].replace("ずゅ","zy u ")
    word[1]=word[1].replace("ずょ","zy o ")
    word[1]=word[1].replace("ずぇ","z e ")
    word[1]=word[1].replace("ずぉ","z o ")
    word[1]=word[1].replace("きゃ","ky a ")
    word[1]=word[1].replace("きゅ","ky u ")
    word[1]=word[1].replace("きょ","ky o ")
    word[1]=word[1].replace("しゃ","sh a ")
    word[1]=word[1].replace("しゅ","sh u ")
    word[1]=word[1].replace("しぇ","sh e ")
    word[1]=word[1].replace("しょ","sh o ")
    word[1]=word[1].replace("ちゃ","ch a ")
    word[1]=word[1].replace("ちゅ","ch u ")
    word[1]=word[1].replace("ちぇ","ch e ")
    word[1]=word[1].replace("ちょ","ch o ")
    word[1]=word[1].replace("とぅ","t u ")
    word[1]=word[1].replace("とゃ","ty a ")
    word[1]=word[1].replace("とゅ","ty u ")
    word[1]=word[1].replace("とょ","ty o ")
    word[1]=word[1].replace("どぁ","d o a ")
    word[1]=word[1].replace("どぅ","d u ")
    word[1]=word[1].replace("どゃ","dy a ")
    word[1]=word[1].replace("どゅ","dy u ")
    word[1]=word[1].replace("どょ","dy o ")
    word[1]=word[1].replace("どぉ","d o: ")
    word[1]=word[1].replace("にゃ","ny a ")
    word[1]=word[1].replace("にゅ","ny u ")
    word[1]=word[1].replace("にょ","ny o ")
    word[1]=word[1].replace("ひゃ","hy a ")
    word[1]=word[1].replace("ひゅ","hy u ")
    word[1]=word[1].replace("ひょ","hy o ")
    word[1]=word[1].replace("みゃ","my a ")
    word[1]=word[1].replace("みゅ","my u ")
    word[1]=word[1].replace("みょ","my o ")
    word[1]=word[1].replace("りゃ","ry a ")
    word[1]=word[1].replace("りゅ","ry u ")
    word[1]=word[1].replace("りょ","ry o ")
    word[1]=word[1].replace("ぎゃ","gy a ")
    word[1]=word[1].replace("ぎゅ","gy u ")
    word[1]=word[1].replace("ぎょ","gy o ")
    word[1]=word[1].replace("ぢぇ","j e ")
    word[1]=word[1].replace("ぢゃ","j a ")
    word[1]=word[1].replace("ぢゅ","j u ")
    word[1]=word[1].replace("ぢょ","j o ")
    word[1]=word[1].replace("じぇ","j e ")
    word[1]=word[1].replace("じゃ","j a ")
    word[1]=word[1].replace("じゅ","j u ")
    word[1]=word[1].replace("じょ","j o ")
    word[1]=word[1].replace("びゃ","by a ")
    word[1]=word[1].replace("びゅ","by u ")
    word[1]=word[1].replace("びょ","by o ")
    word[1]=word[1].replace("ぴゃ","py a ")
    word[1]=word[1].replace("ぴゅ","py u ")
    word[1]=word[1].replace("ぴょ","py o ")
    word[1]=word[1].replace("うぁ","u a ")
    word[1]=word[1].replace("うぃ","w i ")
    word[1]=word[1].replace("うぇ","w e ")
    word[1]=word[1].replace("うぉ","w o ")
    word[1]=word[1].replace("ふぁ","f a ")
    word[1]=word[1].replace("ふぃ","f i ")
    word[1]=word[1].replace("ふぅ","f u ")
    word[1]=word[1].replace("ふゃ","hy a ")
    word[1]=word[1].replace("ふゅ","hy u ")
    word[1]=word[1].replace("ふょ","hy o ")
    word[1]=word[1].replace("ふぇ","f e ")
    word[1]=word[1].replace("ふぉ","f o ")

# 1音からなる変換規則
    word[1]=word[1].replace("あ","a ")
    word[1]=word[1].replace("い","i ")
    word[1]=word[1].replace("う","u ")
    word[1]=word[1].replace("え","e ")
    word[1]=word[1].replace("お","o ")
    word[1]=word[1].replace("か","k a ")
    word[1]=word[1].replace("き","k i ")
    word[1]=word[1].replace("く","k u ")
    word[1]=word[1].replace("け","k e ")
    word[1]=word[1].replace("こ","k o ")
    word[1]=word[1].replace("さ","s a ")
    word[1]=word[1].replace("し","sh i ")
    word[1]=word[1].replace("す","s u ")
    word[1]=word[1].replace("せ","s e ")
    word[1]=word[1].replace("そ","s o ")
    word[1]=word[1].replace("た","t a ")
    word[1]=word[1].replace("ち","ch i ")
    word[1]=word[1].replace("つ","ts u ")
    word[1]=word[1].replace("て","t e ")
    word[1]=word[1].replace("と","t o ")
    word[1]=word[1].replace("な","n a ")
    word[1]=word[1].replace("に","n i ")
    word[1]=word[1].replace("ぬ","n u ")
    word[1]=word[1].replace("ね","n e ")
    word[1]=word[1].replace("の","n o ")
    word[1]=word[1].replace("は","h a ")
    word[1]=word[1].replace("ひ","h i ")
    word[1]=word[1].replace("ふ","f u ")
    word[1]=word[1].replace("へ","h e ")
    word[1]=word[1].replace("ほ","h o ")
    word[1]=word[1].replace("ま","m a ")
    word[1]=word[1].replace("み","m i ")
    word[1]=word[1].replace("む","m u ")
    word[1]=word[1].replace("め","m e ")
    word[1]=word[1].replace("も","m o ")
    word[1]=word[1].replace("ら","r a ")
    word[1]=word[1].replace("り","r i ")
    word[1]=word[1].replace("る","r u ")
    word[1]=word[1].replace("れ","r e ")
    word[1]=word[1].replace("ろ","r o ")
    word[1]=word[1].replace("が","g a ")
    word[1]=word[1].replace("ぎ","g i ")
    word[1]=word[1].replace("ぐ","g u ")
    word[1]=word[1].replace("げ","g e ")
    word[1]=word[1].replace("ご","g o ")
    word[1]=word[1].replace("ざ","z a ")
    word[1]=word[1].replace("じ","j i ")
    word[1]=word[1].replace("ず","z u ")
    word[1]=word[1].replace("ぜ","z e ")
    word[1]=word[1].replace("ぞ","z o ")
    word[1]=word[1].replace("だ","d a ")
    word[1]=word[1].replace("ぢ","j i ")
    word[1]=word[1].replace("づ","z u ")
    word[1]=word[1].replace("で","d e ")
    word[1]=word[1].replace("ど","d o ")
    word[1]=word[1].replace("ば","b a ")
    word[1]=word[1].replace("び","b i ")
    word[1]=word[1].replace("ぶ","b u ")
    word[1]=word[1].replace("べ","b e ")
    word[1]=word[1].replace("ぼ","b o ")
    word[1]=word[1].replace("ぱ","p a ")
    word[1]=word[1].replace("ぴ","p i ")
    word[1]=word[1].replace("ぷ","p u ")
    word[1]=word[1].replace("ぺ","p e ")
    word[1]=word[1].replace("ぽ","p o ")
    word[1]=word[1].replace("や","y a ")
    word[1]=word[1].replace("ゆ","y u ")
    word[1]=word[1].replace("よ","y o ")
    word[1]=word[1].replace("わ","w a ")
    word[1]=word[1].replace("ゐ","i ")
    word[1]=word[1].replace("ゑ","e ")
    word[1]=word[1].replace("ん","N ")
    word[1]=word[1].replace("っ","q ")
    word[1]=word[1].replace("ー",": ")

# ここまでに処理されてない ぁぃぅぇぉ はそのまま大文字扱い
    word[1]=word[1].replace("ぁ","a ")
    word[1]=word[1].replace("ぃ","i ")
    word[1]=word[1].replace("ぅ","u ")
    word[1]=word[1].replace("ぇ","e ")
    word[1]=word[1].replace("ぉ","o ")
    word[1]=word[1].replace("ゎ","w a ")
    word[1]=word[1].replace("ぉ","o ")
    word[1]=word[1].replace("を","o ")

    word[1]=re.sub(r"^ ","",word[1])
    word[1]=re.sub(r":+",":",word[1])
    word[1]=re.sub(r" :",":",word[1])

    lineno+=1
    if re.match(r"^[a-zA-Z:]+$",word[1]):
        if error==0:
            error=1
            print("Error: (they were also printed to stdout)"+"\n")
        print("line "+str(lineno)+":"+word[0]+"\t"+word[1]+"\n")
    voca.write(word[0]+"\t"+word[1]+"\n")
if len(args)==3:
    if args[2]=="-n":
        voca.write(r"% NOISE"+"\n")
        voca.write(r"<sp>"+"\tsp"+"\n")
voca.write(r"% NS_B"+"\n")
voca.write(r"<s>"+"\tsilB"+"\n")
voca.write(r"% NS_E"+"\n")
voca.write(r"</s>"+"\tsilE"+"\n")

yomi.close()
voca.close()