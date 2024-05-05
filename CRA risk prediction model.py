import math
import tkinter as tk

window = tk.Tk()   #Tk()是对象
window.title('Colorectal Adenoma Risk Prediction')   #窗口的标题
window.geometry('1300x670')   #窗口的大小原1250x750

#Age
l_Age = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                 text = '1. Age (years):',   #label上的文字
                 justify = "left",
                 anchor = 'nw',
                 width = 15, height = 2)   #label的大小，即字符数的大小
l_Age.place(x=20, y=20, anchor='nw')  #放置这个label对象的方法

t_Age = tk.Text(window, width = 8, height = 2)
t_Age.place(x=125, y=25, anchor='nw')

#Sex
l_Sex = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                 text = '2. Sex:',   #label上的文字
                 justify = "left",
                 anchor = 'nw',
                 width = 6, height = 2)   #label的大小，即字符数的大小
l_Sex.place(x=300, y=20, anchor='nw')  #放置这个label对象的方法

sex = tk.StringVar()    #定义一个Sex的字符串变量
def sex_male():     #给sex_int赋值
    global sex_int
    sex_int = 1
r_sex1 = tk.Radiobutton(window, text = 'Male',
                        anchor = 'nw',
                        variable = sex,
                        value = 1,    #当我选择Option A的选项时，var就会被复制成A
                        command = sex_male)
r_sex1.place(x=350, y=18, anchor='nw')

def sex_female():     #给sex_int赋值
    global sex_int
    sex_int = 0
r_sex2 = tk.Radiobutton(window, text = 'Female',
                        anchor = 'nw',
                        variable = sex,
                        value = 0,    #当我选择Option A的选项时，var就会被复制成A
                        command = sex_female)
r_sex2.place(x=350, y=39, anchor='nw')


#Processed Meat
l_ProcessedMeat = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                           text = '3. How much processed meat do you eat:',   #label上的文字
                           justify = "left",
                           anchor = 'nw',
                           width = 50, height = 2)   #label的大小，即字符数的大小
l_ProcessedMeat.place(x=20, y=100, anchor='nw')  #放置这个label对象的方法

processedmeat = tk.StringVar()    #定义一个Sex的字符串变量
def processedmeat_0():     #给sex_int赋值
    global processedmeat_int
    processedmeat_int = 0
r_processedmeat0 = tk.Radiobutton(window, text = 'Rarely',
                                  anchor = 'nw',
                                  variable = processedmeat,
                                  value = 0,    #当我选择Option A的选项时，var就会被复制成A
                                  command = processedmeat_0)
r_processedmeat0.place(x=300, y=98, anchor='nw')

def processedmeat_1():     #给sex_int赋值
    global processedmeat_int
    processedmeat_int = 1
r_processedmeat1 = tk.Radiobutton(window, text = 'Occasionally, ＜ 25 g/day',
                                  anchor = 'nw',
                                  variable = processedmeat,
                                  value = 1,    #当我选择Option A的选项时，var就会被复制成A
                                  command = processedmeat_1)
r_processedmeat1.place(x=300, y=119, anchor='nw')

def processedmeat_2():     #给sex_int赋值
    global processedmeat_int
    processedmeat_int = 2
r_processedmeat2 = tk.Radiobutton(window, text = 'Usually, ≥ 25 g/day',
                                  anchor = 'nw',
                                  variable = processedmeat,
                                  value = 2,    #当我选择Option A的选项时，var就会被复制成A
                                  command = processedmeat_2)
r_processedmeat2.place(x=300, y=140, anchor='nw')


#Fish
l_Fish = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                  text = '4. How much fish and seafood do you eat:',   #label上的文字
                  justify = "left",anchor = 'nw',
                  width = 50, height = 2)   #label的大小，即字符数的大小
l_Fish.place(x=20, y=180, anchor='nw')  #放置这个label对象的方法

fish = tk.StringVar()    #定义一个Sex的字符串变量
def fish_0():     #给sex_int赋值
    global fish_int
    fish_int = 0
r_fish0 = tk.Radiobutton(window, text = 'Rarely',anchor = 'nw',
                         variable = fish,
                         value = 0,    #当我选择Option A的选项时，var就会被复制成A
                         command = fish_0)
r_fish0.place(x=300, y=178, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def fish_1():     #给sex_int赋值
    global fish_int
    fish_int = 1
r_fish1 = tk.Radiobutton(window, text = 'Occasionally, ＜ 50 g/day',anchor = 'nw',
                         variable = fish,
                         value = 1,    #当我选择Option A的选项时，var就会被复制成A
                         command = fish_1)
r_fish1.place(x=300, y=199, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def fish_2():     #给sex_int赋值
    global fish_int
    fish_int = 2
r_fish2 = tk.Radiobutton(window, text = 'Usually, ≥ 50 g/day',anchor = 'nw',
                         variable = fish,
                         value = 2,    #当我选择Option A的选项时，var就会被复制成A
                         command = fish_2)
r_fish2.place(x=300, y=220, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2


#Vegetables and Fruits
l_VegetablesFruits = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                              text = '5. How many vegetables and fruits do you\n    eat:',   #label上的文字
                              justify = "left",anchor = 'nw',width = 50, height = 3).place(x=20, y=260, anchor='nw')  #放置这个label对象的方法

vegetablesfruits = tk.StringVar()    #定义一个Sex的字符串变量
def vegetablesfruits_0():     #给sex_int赋值
    global vegetablesfruits_int
    vegetablesfruits_int = 0
r_vegetablesfruits0 = tk.Radiobutton(window, text = 'Rarely',anchor = 'nw',
                                     variable = vegetablesfruits, value = 0,    #当我选择Option A的选项时，var就会被复制成A
                                     command = vegetablesfruits_0).place(x=300, y=258, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def vegetablesfruits_1():     #给sex_int赋值
    global vegetablesfruits_int
    vegetablesfruits_int = 1
r_vegetablesfruits1 = tk.Radiobutton(window, text = 'Occasionally, ＜ 500 g/day',anchor = 'nw',
                                     variable = vegetablesfruits, value = 1,    #当我选择Option A的选项时，var就会被复制成A
                                     command = vegetablesfruits_1).place(x=300, y=279, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def vegetablesfruits_2():     #给sex_int赋值
    global vegetablesfruits_int
    vegetablesfruits_int = 2
r_vegetablesfruits2 = tk.Radiobutton(window, text = 'Usually, ≥ 500 g/day',anchor = 'nw',
                                     variable = vegetablesfruits, value = 2,    #当我选择Option A的选项时，var就会被复制成A
                                     command = vegetablesfruits_2).place(x=300, y=300, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2相邻两道题相差80


#Cereals and Legumes
l_CerealsLegumes = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                            text = '6. How many cereals and legumes do you\n    eat:',   #label上的文字
                            justify = "left",anchor = 'nw',width = 50, height = 3).place(x=20, y=340, anchor='nw')  #放置这个label对象的方法

cerealslegumes = tk.StringVar()    #定义一个Sex的字符串变量
def cerealslegumes_0():     #给sex_int赋值
    global cerealslegumes_int
    cerealslegumes_int = 0
r_cerealslegumes0 = tk.Radiobutton(window, text = 'Rarely',anchor = 'nw',
                                   variable = cerealslegumes, value = 0,    #当我选择Option A的选项时，var就会被复制成A
                                   command = cerealslegumes_0).place(x=300, y=338, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def cerealslegumes_1():     #给sex_int赋值
    global cerealslegumes_int
    cerealslegumes_int = 1
r_cerealslegumes1 = tk.Radiobutton(window, text = 'Occasionally, ＜ 25 g/day',anchor = 'nw',
                                   variable = cerealslegumes, value = 1,    #当我选择Option A的选项时，var就会被复制成A
                                   command = cerealslegumes_1).place(x=300, y=359, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def cerealslegumes_2():     #给sex_int赋值
    global cerealslegumes_int
    cerealslegumes_int = 2
r_cerealslegumes2 = tk.Radiobutton(window, text = 'Usually, ≥ 25 g/day',anchor = 'nw',
                                   variable = cerealslegumes, value = 2,    #当我选择Option A的选项时，var就会被复制成A
                                   command = cerealslegumes_2).place(x=300, y=380, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2，相邻两道题相差80


#Beverage
l_Beverage = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                      text = '7. How many sugar-sweetened beverages\n    do you drink:',   #label上的文字
                      justify = "left",anchor = 'nw',width = 50, height = 3).place(x=20, y=420, anchor='nw')  #放置这个label对象的方法

beverage = tk.StringVar()    #定义一个Sex的字符串变量
def beverage_0():     #给sex_int赋值
    global beverage_int
    beverage_int = 0
r_beverage0 = tk.Radiobutton(window, text = 'Rarely',anchor = 'nw',
                             variable = beverage, value = 0,    #当我选择Option A的选项时，var就会被复制成A
                             command = beverage_0).place(x=300, y=418, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def beverage_1():     #给sex_int赋值
    global beverage_int
    beverage_int = 1
r_beverage1 = tk.Radiobutton(window, text = 'Occasionally, ＜ 200 mL/day',anchor = 'nw',
                             variable = beverage, value = 1,    #当我选择Option A的选项时，var就会被复制成A
                             command = beverage_1).place(x=300, y=439, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def beverage_2():     #给sex_int赋值
    global beverage_int
    beverage_int = 2
r_beverage2 = tk.Radiobutton(window, text = 'Usually, ≥ 200 mL/day',anchor = 'nw',
                             variable = beverage, value = 2,    #当我选择Option A的选项时，var就会被复制成A
                             command = beverage_2).place(x=300, y=460, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2，相邻两道题相差80


#Coffee
l_Coffee = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                    text = '8. How much coffee do you drink:',   #label上的文字
                    justify = "left",anchor = 'nw',width = 50, height = 3).place(x=20, y=500, anchor='nw')  #放置这个label对象的方法

coffee = tk.StringVar()    #定义一个Sex的字符串变量
def coffee_0():     #给sex_int赋值
    global coffee_int
    coffee_int = 0
r_coffee0 = tk.Radiobutton(window, text = 'Rarely',anchor = 'nw',
                             variable = coffee, value = 0,    #当我选择Option A的选项时，var就会被复制成A
                             command = coffee_0).place(x=300, y=498, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def coffee_1():     #给sex_int赋值
    global coffee_int
    coffee_int = 1
r_coffee1 = tk.Radiobutton(window, text = 'Occasionally, ＜ 200 mL/day',anchor = 'nw',
                           variable = coffee, value = 1,    #当我选择Option A的选项时，var就会被复制成A
                           command = coffee_1).place(x=300, y=519, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def coffee_2():     #给sex_int赋值
    global coffee_int
    coffee_int = 2
r_coffee2 = tk.Radiobutton(window, text = 'Usually, ≥ 200 mL/day',anchor = 'nw',
                           variable = coffee, value = 2,    #当我选择Option A的选项时，var就会被复制成A
                           command = coffee_2).place(x=300, y=540, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2,相邻两道题相差80,，text比同一行的label的y加5

#Aspirin
l_Aspirin = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                    text = '9. Do you take aspirin or other NSAIDs\n     regularly:',   #label上的文字
                    justify = "left",anchor = 'nw',width = 50, height = 4).place(x=20, y=580, anchor='nw')  #放置这个label对象的方法

aspirin = tk.StringVar()    #定义一个Sex的字符串变量
def aspirin_0():     #给sex_int赋值
    global aspirin_int
    aspirin_int = 0
r_aspirin0 = tk.Radiobutton(window, text = 'No',anchor = 'nw',
                           variable = aspirin, value = 0,    #当我选择Option A的选项时，var就会被复制成A
                           command = aspirin_0).place(x=300, y=578, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def aspirin_1():     #给sex_int赋值
    global aspirin_int
    aspirin_int = 1
r_aspirin1 = tk.Radiobutton(window, text = 'Yes',anchor = 'nw',
                           variable = aspirin, value = 1,    #当我选择Option A的选项时，var就会被复制成A
                           command = aspirin_1).place(x=300, y=599, anchor='nw')     #相邻两道题相差80，两行radiobutton的y相差21，比同一行的label的y减2,text比同一行的label的y加5


#Smoking
l_Smoking = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                     text = '10. Do you smoke:',   #label上的文字
                     justify = "left",anchor = 'nw',width = 50, height = 3).place(x=660, y=20, anchor='nw')  #放置这个label对象的方法

smoking = tk.StringVar()    #定义一个Sex的字符串变量
def smoking_0():     #给sex_int赋值
    global smoking_int
    smoking_int = 0
r_smoking0 = tk.Radiobutton(window, text = 'Never smoked',anchor = 'nw',
                            variable = smoking, value = 0,    #当我选择Option A的选项时，var就会被复制成A
                            command = smoking_0).place(x=910, y=18, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def smoking_1():     #给sex_int赋值
    global smoking_int
    smoking_int = 1
r_smoking1 = tk.Radiobutton(window, text = 'Ever smoked',anchor = 'nw',
                            variable = smoking, value = 1,    #当我选择Option A的选项时，var就会被复制成A
                            command = smoking_1).place(x=910, y=39, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def smoking_2():     #给sex_int赋值
    global smoking_int
    smoking_int = 2
r_smoking2 = tk.Radiobutton(window, text = 'Current smoking',anchor = 'nw',
                            variable = smoking, value = 2,    #当我选择Option A的选项时，var就会被复制成A
                            command = smoking_2).place(x=910, y=60, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2,相邻两道题相差80,，text比同一行的label的y加5


#Drinking
l_Drinking = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                      text = '11. Do you drink alcohol:',   #label上的文字
                     justify = "left",anchor = 'nw',width = 50, height = 3).place(x=660, y=100, anchor='nw')  #放置这个label对象的方法

drinking = tk.StringVar()    #定义一个Sex的字符串变量
def drinking_0():     #给sex_int赋值
    global drinking_int
    drinking_int = 0
r_drinking0 = tk.Radiobutton(window, text = 'Never drunk',anchor = 'nw',
                             variable = drinking, value = 0,    #当我选择Option A的选项时，var就会被复制成A
                             command = drinking_0).place(x=910, y=98, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def drinking_1():     #给sex_int赋值
    global drinking_int
    drinking_int = 1
r_drinking1 = tk.Radiobutton(window, text = 'Ever drunk',anchor = 'nw',
                             variable = drinking, value = 1,    #当我选择Option A的选项时，var就会被复制成A
                             command = drinking_1).place(x=910, y=119, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def drinking_2():     #给sex_int赋值
    global drinking_int
    drinking_int = 2
r_drinking2 = tk.Radiobutton(window, text = 'Current drinking',anchor = 'nw',
                             variable = drinking, value = 2,    #当我选择Option A的选项时，var就会被复制成A
                             command = drinking_2).place(x=910, y=140, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2,相邻两道题相差80,，text比同一行的label的y加5


#FamilyHistory
l_FamilyHistory = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                           text = '12. Do you have family history of\n     gastrointestinal cancer:',   #label上的文字
                           justify = "left",anchor = 'nw',width = 50, height = 3).place(x=660, y=180, anchor='nw')  #放置这个label对象的方法

familyhistory = tk.StringVar()    #定义一个Sex的字符串变量
def familyhistory_0():     #给sex_int赋值
    global familyhistory_int
    familyhistory_int = 0
r_familyhistory0 = tk.Radiobutton(window, text = 'No',
                                  anchor = 'nw',
                                  variable = familyhistory, value = 0,    #当我选择Option A的选项时，var就会被复制成A
                                  command = familyhistory_0).place(x=910, y=178, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def familyhistory_1():     #给sex_int赋值
    global familyhistory_int
    familyhistory_int = 1
r_familyhistory1 = tk.Radiobutton(window, text = 'Family history of other gastrointestinal cancer',anchor = 'nw',
                                  variable = familyhistory, value = 1,    #当我选择Option A的选项时，var就会被复制成A
                                  command = familyhistory_1).place(x=910, y=199, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def familyhistory_2():     #给sex_int赋值
    global familyhistory_int
    familyhistory_int = 2
r_familyhistory2 = tk.Radiobutton(window, text = 'Family history of colorectal cancer',anchor = 'nw',
                                  variable = familyhistory, value = 2,    #当我选择Option A的选项时，var就会被复制成A
                                  command = familyhistory_2).place(x=910, y=220, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2,相邻两道题相差80,，text比同一行的label的y加5



#CancerHistory
l_CancerHistory = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                           text = '13. Do you have history of other cancer:',   #label上的文字
                           justify = "left",anchor = 'nw',width = 50, height = 3).place(x=660, y=260, anchor='nw')  #放置这个label对象的方法

cancerhistory = tk.StringVar()    #定义一个Sex的字符串变量
def cancerhistory_0():     #给sex_int赋值
    global cancerhistory_int
    cancerhistory_int = 0
r_cancerhistory0 = tk.Radiobutton(window, text = 'No',anchor = 'nw',
                                  variable = cancerhistory, value = 0,    #当我选择Option A的选项时，var就会被复制成A
                                  command = cancerhistory_0).place(x=910, y=258, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

def cancerhistory_1():     #给sex_int赋值
    global cancerhistory_int
    cancerhistory_int = 1
r_cancerhistory1 = tk.Radiobutton(window, text = 'History of other cancer',anchor = 'nw',
                                  variable = cancerhistory, value = 1,    #当我选择Option A的选项时，var就会被复制成A
                                  command = cancerhistory_1).place(x=910, y=279, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2

#def cancerhistory_2():     #给sex_int赋值
#    global cancerhistory_int
#    cancerhistory_int = 2
#r_cancerhistory2 = tk.Radiobutton(window, text = '有消化系统肿瘤史  History of gastrointestinal cancer',anchor = 'nw',
#                                  variable = cancerhistory, value = 2,    #当我选择Option A的选项时，var就会被复制成A
#                                  command = cancerhistory_2).place(x=910, y=300, anchor='nw')     #两行radiobutton的y相差21，比同一行的label的y减2,相邻两道题相差80,，text比同一行的label的y加5


#Hyperlipidemia
l_Hyperlipidemia = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                            text = '14. How long have you been diagnosed with \n     hyperlipidemia (years):',   #label上的文字
                            justify = "left", anchor = 'nw',
                            width = 100, height = 3)   #label的大小，即字符数的大小
l_Hyperlipidemia.place(x=660, y=340, anchor='nw')  #放置这个label对象的方法

t_Hyperlipidemia = tk.Text(window, width = 8, height = 2)
t_Hyperlipidemia.place(x=950, y=345, anchor='nw')    #相邻两道题相差80，两行radiobutton的y相差21，比同一行的label的y减2,text比同一行的label的y加5


#Hypertension
l_Hypertension = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                          text = '15. How long have you been diagnosed with \n     hypertension (years):',   #label上的文字
                          justify = "left", anchor = 'nw',
                          width = 100, height = 3)   #label的大小，即字符数的大小
l_Hypertension.place(x=660, y=420, anchor='nw')  #放置这个label对象的方法

t_Hypertension = tk.Text(window, width = 8, height = 2)
t_Hypertension.place(x=950, y=425, anchor='nw')    #相邻两道题相差80，两行radiobutton的y相差21，比同一行的label的y减2,text比同一行的label的y加5


#Sedentary
l_Sedentary = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                       text = '16. How long do you sit every day (hours):',   #label上的文字
                       justify = "left", anchor = 'nw',
                       width = 50, height = 2)   #label的大小，即字符数的大小
l_Sedentary.place(x=660, y=500, anchor='nw')  #放置这个label对象的方法

t_Sedentary = tk.Text(window, width = 8, height = 2)
t_Sedentary.place(x=950, y=505, anchor='nw')


#Moderate Activity
l_ModerateActivity = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
                              text = '17. How long do you spend each week doing\n     moderate activity (hours):',   #label上的文字
                              justify = "left", anchor = 'nw',
                              width = 100, height = 3)   #label的大小，即字符数的大小
l_ModerateActivity.place(x=660, y=580, anchor='nw')  #放置这个label对象的方法

t_ModerateActivity = tk.Text(window, width = 8, height = 2)
t_ModerateActivity.place(x=950, y=585, anchor='nw')    #两行radiobutton的y相差21，比同一行的label的y减2,相邻两道题相差80,，text比同一行的label的y加5


#设置显示结果的label
var_results = tk.StringVar()    #显示的东西用一个字符串的变量代替
l_results = tk.Label(window,   #定义一个label的对象，在window上的label，window是label的主题
             textvariable = var_results,   #label上显示的文字是个变量，变量根据var变量而定
             bg = 'skyblue',   #背景颜色
             anchor = 'nw',justify = 'left',
             width = 36, height = 16)   #label的大小，即字符数的大小
l_results.place(x=1024, y=340, anchor='nw')  #放置这个label对象的方法


#Submit Button
def submit():    #submit()函数的作用：提取几个对话框里的内容，并转成整数，计算风险
    global age_int, hyperlipidemia_int, hypertension_int, sedentary_int, moderateactivity_int, Z, Y, z, y, var_results
    age_int = int(t_Age.get("1.0","end"))
    hyperlipidemia_int = float(t_Hyperlipidemia.get("1.0","end"))
    hypertension_int = float(t_Hypertension.get("1.0","end"))
    sedentary_int = float(t_Sedentary.get("1.0","end"))
    moderateactivity_int = float(t_ModerateActivity.get("1.0","end"))

    n = -6.06 + 1.18*cancerhistory_int + 0.61*sex_int + 0.45*processedmeat_int + 0.4*beverage_int + 0.33*coffee_int + 0.23*smoking_int + 0.22*familyhistory_int + 0.17*sedentary_int + 0.15*hyperlipidemia_int + 0.12*drinking_int + 0.08*age_int - 0.64*cerealslegumes_int - 0.71*vegetablesfruits_int - 1.37*aspirin_int
    z = math.exp(n)
    Z = z / (1+z)

    if Z < 0.310:
        absolute = "Your absolute risk for colorectal adenoma:\nNon-high risk\n"
    elif Z >= 0.608:
        absolute = "Your absolute risk for colorectal adenoma:\nExtreme-high risk\n"
    else:
        absolute = "Your absolute risk for colorectal adenoma:\nHigh risk\n"

    m = -1.06 + 1.3*cancerhistory_int + 0.48*processedmeat_int + 0.41*sex_int + 0.35*beverage_int + 0.33*fish_int + 0.29*smoking_int + 0.27*familyhistory_int + 0.25*hyperlipidemia_int + 0.06*hypertension_int - 0.03*moderateactivity_int - 0.57*cerealslegumes_int - 0.64*vegetablesfruits_int
    y = math.exp(m)
    Y = y / (1+y)

    if Y < 0.287:
        relative = absolute + "\nYour relative risk for colorectal adenoma:\nNon-high risk\n\nThe recommended age for you to start\ncolonoscopy screening is 56.8 years old"
        var_results.set(relative)
    elif Y >= 0.525:
        relative = absolute + "\nYour relative risk for colorectal adenoma:\nExtreme-high risk\n\nThe recommended age for you to start\ncolonoscopy screening is 41.9 years old"
        var_results.set(relative)
    else:
        relative = absolute + "\nYour relative risk for colorectal adenoma:\nHigh risk\n\nThe recommended age for you to start\ncolonoscopy screening is 47.3 years old"
        var_results.set(relative)
        
    
b = tk.Button(window,   #定义一个button的对象，在window上的label，window是label的主题
              text = 'SUBMIT',   #label上的文字
              bg = 'orange1',   #背景颜色
              font = ('Segoe Print', 10, 'bold'),   #字体颜色和大小
              width = 8, height = 2,   #label的大小，即字符数的大小
              bd = 6, relief = 'raised',
              command = submit)   #点击它会执行hit_me函数
b.place(x=1110, y=580, anchor='nw')   #把button也放到window里面





window.mainloop()    #这个window会不断循环刷新，一定要有mainloop()

















