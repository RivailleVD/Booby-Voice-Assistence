import pyaudio

# Configurações
format = pyaudio.paInt16
channels = 1
rate = 16000
input_device_index = 1  # ALC887-VD Analog

# Inicializa PyAudio
p = pyaudio.PyAudio()

# Abre um stream
stream = p.open(format=format, channels=channels, rate=rate,
                 input=True, input_device_index=input_device_index)

# Aqui você pode adicionar código para processar a gravação

# Fecha o stream e PyAudio
stream.stop_stream()
stream.close()
p.terminate()
import pyaudio

def ouvir():
    p = pyaudio.PyAudio()

    # Defina o índice do dispositivo aqui com base no resultado de 'arecord -l'
    input_device_index = 1  # Substitua isso pelo índice correto da placa

    stream = p.open(format=pyaudio.paInt16, 
                    channels=1, 
                    rate=16000, 
                    input=True, 
                    frames_per_buffer=8192, 
                    input_device_index=input_device_index)  # Aqui você define o índice correto

    print("Gravando áudio...")

    # Configuração para gravação e processamento do áudio aqui
    frames = []

    for i in range(0, int(16000 / 8192 * 5)):  # Gravar por 5 segundos
        data = stream.read(8192)
        frames.append(data)

    print("Áudio gravado com sucesso")

    stream.stop_stream()
    stream.close()
    p.terminate()

# Chame a função de gravação
ouvir()
