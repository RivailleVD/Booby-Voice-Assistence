https://github.com/user-attachments/assets/b4517126-058c-4880-85d5-e1df971c4132



## Reconhecimento de Voz com Vosk 🎙️
Este projeto explora as capacidades do Vosk: https://alphacephei.com/vosk/, uma ferramenta de reconhecimento de voz offline open-source, e demonstra como integrá-la em aplicações Python de forma personalizada e eficiente.

### 📚 Sobre o Projeto
O objetivo deste projeto é proporcionar um exemplo prático de integração do Vosk com Python, permitindo o reconhecimento de voz de maneira eficaz e sem a necessidade de conexão com a internet.

você pode conferir a primeira versão do código neste repositório https://github.com/RivailleVD/Boobi-Voice-Assistant

### ⚙️ Funcionalidades
* **Reconhecimento de voz offline:** Processamento de áudio completamente local, sem necessidade de internet.
* **Suporte a múltiplos idiomas:** Fácil adaptação para diferentes línguas e dialetos.
* **Integração simplificada com Python:** Uso de bibliotecas Python para rápida implementação e execução.

### 🚀 Como Instalar

*Clone o repositório:*
 **git clone https://github.com/RivailleVD/Boobi-Voice-Assistant.git**
**cd Boobi-Voice-Assistant**

###crie um novo ambiente virtual, instale as dependências necessárias com:

**pip install -r requirements.txt**

### Ative o ambiente virtual:

**source ambientevirt2/bin/activate**



## 🔧 Configurações Importantes

* **Caminho para o Modelo Vosk:**

Ao configurar o ambiente, crie uma pasta dentro do projeto chamada "Models" e extraia o modelo de reconhecimento do Vosk que você baixou em https://alphacephei.com/vosk/models


  * **ID do microfone**

    Dependendo do sistema operacional que você irá executar a aplicaçao pode ser necessario definir o ID do seu microphone manualmente, execute o arquivo /Tests
/verificação.py para visualizar informações importantes sobre dispositivos conectados em sua maquina!

    Você pode testar o funcionamento do seu microfone desejado com o arquivo /Tests/gravação.py, lembre-se que a tecla para interromper o processo é "ctrl + c"! se o audio for gravado com sucesso, seu microfone está sendo reconhecido pelo Pyaudio e pode ser utilizado.

    Uma vez identificado e testado, você pode definir manualmente o ID do seu microfone em Recognition
/reconhecimento03.py no módulo # Configurações do PyAudio a partir da linha 17, na variável "stream" dessa forma:

    python
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=8192, input_device_index= ID DO MICROFONE)

* **Microfone**
      lembre-se, ter um microfone de qualidade é fundamental para o funcionamendo do programa, diferente de outros Sistemas de reconhecimento que utilizam APIs do Google, Amazon, IBM, etc, o vosk é totalmente Offline, logo não possui uma precisão muito boa!

* **Sensibilidade do microfone**
        se o seu microfone não possuir um filtro de ruido evite ficar perto de ambientes barulhentos e longe do ventilador, isso certamente vai atrapalhar o reconhecimento da sua voz!
        pelos meus testes recomendo ajustar a sensibilidade do microfone para 55~70% para isolar o ruido ambiente, claro que isso vai depender de cada microfone, então terá de fazer seus próprios testes!
    

  ## ▶️ Executando a Aplicação
Depois de concluir todas as configurações, execute o arquivo main.py para iniciar a aplicação:
