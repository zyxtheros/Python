import pyaudio
import wave
import speech_recognition as sr

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
            format = pa.get_format_from_width(wf.getsampwidth()),
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            output = True
        )
    datastream = wf.readframes(chunk)

    while datastream:
        stream.write(datastream)
        datastream = wf.readframes(chunk)

    stream.close()
    pa.terminate

r = sr.Recognizer()

def initSpeech():
    print("Listening...")

    play_audio("startsound.wav")
    m= sr.Microphone(device_index=0)

    with sr.Microphone(device_index=0) as source: #TODO fix microphone index or recognition
        audio = r.listen(source)

    play_audio("endsound.wav")

    command = ""

    try:
        command = r.recognize_google(audio)

    except:
        print("Couldn't not understand you...")

    print("Your Command:")
    print(command)

initSpeech()
