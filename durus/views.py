from django.shortcuts import render, redirect
from .models import Lesson
from .forms import LessonForm
from hijri_converter import convert
from datetime import date
from .models import Newz
from .forms import NewzForm
from .forms import QurForm
from .models import Qur
from django.contrib import messages
from .models import Qur
from django.shortcuts import render, get_object_or_404
from .models import Qur

def play_audio(request, audio_id):
    """
    View to play a specific Qur'an audio.
    """
    audio = get_object_or_404(Qur, id=audio_id)  # Retrieve the audio object based on ID
    
    return render(request, 'durus/play_audio.html', {'audio': audio})

def sura_list(request):
    """
    View to display 114 suras of the Qur'an with clickable links.
    """
    # Fetch all suras and associate them with their audio if available
    suras = [
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

    # Fetch all audio files and create a dictionary mapping sura to audio
    audio_files = Qur.objects.all()
    sura_audio_mapping = {audio.sura: audio for audio in audio_files}

    # Add sura audio object and msomaji name to each sura
    suras_with_audio = []
    for sura in suras:
        audio = sura_audio_mapping.get(sura, None)
        suras_with_audio.append({
            'sura': sura,
            'audio': audio,
            'msomaji': audio.msomaji if audio else None  # Get msomaji name if audio exists
        })

    return render(request, 'durus/sura.html', {'suras_with_audio': suras_with_audio})



def upload_qur(request):
    """
    View for uploading Qur'an audio files.
    """
    if request.method == 'POST':
        form = QurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Audio uploaded successfully and linked to the specified sura.')
            return redirect('sura_list')  # Redirect to the sura list page
        else:
            messages.error(request, 'Failed to upload audio. Please check the form for errors.')
    else:
        form = QurForm()

    return render(request, 'durus/add_quran.html', {'form': form})

def qur_list(request):
    qur_items = Qur.objects.all()  # Retrieve all Qur'an records
    return render(request, 'durus/qur_list.html', {'qur_items': qur_items})


def news_list(request):
    # Fetch all news events from the database
    news = Newz.objects.all()
    return render(request, 'durus/news_list.html', {'news': news})
from django.shortcuts import render, redirect
from .forms import NewzForm  # Make sure NewzForm is imported

def add_event(request):
    if request.method == 'POST':
        form = NewzForm(request.POST)  # Use POST data to create the form instance
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the event to the database
            return redirect('news_list')  # Redirect after successful submission
    else:
        form = NewzForm()  # Create an empty form for GET request

    return render(request, 'durus/add_event.html', {'form': form})

def islamic_calender(request):
    # Generate a list of Gregorian dates and their corresponding Hijri dates
    today = date.today()
    calendar = []

    # Generate dates for the current year
    for month in range(1, 13):
        for day in range(1, 32):  # Attempt all days; invalid ones will be skipped
            try:
                gregorian_date = date(today.year, month, day)
                hijri_date = convert.Gregorian(gregorian_date.year, gregorian_date.month, gregorian_date.day).to_hijri()
                
                # Ensure month_name is called as a method
                calendar.append({
                    'gregorian': gregorian_date.strftime('%d %B %Y'),
                    'hijri': f"{hijri_date.day} {hijri_date.month_name()} {hijri_date.year}",
                })
            except ValueError:
                continue  # Skip invalid days (e.g., February 30)

    return render(request, 'durus/islamic_calender.html', {'calendar': calendar})
def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)  # Ensure request.FILES is included for file uploads
        if form.is_valid():
            lesson = form.save()  # Save the form and get the Lesson object
            print(lesson.audio.url)  # Print the audio file path after saving
            return redirect('home')  # Redirect to home or another page after saving
    else:
        form = LessonForm()
    return render(request, 'durus/add_lesson.html', {'form': form})

# View for the audio page
def lesson_audio(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'durus/lesson_audio.html', {'lesson': lesson})

# Admin login view with hardcoded credentials
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Hardcoded credentials for login
        if username == 'jid' and password == '2000sss@':
            # Redirect to the Add Lesson page on successful login
            return redirect('add_lesson')  
        else:
            error_message = "Invalid username or password."
            return render(request, 'durus/login.html', {'error_message': error_message})
    
    return render(request, 'durus/login.html')

# Home view to display all lessons
def home(request):
    # Fetch lessons ordered by date_created in descending order (latest first)
    lessons = Lesson.objects.all().order_by('-date_created')
    
    # Tag the first lesson as 'New'
    for lesson in lessons:
        if lesson == lessons[0]:
            lesson.is_new = True  # Add a custom attribute to indicate 'New'
        else:
            lesson.is_new = False
    
    return render(request, 'durus/home.html', {'lessons': lessons})

