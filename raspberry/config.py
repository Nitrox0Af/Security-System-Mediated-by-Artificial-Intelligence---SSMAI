OWNER = "carlos@gmail.com"


HOSTNAME = "10.9.10.17"


TOKEN = '5813859429:AAH1KS33INDbN1LMa2SDALBH53WngdU2aJk'


MAX_DISTANCE = 40
MIN_DISTANCE = 5
TIME_TO_RECOGNIZE = 10
QNTD_RECOGNIZE = 2

TIME_TO_TAKE_PHOTO = 100

TIME_TO_PRESS_HASH = 10

POTHO_PATH = "./unknown_face/photo.jpg"


ROW_PINS = [7, 11, 13, 15]
COL_PINS = [12, 16, 18]

KEY_MATRIX = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]


BUTTON_PIN = 2

LED_PIN = 17
DELAY_LED = 1

FINGERPRINT_PORT = '/dev/ttyAMA0'

DELAY_RELAY = 5
RELAY_PIN = 40

REED_SENSOR_PIN = 37

BUZZER_PIN = 17


# Configuração teclado matricial 4x4
# R - Linha; C - Colunas
R1 = 7
R2 = 11
R3 = 13
R4 = 15

C1 = 12
C2 = 16
C3 = 18
C4 = 22

# Flag
LOCKED = 1

# Configuração dos LEDs
RED_LED_PIN = 5
GREEN_LED_PIN = 3


# Configuração do botão
BUTTON_PIN = 38

# Configuração do sensor de distância
# Define os pinos TRIG e ECHO
TRIG_PIN = 32
ECHO_PIN = 36