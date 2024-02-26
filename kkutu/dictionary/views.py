from django.shortcuts import render, redirect
from dictionary.models import *
import requests
from bs4 import BeautifulSoup

# Create your views here.

"""
해야 할 것
끝말잇기
앞말잇기
공격단어
ㄴ 이을 수 있는 단어 수
ㄴㄴ 두음법칙도 고려
한방단어
쿵쿵따
단어대결
\/단어 길이 정렬
\/단어 미션 정렬
\/단어 길이 검색
미션 있으면 미션 글자 개수 표시, 없으면 단어 길이 표시
문의 링크
끄투 이동 링크
"""

def LenSort(words):
    for i in range(len(words) - 1):
        for j in range(i, len(words) - 1):
            if len(words[j].word) > len(words[i].word):
                tmp = words[i]
                words[i] = words[j]
                words[j] = tmp

def HeadSoundFilter1(word):
    li = ["리", "랴", "려", "료", "류"]
    for i in li:
        if word[-1] == li:
            return True
        
def HeadSoundFilter2(word):
    li = ["라", "로", "루", "르", "래", "레", "뢰"]
    for i in li:
        if word[-1] == li:
            return True
        
def HeadSoundRule(letter):
    match letter:
        case "리":
            return "이"
                

def main(request):
    return render(request, "main.html")


def wordsheet(request):
    return redirect("backletter")


def backletter(request):
    if request.method == "POST":
        first = request.POST.get("first")
        mission = request.POST.get("mission")
        length = request.POST.get("length")
        candidate = []
        for i in Dictionary.objects.all():
            corre = 0
            for j,k in zip(i.word, first):
                if j == k:
                    corre += 1
            if len(length) == 0:
                if corre == len(first):
                    candidate.append(i)
            else:
                if corre == len(first) and len(i.word) == int(length):
                    candidate.append(i)
        
        LenSort(candidate)
        
        dic = {}
        for i in candidate:
            misnum = 0
            for j in i.word:
                if j == mission:
                    misnum += 1
            dic[i.word] = misnum

        mis = 6
        words = []
        for i in range(7):
            for j in dic:
                if dic[j] == mis:
                    class Word:
                        word = j
                        leng = len(j)
                        misnum = dic[j]
                    words.append(Word)
            mis -= 1

        placeholders = [first, mission, length]
        if len(placeholders[0]) == 0:
            placeholders[0] = "시작 글자"
        if len(placeholders[1]) == 0:
            placeholders[1] = "미션 글자"
        if len(placeholders[2]) == 0:
            placeholders[2] = "단어 길이"
        

        return render(request, "backletter.html", {"words" : words, "placeholders" : placeholders})
    return render(request, "backletter.html", {"placeholders" : ["시작 글자", "미션 글자", "단어 길이"]})


def frontletter(request):
    if request.method == "POST":
        last = request.POST.get("last")
        mission = request.POST.get("mission")
        length = request.POST.get("length")
        candidate = []
        for i in Dictionary.objects.all():
            corre = 0
            rev = -1
            for j in last:
                if j == i.word[rev]:
                    rev -= 1
                    corre += 1
            if len(length) == 0:
                if corre == len(last):
                    candidate.append(i)
            else:
                if corre == len(last) and len(i.word) == int(length):
                    candidate.append(i)
        dic = {}
        for i in candidate:
            misnum = 0
            for j in i.word:
                if j == mission:
                    misnum += 1
            dic[i.word] = misnum

        mis = 6
        words = []
        for i in range(7):
            for j in dic:
                if dic[j] == mis:
                    class Word:
                        word = j
                        leng = len(j)
                        misnum = dic[j]
                    words.append(Word)
            mis -= 1

        LenSort(words)
            
        placeholders = [last, mission, length]
        if len(placeholders[0]) == 0:
            placeholders[0] = "시작 글자"
        if len(placeholders[1]) == 0:
            placeholders[1] = "미션 글자"
        if len(placeholders[2]) == 0:
            placeholders[2] = "단어 길이"

        return render(request, "frontletter.html", {"words" : words, "placeholders" : placeholders})
    return render(request, "frontletter.html", {"placeholders" : ["마지막 글자", "미션 글자", "단어 길이"]})


dic = Dictionary.objects.all()
li = []
for i in dic:
    li.append(i.word)

def attack(request):
    if request.method == "POST":
        first = request.POST.get("first")
        mission = request.POST.get("mission")
        length = request.POST.get("length")
        candidate = []
        for i in Attack.objects.all():
            corre = 0
            for j,k in zip(i.word, first):
                if j == k:
                    corre += 1
            if len(length) == 0:
                if corre == len(first):
                    candidate.append(i)
            else:
                if corre == len(first) and len(i.word) == int(length):
                    candidate.append(i)
        dic = {}
        for i in candidate:
            misnum = 0
            for j in i.word:
                if j == mission:
                    misnum += 1
            dic[i.word] = misnum

        mis = 6
        words = []
        for i in range(7):
            for j in dic:
                if dic[j] == mis:
                    count = 0
                    for k in li:
                        if k[0] == j[-1]:
                            count += 1
                    class Word:
                        word = j
                        leng = len(j)
                        misnum = dic[j]
                        next = count
                    words.append(Word)
            mis -= 1

        LenSort(words)
        
        placeholders = [first, mission, length]
        if len(placeholders[0]) == 0:
            placeholders[0] = "시작 글자"
        if len(placeholders[1]) == 0:
            placeholders[1] = "미션 글자"
        if len(placeholders[2]) == 0:
            placeholders[2] = "단어 길이"

        return render(request, "attack.html", {"words" : words, "placeholders" : placeholders})
    return render(request, "attack.html", {"placeholders" : ["시작 글자", "미션 글자", "단어 길이"]})


def onetime(request):
    return render(request, "onetime.html")


def threeletter(request):
    if request.method == "POST":
        first = request.POST.get("first")
        mission = request.POST.get("mission")
        candidate = []
        for i in Dictionary.objects.all():
            corre = 0
            for j,k in zip(i.word, first):
                if j == k:
                    corre += 1
                if corre == len(first) and len(i) == 3:
                    candidate.append(i)
        
        LenSort(candidate)
        
        dic = {}
        for i in candidate:
            misnum = 0
            for j in i.word:
                if j == mission:
                    misnum += 1
            dic[i.word] = misnum

        mis = 6
        words = []
        for i in range(7):
            for j in dic:
                if dic[j] == mis:
                    class Word:
                        word = j
                        leng = len(j)
                        misnum = dic[j]
                    words.append(Word)
            mis -= 1

        placeholders = [first, mission]
        if len(placeholders[0]) == 0:
            placeholders[0] = "시작 글자"
        if len(placeholders[1]) == 0:
            placeholders[1] = "미션 글자"
        if len(placeholders[2]) == 0:
            placeholders[2] = "단어 길이"
        

        return render(request, "backletter.html", {"words" : words, "placeholders" : placeholders})
    return render(request, "threeletter.html", {"placeholders" : ["시작 글자", "미션 글자"]})


def wordbattle(request):
    if request.method == "POST":
        first = request.POST.get("first")
        mission = request.POST.get("mission")
        length = request.POST.get("length")
        category = request.POST.get("category")
        candidate = []
        print(category)
        for i in WordBattle.objects.all():
            corre = 0
            for j,k in zip(i.word, first):
                if j == k:
                    corre += 1
            if len(length) == 0:
                if corre == len(first) and i.category == category:
                    candidate.append(i)
            else:
                if corre == len(first) and len(i.word) == int(length) and i.category == category:
                    candidate.append(i)
        
        LenSort(candidate)
        
        dic = {}
        for i in candidate:
            misnum = 0
            for j in i.word:
                if j == mission:
                    misnum += 1
            dic[i.word] = misnum

        mis = 6
        words = []
        for i in range(7):
            for j in dic:
                if dic[j] == mis:
                    class Word:
                        word = j
                        leng = len(j)
                        misnum = dic[j]
                    words.append(Word)
            mis -= 1

        placeholders = [first, mission, length, category]
        if len(placeholders[0]) == 0:
            placeholders[0] = "시작 글자"
        if len(placeholders[1]) == 0:
            placeholders[1] = "미션 글자"
        if len(placeholders[2]) == 0:
            placeholders[2] = "단어 길이"
        if len(placeholders[3]) == 0:
            placeholders[3] = "주제"

        url = "https://kkukowiki.kr/w/주제"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        categories = []
        for i in soup.select(".wikitable > tbody > tr > td > a")[:141]:
            categories.append(i.text)

        value = [category]

        return render(request, "wordbattle.html", {"words" : words, "placeholders" : placeholders, "categories" : categories, "value" : value})
    
    url = "https://kkukowiki.kr/w/주제"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    categories = []
    for i in soup.select(".wikitable > tbody > tr > td > a")[:141]:
        categories.append(i.text)
    return render(request, "wordbattle.html", {"placeholders" : ["시작 글자", "미션 글자", "단어 길이", "주제"], "categories" : categories, "value" : [""]})


def database(request):
    li = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

    if request.method == "POST":
        category = request.POST.get("category")

        if category == "1":
            # 긴 단어(한국어)
            # for i in li:
            #     res = requests.get(f"https://kkukowiki.kr/w/긴_단어/한국어/{i}")
            #     soup = BeautifulSoup(res.text, "html.parser")
            #     for j in soup.select(".sortable > tbody > tr > td > a"):
            #         word = j.text
            #         if not Dictionary.objects.filter(word=word).exists():
            #             Dictionary.objects.create(word=word).save()
            # 막아놓음
            return render(request, "disabled.html")


        elif category == "2":
            # 공격 단어(한국어)
            # for i in li:
            #     res = requests.get(f"https://kkukowiki.kr/w/공격단어/한국어/{i}")
            #     soup = BeautifulSoup(res.text, "html.parser")
            #     for j in soup.select(".sortable > tbody > tr > td > a"):
            #         word = j.text
            #         next = 0
            #         for k in Dictionary.objects.all():
            #             if k.word[0] == word[-1]:
            #                 next += 1
            #         if not Attack.objects.filter(word=word).exists():
            #             Attack.objects.create(word=word).save()
            #         if Attack.objects.filter(word=word) and not Attack.objects.filter(next=next):
            #             att = Attack.objects.get(word=word)
            #             att.next = next
            #             att.save()
            #         if not Dictionary.objects.filter(word=word).exists():
            #             Dictionary.objects.create(word=word).save()
            # 막아놓음
            return render(request, "disabled.html")


        elif category == "3":
            # 방어 단어(한국어)
            # for i in li:
            #     res = requests.get(f"https://kkukowiki.kr/w/방어단어/한국어/{i}")
            #     soup = BeautifulSoup(res.text, "html.parser")
            #     for j in soup.select(".sortable > tbody > tr > td > a"):
            #         word = j.text
            #         if not Dictionary.objects.filter(word=word).exists():
            #             Dictionary.objects.create(word=word).save()
            # 막아놓음
            return render(request, "disabled.html")


        elif category == "4":
            # 긴 단어(영어)
            # res = requests.get(f"https://kkukowiki.kr/w/긴_단어/영어")
            # soup = BeautifulSoup(res.text, "html.parser")
            # for j in soup.select(".sortable > tbody > tr > td > a"):
            #     word = j.text
            #     if not Dictionary.objects.filter(word=word).exists():
            #         Dictionary.objects.create(word=word).save()
            # 막아놓음
            return render(request, "disabled.html")


        elif category == "5":
            # 일반 단어(한국어)
            # f = open("db.sql", "r", encoding="utf-8")

            # data = f.readlines()[147827:579225:]

            # for i in data:
            #     word = ""
            #     for j in i:
            #         if j == "\t":
            #             if not Dictionary.objects.filter(word=word).exists():
            #                 Dictionary.objects.create(word=word).save()
            #             break
            #         word += j
            # 막아놓음
            return render(request, "disabled.html")


        elif category == "6":
            # 일반 단어(영어)
            # f = open("db.sql", "r", encoding="utf-8")

            # data = f.readlines()[794:147811:]
            # # data = f.readlines()[116634:147811:] # 중간 점검

            # for i in data:
            #     word = ""
            #     for j in i:
            #         if j == "\t":
            #             if not Dictionary.objects.filter(word=word).exists():
            #                 Dictionary.objects.create(word=word).save()
            #             break
            #         word += j
            # 막아놓음
            return render(request, "disabled.html")

        elif category == "7":
            # 쿵쿵따
            # for i in Dictionary.objects.all():
            #     word = i.word
            #     if len(word) == 3:
            #         if ord(word[0]) >= 127:
            #             if not ThreeLetter.objects.filter(word=word).exists():
            #                 ThreeLetter.objects.create(word=word).save()
            # 막아놓음
            return render(request, "disabled.html")
        
        elif category == "8":
            # 단어 대결
            # url = "https://kkukowiki.kr/w/주제"
            # res = requests.get(url)
            # soup = BeautifulSoup(res.text, "html.parser")

            # category = []

            # for i in soup.select(".wikitable > tbody > tr > td > a"):
            #     category.append(i.text)

            # for i in category:
            #     for j in "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ":
            #         url = f"https://kkukowiki.kr/w/{i}/글자별_단어목록/{j}"
            #         res = requests.get(url)
            #         soup = BeautifulSoup(res.text, "html.parser")
            #         for k in soup.select(".wikitable > tbody > tr > td > a")[14:]:
            #             word = k.text
            #             if not WordBattle.objects.filter(word=word).exists():
            #                 WordBattle.objects.create(word=word, category=i).save()
            #             else:
            #                 try:
            #                     if WordBattle.objects.get(word=word).category != i:
            #                         WordBattle.objects.create(word=word, category=i).save()
            #                 except:
            #                     pass
            # 막아 놓음
            return render(request, "disabled.html")
        
        elif category == "9":
            return render(request, "preparing.html")

        else:
            return render(request, "NotFound.html")
        
        return render(request, "main.html")


    return render(request, "database.html")