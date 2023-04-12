import pyaudio
import wave

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

play_audio("endsound.wav") #// TODO: fogure out why this does not work