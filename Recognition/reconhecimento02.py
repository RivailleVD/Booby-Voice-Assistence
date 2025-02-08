import pyaudio
from vosk import Model, KaldiRecognizer
import json


def ouvir():
    
    model = Model (r'/home/levs/Área de trabalho/boobi/vosk-model-small-pt-0.3' , lang="pt-br")
    recognizer = KaldiRecognizer(model, 44100)  # Use 44100 Hz

    mic = pyaudio.PyAudio()

    # Abre o stream de áudio
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=8192, input_device_index=3)
    print("Iniciando o reconhecimento de voz...")

    try:
        while True:
            data = stream.read(4096, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                result_json = recognizer.Result()
                result = json.loads(result_json)
                recognized_text = result.get("text", "")
                print(f"Você disse: {recognized_text}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        mic.terminate()
        print("Reconhecimento de voz encerrado.")

ouvir()