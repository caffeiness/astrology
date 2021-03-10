import random
import ipywidgets as widgets

def on_button_clicked(b):
    birthvalue = birthdate.value
    constella = calc_constellation(birthvalue)
    fortune = ["ラッキー","ダメかも","果報は寝て待て","急がば回れ","思い立ったが吉日","ラーメン食べろ","痛い上の針"]
    result = random.choice(fortune)
    print("今日の" + constella + "の運勢は" + result)

def calc_constellation(x):
    constellation={1:"やぎ座",2:"みずがめ座",3:"うお座",
                   4:"お羊座",5:"おうし座",6:"ふたご座",
                   7:"かに座",8:"しし座",9:"おとめ座",
                   10:"てんびん座",11:"さそり座",12:"いて座"}
    if x.day>22:
        if x.month==12:
            return constellation[1]
        else: 
            return constellation[x.month+1]
    else:
        return constellation[x.month]

birthdate = widgets.DatePicker()

button = widgets.Button(description = "占う")
button.on_click(on_button_clicked)

print("誕生日を入力してください")
display(birthdate)
display(button)
