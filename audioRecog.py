import speech_recognition as sr
text = ""

def recognize_speech():
    global text
    # Inisialisasi recognizer
    recognizer = sr.Recognizer()
    
    # Gunakan microphone sebagai sumber audio
    with sr.Microphone() as source:
        print("Silakan berbicara...")
        
        # Atur untuk mengurangi noise lingkungan
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        try:
            # Dengarkan audio dari microphone
            audio = recognizer.listen(source, timeout=5)
            print("loading...")
            
            # Gunakan Google Web Speech API untuk mengenali suara
            text = recognizer.recognize_google(audio, language="id-ID")  # Ganti dengan kode bahasa yang diinginkan
            
        except sr.WaitTimeoutError:
            print("tidak ada pesan terdeteksi sedangkan waktu sudah habis")
            return None
        except sr.UnknownValueError:
            print("Tidak dapat mengenali pembicaraan")
            return None
        except sr.RequestError as e:
            print(f"Tidak dapat meminta hasil dari service; {e}")
            return None
        except Exception as e:
            print(f"Terjadi error: {e}")
            return None