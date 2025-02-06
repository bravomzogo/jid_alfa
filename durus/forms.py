from django import forms
from .models import Lesson
from .models import Newz
from .models import Qur

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['Shekh', 'Description', 'audio' ,'Topic', 'Book']


class NewzForm(forms.ModelForm):
    class Meta:
        model = Newz  # Specify the model
        fields = ['Events', 'Shekh', 'Location' , 'Time']  # Specify the fields you want in the form
from django import forms
from .models import Qur

SURA_CHOICES = [
    (sura, sura) for sura in [
         "Al-Fatiha", "Al-Baqarah", "Aal-E-Imran", "An-Nisa", "Al-Maidah",
        "Al-Anam", "Al-Araf", "Al-Anfal", "At-Tawbah", "Yunus",
        "Hud", "Yusuf", "Ar-Ra’d", "Ibrahim", "Al-Hijr",
        "An-Nahl", "Al-Isra", "Al-Kahf", "Maryam", "Taha",
        "Al-Anbiya", "Al-Hajj", "Al-Muminun", "An-Nur", "Al-Furqan",
        "Ash-Shuara", "An-Naml", "Al-Qasas", "Al-Ankabut", "Ar-Rum",
        "Luqman", "As-Sajda", "Al-Ahzab", "Saba", "Fatir",
        "Ya-Sin", "As-Saffat", "Sad", "Az-Zumar", "Ghafir",
        "Fussilat", "Ash-Shura", "Az-Zukhruf", "Ad-Dukhan", "Al-Jathiya",
        "Al-Ahqaf", "Muhammad", "Al-Fath", "Al-Hujurat", "Qaf",
        "Adh-Dhariyat", "At-Tur", "An-Najm", "Al-Qamar", "Ar-Rahman",
        "Al-Waqia", "Al-Hadid", "Al-Mujadila", "Al-Hashr", "Al-Mumtahina",
        "As-Saff", "Al-Jumu’a", "Al-Munafiqun", "At-Taghabun", "At-Talaq",
        "At-Tahrim", "Al-Mulk", "Al-Qalam", "Al-Haqqa", "Al-Maarij",
        "Nuh", "Al-Jinn", "Al-Muzzammil", "Al-Muddaththir", "Al-Qiyama",
        "Al-Insan", "Al-Mursalat", "An-Naba", "An-Nazi’at", "Abasa",
        "At-Takwir", "Al-Infitar", "Al-Mutaffifin", "Al-Inshiqaq", "Al-Buruj",
        "At-Tariq", "Al-Ala", "Al-Ghashiya", "Al-Fajr", "Al-Balad",
        "Ash-Shams", "Al-Lail", "Ad-Duhaa", "Ash-Sharh", "At-Tin",
        "Al-Alaq", "Al-Qadr", "Al-Bayyina", "Az-Zalzala", "Al-Adiyat",
        "Al-Qaria", "At-Takathur", "Al-Asr", "Al-Humaza", "Al-Fil",
        "Quraish", "Al-Ma’un", "Al-Kawthar", "Al-Kafirun", "An-Nasr",
        "Al-Masad", "Al-Ikhlas", "Al-Falaq", "An-Nas"
    ]
]

class QurForm(forms.ModelForm):
    sura = forms.ChoiceField(choices=SURA_CHOICES, label="Sura Name")

    class Meta:
        model = Qur
        fields = ['msomaji', 'audio', 'sura']

       
