# Voice Robo

Voice Robo is a simple Python project that turns text input into speech using the `pyttsx3` library. With Voice Robo, you can make your computer speak any text you enter into the terminal. This project is perfect for beginners looking to explore text-to-speech (TTS) capabilities in Python.

## Prerequisites

Before running Voice Robo, make sure you have Python installed on your system. You can download Python from (https://www.python.org/downloads/).

Additionally, install the `pyttsx3` library using pip:

```bash
pip install pyttsx3
Getting Started
Clone this repository to your local machine:


git clone https://github.com/your-username/voice-robo.git
Navigate to the project directory:


cd voice-Robo
Run the program by executing the voice_robo.py file:


python voice_robo.py
You will be prompted to enter text in the terminal. After entering the text, press Enter, and Voice Robo will convert it into spoken words.
Customization
You can customize the speech output by modifying the voice settings in the voice_robo.py file. Adjust the rate (speed) and volume to achieve the desired voice characteristics.



# Customize voice settings
engine.setProperty('rate', 150)    # Adjust the speed (words per minute)
engine.setProperty('volume', 1.0) # Adjust the volume (1.0 is maximum)
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
pyttsx3: The Python library used for text-to-speech conversion.
Enjoy using Voice Robo to hear your text come to life!

