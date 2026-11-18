import flet as random_lib
import random

# قاعدة بيانات مصغرة للأحاديث النبوية الشريفة
hadiths = [
    ("الأخلاق", "إنما بُعثت لأتمم مكارم الأخلاق.", "مسند أحمد"),
    ("النية", "إنما الأعمال بالنيات، وإنما لكل امرئ ما نوى.", "صحيح البخاري ومسلم"),
    ("البر", "الدين النصيحة. قلنا: لمن؟ قال: لله ولكتابه ولرسوله ولأئمة المسلمين وعامتهم.", "صحيح مسلم"),
    ("الرحمة", "لا يرحم الله من لا يرحم الناس.", "صحيح البخاري ومسلم"),
    ("الصدق", "عليكم بالصدق، فإن الصدق يهدي إلى البر، وإن البر يهدي إلى الجنة.", "صحيح البخاري ومسلم"),
    ("العلم", "من سلك طريقاً يلتمس فيه علماً سهل الله له به طريقاً إلى الجنة.", "صحيح مسلم"),
    ("الذكر", "كلمتان خفيفتان على اللسان، ثقييلتان في الميزان، حبيبتان إلى الرحمن: سبحان الله وبحمده، سبحان الله العظيم.", "متفق عليه")
]

def main(page: random_lib.Page):
    page.title = "موسوعة الأحاديث النبوية"
    page.vertical_alignment = random_lib.MainAxisAlignment.CENTER
    page.horizontal_alignment = random_lib.CrossAxisAlignment.CENTER
    page.theme_mode = random_lib.ThemeMode.LIGHT
    page.bgcolor = random_lib.colors.AMBER_50

    category_text = random_lib.Text("اضغط الزر أدناه لعرض حديث شريف", size=14, weight=random_lib.FontWeight.BOLD, color=random_lib.colors.INDIGO_700)
    hadith_text = random_lib.Text("« خُذ من العلم ما شيئت، ولا تشغل قلبك إلا بما ينفع »", size=18, text_align=random_lib.TextAlign.CENTER, italic=True)
    source_text = random_lib.Text("المصدر: حديث شريف", size=12, color=random_lib.colors.GREY_700)

    def show_random_hadith(e):
        cat, txt, src = random.choice(hadiths)
        category_text.value = f"تصنيف: {cat}"
        hadith_text.value = f'"{txt}"'
        source_text.value = f"الراوي/المصدر: {src}"
        page.update()

    btn = random_lib.ElevatedButton(
        text="حديث نبوي جديد",
        icon=random_lib.icons.REFRESH,
        on_click=show_random_hadith,
        color=random_lib.colors.WHITE,
        bgcolor=random_lib.colors.GREEN_700
    )

    page.add(
        random_lib.Container(
            content=random_lib.Column([
                category_text,
                random_lib.Divider(height=20, color=random_lib.colors.TRANSPARENT),
                hadith_text,
                random_lib.Divider(height=20, color=random_lib.colors.TRANSPARENT),
                source_text,
                random_lib.SizedBox(height=20),
                btn
            ], alignment=random_lib.MainAxisAlignment.CENTER, horizontal_alignment=random_lib.CrossAxisAlignment.CENTER),
            padding=30,
            bgcolor=random_lib.colors.WHITE,
            border_radius=15,
            shadow=random_lib.BoxShadow(spread_radius=1, blur_radius=10, color=random_lib.colors.BLACK12),
            width=350
        )
    )

random_lib.app(target=main)
