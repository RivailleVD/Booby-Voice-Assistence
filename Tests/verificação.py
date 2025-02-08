import pyaudio

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"Dispositivo {i}: {info['name']}, Canais: {info['maxInputChannels']}")
p.terminate()

device_index = 3  # O índice do dispositivo ALC887-VD Analog
info = p.get_device_info_by_index(device_index)
print(f"Dispositivo: {info['name']}")
print(f"Taxas de amostragem suportadas: {info['defaultSampleRate']}")
p.terminate()

# Listar dispositivos disponíveis
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"ID: {info['index']}, Name: {info['name']}, Max Input Channels: {info['maxInputChannels']}")
# Usar um dispositivo válido (por exemplo, dispositivo 3)
device_index = 3  # ou 5, dependendo do que você preferir

try:
    info = p.get_device_info_by_index(device_index)
    print(f"Usando dispositivo: {info['name']}")
except OSError as e:
    print(f"Erro ao acessar o dispositivo: {e}")





def listar_dispositivos1():
    mic = pyaudio.PyAudio()
    for i in range(mic.get_device_count()):
        info = mic.get_device_info_by_index(i)
        print(f"Dispositivo {i}: {info['name']}, Canais: {info['maxInputChannels']}, Taxa máxima de amostragem: {info.get('defaultSampleRate', 'N/A')} Hz")
    mic.terminate()

import pyaudio

def listar_dispositivos():
    p = pyaudio.PyAudio()
    print("Dispositivos de Áudio Disponíveis:")
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(f"Dispositivo {i}: {info['name']}, Canais de Entrada: {info['maxInputChannels']}, Taxa de Amostragem Padrão: {info['defaultSampleRate']} Hz")
    p.terminate()

import pyaudio

p = pyaudio.PyAudio()

print("Dispositivos de entrada disponíveis:")
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    if info['maxInputChannels'] > 0:  # Apenas dispositivos de entrada
        print(f"Dispositivo {i}: {info['name']}, Canais: {info['maxInputChannels']}")

p.terminate()

listar_dispositivos1()
listar_dispositivos()
import pyaudio

p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
    device_info = p.get_device_info_by_index(i)
    print(f"Device {i}: {device_info['name']}")
    try:
        supported_rate = p.is_format_supported(16000.0,  # Taxa de amostragem que você está verificando
                                               input_device=device_info["index"],
                                               input_channels=1,
                                               input_format=pyaudio.paInt16)
        print(f"16000 Hz supported: {supported_rate}")
    except ValueError as e:
        print(f"Error: {e}")

