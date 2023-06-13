import random
import time

# تعريف المتغيرات العامة
score = 0
colors = {'ازرق': 0, 'اخضر': 0, 'احمر': 0, 'برتقالى': 0}

# دالة لطباعة النص بتأخير
def print_pause():
    print("تجد نفسك واقفًا في حقل مفتوح، مليء بالعشب",
          "وأزهار برية صفراء .")
    time.sleep(1)
    print(" شائعة تقول أن جنية شريرة موجودة في مكان ما هنا،",
          "وكانت تخيف القرية المجاورة")
    time.sleep(1)
    print("أمامك منزل.")
    time.sleep(1)
    print("على يمينك كهف مظلم")
    time.sleep(1)
    print("في يدك تمسك بعصاك السحرية الموثوق به (ولكن ليس فعالًا جدًا).")
    time.sleep(1)
    print("ماذا تريد ان تفعل؟")
    time.sleep(1)
    print("1- الذهاب إلى المنزل")
    time.sleep(1)
    print("2- النظر إلى الكهف")
    time.sleep(1)
    print("3- الوحش يظهر أمامك!")
    time.sleep(1)

# دالة لتشغيل اللعبة والتحقق من اختيار المستخدم
def play_choice():
    global score # استخدام المتغير العام score
    wand_color = random.choice(list(colors.keys())) 
    while True:
        choice = input("الرجاء إدخال اختيارك: ")
        if choice == "1":
            house()
            score += 5
            break
        elif choice == "2":
            cave()
            score += 10
            break
        elif choice == "3":
            monster(wand_color)
            break
        else:
            print("الرجاء اختيار خيار صحيح (1, 2, أو 3)")
    def play_again():
        global score
        score=0
        play_again_choice = input("هل تريد اللعب مجددًا؟ (نعم/لا)").lower()
        if play_again_choice == "نعم":
            print_pause()
            play_choice()
        elif play_again_choice == "لا":
            print("شكرًا لك على اللعب!")
        else:
            play_again_choice = input("هل تريد اللعب مجددًا؟ (نعم/لا)")
    play_again()
# دالة لتشغيل الإجراءات المناسبة للخيار 1
def house():
    print("انت تدخل المنزل وتجد أنه خالٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍمفروش جيدونظيف، وتشم رائحة الكعك اللذيذة.")
    time.sleep(1)
    print("تدخل المطبخ وتجد كعكة جديدة على الطاولة.")
    time.sleep(1)
    print("تأكل الكعكة وتشعر بالرضا.")
    time.sleep(1)
    print("ترجع إلى الخارج.")

# دالة لتشغيل الإجراءات المناسبة للخيار 2
def cave():
    print("أنت تدخل الكهف المظلم وتجد نفسك تسير في الممرات الضيقة.")
    time.sleep(1)
    print("تبدأ في الشعور بالخوف.")
    time.sleep(1)
    print("لكن بعد قليل ترى ضوءًا يتسلل في الممر.")
    time.sleep(1)
    print("تتبع الضوء وتجد كنزًا ثمينًا!")
    time.sleep(1)
    print("تحصل على حزمة من الذهب وتعود بسلام.")

# دالة لتشغيل الإجراءات المناسبة للخيار 3 وتحديث قيم الألوان
def monster(wand_color):
    global score # استخدام المتغير العام score
    print("تواجه الوحش!")
    time.sleep(1)
    if wand_color == 'ازرق':
        print("عصاك السحرية الزرقاء تلمع وتطلق ضوءًا شديدًا!")
        time.sleep(1)
        print("الوحش يتألم ويهرب!")
        time.sleep(1)
        colors['ازرق'] += 1
        score += 20
    elif wand_color == 'اخضر':
        print("عصاك السحرية الخضراء تطلق ثلاثة أشعة تحطم الوحش!")
        time.sleep(1)
        colors['اخضر'] += 1
        score += 10
    elif wand_color == 'احمر':
        print("عصاك السحرية الحمراء تصدر صوتًا عاليًا، لكن لا يحدث شيء!")
        time.sleep(1)
        colors['احمر'] += 1
        score += 5
    elif wand_color == 'برتقالى':
        print("عصاك السحرية البرتقالية تصدر اللهب ولكن لا يحدث شيء!")
        time.sleep(1)
        colors['برتقالى'] += 1
        score += 5
    
    # عرض نتائج الألوان بعد الانتهاء من اللعبة
    print("نتائج اللعبة:")
    for color, points in colors.items():
        print(color + ": " + str(points) + " نقطة")
    print("لقد حصلت على " + str(score) + " نقطة.")

    print("تم انهاء اللعبة. مجموع النقاط الخاص بك هو: " + str(score))
        
# تشغيل اللعبة
print_pause()
play_choice()

      
