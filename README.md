# Emotion-AI-
# 🤖 AI Emotion Recognition with ESP32-S3 & 8×8 LED Matrix

Kompyuter kamerasi yordamida inson yuzidagi emotsiyani aniqlaydigan va aniqlangan emotsiyani **ESP32-S3 orqali 8×8 MAX7219 LED Matrix** displeyida pixel-art ko'rinishidagi yuz sifatida aks ettiradigan loyiha.

> 🎥 Webcam → 🐍 Python + DeepFace → 🔌 USB Serial → 🤖 ESP32-S3 → 💡 MAX7219 8×8 LED Matrix

---

## 📌 Loyiha haqida

Ushbu loyihada kompyuterning kamerasi real vaqt rejimida kuzatiladi. Python dasturi OpenCV yordamida video oqimini oladi, yuzni aniqlaydi va DeepFace yordamida yuz ifodasidagi asosiy emotsiyani aniqlaydi.

Aniqlangan emotsiya USB orqali ESP32-S3 ga yuboriladi.

ESP32-S3 esa kelgan emotsiya kodiga qarab 8×8 MAX7219 LED Matrix'da tegishli pixel-art yuzni ko'rsatadi.

Masalan:

```text
Camera
   │
   ▼
OpenCV
   │
   ▼
Face Detection
   │
   ▼
DeepFace
   │
   ▼
Happy
   │
   ▼
"H"
   │
   ▼
USB Serial
   │
   ▼
ESP32-S3
   │
   ▼
MAX7219
   │
   ▼
😊
```

---

# ✨ Asosiy imkoniyatlar

* 🎥 Kompyuter kamerasi bilan real vaqt rejimida ishlash
* 👤 Yuzni aniqlash
* 🧠 DeepFace yordamida emotsiya tahlili
* 📊 Emotsiya confidence qiymatini olish
* ⚡ DeepFace'ni har bir frame'da emas, interval bilan ishlatish
* 🔌 USB Serial orqali ESP32-S3 bilan aloqa
* 💡 MAX7219 8×8 LED Matrix'da emotsiyani ko'rsatish
* 🙂 Pixel-art yuzlar
* 😄 Happy
* 😢 Sad
* 😐 Neutral
* 😠 Angry
* 😮 Surprise
* 😨 Fear
* 🤢 Disgust
* 🔧 Sozlamalarni `config.py` orqali boshqarish
* 🧩 Modulli loyiha arxitekturasi

---

# 🧰 Kerakli qurilmalar

## Hardware

| Qurilma                |            Soni | Vazifasi              |
| ---------------------- | --------------: | --------------------- |
| ESP32-S3               |               1 | LED Matrix boshqaruvi |
| MAX7219 8×8 LED Matrix |               1 | Emotsiyani ko'rsatish |
| USB Type-C kabel       |               1 | Kompyuter ↔ ESP32-S3  |
| Webcam                 |               1 | Yuzni tasvirga olish  |
| Jumper wires           |      Bir nechta | Ulanish               |
| 5V quvvat manbai       | Zaruratga qarab | MAX7219 quvvati       |

> Ushbu loyiha kompyuterning ichki kamerasidan ham foydalanishi mumkin. Alohida USB webcam majburiy emas.

---

# 💻 Software

* Python 3.x
* OpenCV
* DeepFace
* NumPy
* PySerial
* Arduino IDE
* ESP32 Arduino Core
* LedControl kutubxonasi

DeepFace'ni PyPI orqali o'rnatish mumkin va rasmiy loyiha hujjatlarida `pip install deepface` usuli ko'rsatilgan.

---

# 📁 Loyiha strukturasi

```text
Emotion_Project/
│
├── main.py
├── config.py
├── camera.py
├── face_detector.py
├── emotion_detector.py
├── serial_sender.py
├── matrix_icons.py
├── requirements.txt
├── README.md
│
└── esp32/
    │
    └── esp32s3_matrix.ino
```

---

# 🧩 Fayllarning vazifasi

## `main.py`

Loyihaning asosiy fayli.

Barcha modullarni birlashtiradi:

```text
Camera
   ↓
Face Detector
   ↓
Emotion Detector
   ↓
Serial Sender
```

---

## `config.py`

Barcha sozlamalar shu faylda saqlanadi.

Masalan:

```python
CAMERA_INDEX = 0

FRAME_WIDTH = 640
FRAME_HEIGHT = 480

EMOTION_INTERVAL = 0.5

SERIAL_ENABLE = True
SERIAL_PORT = "COM5"
BAUDRATE = 115200
```

Shuning uchun keyinchalik kod ichidan qidirib o'tirmasdan sozlamalarni bitta fayldan o'zgartirish mumkin.

---

## `camera.py`

Kamera bilan ishlaydi.

Vazifalari:

* kamerani ochish
* frame olish
* tasvirni horizontal akslantirish
* kamera o'lchamini sozlash
* kamerani yopish

Kameradagi tasvirni oynadagi kabi ko'rsatish uchun:

```python
frame = cv2.flip(frame, 1)
```

ishlatiladi.

---

## `face_detector.py`

Yuzni aniqlash uchun javob beradi.

Hozirgi loyihada OpenCV Haar Cascade ishlatiladi.

```text
Camera Frame
     ↓
Grayscale
     ↓
Haar Cascade
     ↓
Face coordinates
```

Natija:

```python
(x, y, w, h)
```

ko'rinishida olinadi.

---

## `emotion_detector.py`

Loyihaning AI qismi.

DeepFace orqali:

```text
angry
fear
neutral
sad
disgust
happy
surprise
```

emotsiyalaridan dominant emotsiya aniqlanadi.

DeepFace yuz ifodasi/emotsiya tahlilini qo'llab-quvvatlaydi.

---

## `serial_sender.py`

Python'dan ESP32-S3 ga Serial orqali ma'lumot yuboradi.

Masalan:

```text
H
```

yoki:

```text
S
```

yoki:

```text
N
```

---

## `matrix_icons.py`

8×8 LED Matrix uchun pixel-art rasmlar saqlanadi.

Masalan:

```python
HAPPY = [
    0b00100100,
    0b00100100,
    0b00000000,
    0b00000000,
    0b01000010,
    0b00111100,
    0b00000000,
    0b00000000
]
```

---

## `requirements.txt`

Python dependency'lari:

```text
opencv-python
numpy
pyserial
deepface
```

O'rnatish:

```bash
pip install -r requirements.txt
```

---

# 🐍 Python qismini o'rnatish

## 1. Repository'ni clone qilish

GitHub repository'ni kompyuterga yuklab oling.

Keyin loyiha papkasiga o'ting:

```bash
cd Emotion_Project
```

---

## 2. Virtual environment yaratish

Windows:

```bash
python -m venv venv
```

Faollashtirish:

```bash
venv\Scripts\activate
```

Terminalda:

```text
(venv)
```

paydo bo'lishi kerak.

---

## 3. pip yangilash

```bash
python -m pip install --upgrade pip
```

---

## 4. Kutubxonalarni o'rnatish

```bash
pip install -r requirements.txt
```

Yoki alohida:

```bash
pip install opencv-python
pip install numpy
pip install pyserial
pip install deepface
```

---

# 🧪 Python dasturini tekshirish

Avval kamerani tekshirish tavsiya qilinadi:

```bash
python main.py
```

Kamera oynasi ochilishi kerak.

Yuz aniqlanganda:

```text
Faces : 1
```

ko'rsatiladi.

DeepFace ishlaganda:

```text
Emotion : happy
Confidence : 95.4 %
```

kabi natija chiqadi.

---

# 🧠 DeepFace qanday ishlaydi?

Pipeline:

```text
Video Frame
     │
     ▼
Face Detection
     │
     ▼
Face Crop
     │
     ▼
DeepFace
     │
     ▼
Emotion Scores
     │
     ▼
Dominant Emotion
```

Misol:

```text
happy     94.2%
neutral    3.1%
sad        1.7%
angry      0.6%
fear       0.2%
surprise   0.2%
disgust    0.0%
```

Natijada:

```text
dominant_emotion = happy
```

bo'ladi.

---

# ⚡ Performance Optimization

DeepFace nisbatan og'ir model bo'lgani sababli uni har bir video frame'da ishga tushirish yaxshi usul emas.

Masalan:

```text
30 FPS camera
      ↓
30 DeepFace analysis / second
```

kompyuterga katta yuklama beradi.

Shuning uchun loyiha:

```text
Camera
  ↓
30 FPS
  ↓
Face Detection

DeepFace
  ↓
har 0.5 sekund
```

tamoyilida ishlaydi.

Masalan:

```text
Frame 1
Frame 2
Frame 3
Frame 4
Frame 5
   ↓
DeepFace
   ↓
Happy
```

Keyingi emotsiya yangilanguncha oxirgi natija ko'rsatiladi.

---

# 🔌 ESP32-S3 va MAX7219 ulanishi

Ushbu loyiha uchun MAX7219 8×8 LED Matrix ishlatiladi.

MAX7219 uchun `LedControl` kutubxonasi mavjud va u MAX7219/MAX7221 LED driver'larini boshqarishga mo'ljallangan.

## Ulanish jadvali

| MAX7219   | ESP32-S3 |
| --------- | -------- |
| VCC       | 5V       |
| GND       | GND      |
| DIN       | GPIO 11  |
| CS / LOAD | GPIO 10  |
| CLK       | GPIO 12  |

ESP32-S3 uchun Arduino/Espressif hujjatlarida GPIO11 MOSI va GPIO12 SCK sifatida ko'rsatilgan; GPIO10 esa CS sifatida ishlatilishi mumkin.

---

# 🔌 Ulanish sxemasi

```text
              ESP32-S3
          ┌──────────────┐
          │              │
          │       5V ────┼──────── VCC
          │      GND ────┼──────── GND
          │   GPIO 11 ───┼──────── DIN
          │   GPIO 10 ───┼──────── CS
          │   GPIO 12 ───┼──────── CLK
          │              │
          └──────────────┘
                   │
                   │
                   ▼
          ┌────────────────┐
          │    MAX7219     │
          │     8 × 8      │
          │ LED MATRIX     │
          └────────────────┘
```

---

# ⚠️ Elektr ta'minoti

MAX7219 modulining VCC'si odatda 5V bilan ishlatiladi.

ESP32-S3 GPIO'lari esa 3.3V logic hisoblanadi.

Shuning uchun:

```text
MAX7219 VCC → 5V
ESP32 GND   → MAX7219 GND
```

bo'lishi kerak.

GND umumiy bo'lishi juda muhim:

```text
ESP32 GND
    │
    └──── MAX7219 GND
```

Agar matrixda tasvir chiqmasa yoki flicker kuzatilsa, birinchi navbatda:

* GND ulanishini
* VCC kuchlanishini
* DIN/CS/CLK pinlarini
* simlarning uzunligini

tekshirish kerak.

---

# 💡 MAX7219 test kodi

Arduino IDE'da `LedControl` kutubxonasini o'rnating.

Keyin:

```cpp
#include <LedControl.h>

#define DIN_PIN 11
#define CLK_PIN 12
#define CS_PIN  10

LedControl matrix(
    DIN_PIN,
    CLK_PIN,
    CS_PIN,
    1
);

void setup() {

    matrix.shutdown(0, false);

    matrix.setIntensity(0, 8);

    matrix.clearDisplay(0);
}

void loop() {

    byte happy[8] = {

        B00100100,
        B00100100,
        B00000000,
        B01000010,
        B00111100,
        B00000000,
        B00000000,
        B00000000
    };

    for (int row = 0; row < 8; row++) {

        matrix.setRow(
            0,
            row,
            happy[row]
        );
    }

    delay(2000);

    matrix.clearDisplay(0);

    delay(500);
}
```

Agar matrix to'g'ri ulangan bo'lsa, pixel-art yuz paydo bo'ladi.

---

# 🔄 Python → ESP32-S3 aloqa protokoli

Python emotsiyani qisqa kodga aylantiradi.

| Emotion  | Code | Matrix |
| -------- | ---- | ------ |
| happy    | `H`  | 😊     |
| sad      | `S`  | 😢     |
| neutral  | `N`  | 😐     |
| angry    | `A`  | 😠     |
| surprise | `U`  | 😮     |
| fear     | `F`  | 😨     |
| disgust  | `D`  | 🤢     |

Masalan DeepFace:

```text
happy
```

aniqladi.

Python:

```text
H
```

yuboradi.

ESP32:

```text
H → HAPPY ICON
```

Matrix:

```text
😊
```

---

# 🔁 To'liq ishlash jarayoni

```text
┌──────────────────────┐
│       WEBCAM         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       OpenCV         │
│   Camera Processing  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Face Detection     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      DeepFace        │
│ Emotion Recognition  │
└──────────┬───────────┘
           │
           ▼
       "happy"
           │
           ▼
          "H"
           │
           ▼
┌──────────────────────┐
│      USB Serial      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      ESP32-S3        │
└──────────┬───────────┘
           │
           │ SPI
           ▼
┌──────────────────────┐
│       MAX7219        │
│        8 × 8         │
└──────────┬───────────┘
           │
           ▼
          😊
```

---

# 🧩 ESP32-S3 qismi

ESP32-S3 faqat AI hisob-kitobini bajarmaydi.

AI hisob-kitob:

```text
COMPUTER
```

da bajariladi.

ESP32-S3 esa:

```text
Serial → Emotion Code → Matrix
```

vazifasini bajaradi.

Bu arxitektura ESP32-S3 uchun ancha yengil.

---

# 🔌 Serial aloqa

Python:

```text
COM5
115200 baud
```

ESP32:

```cpp
Serial.begin(115200);
```

Python:

```python
serial.Serial(
    "COM5",
    115200
)
```

Agar Windows'da ESP32 boshqa COM portga tushsa, masalan:

```text
COM7
```

bo'lsa:

```python
SERIAL_PORT = "COM7"
```

deb o'zgartiriladi.

---

# 🛠️ Troubleshooting

## Kamera ochilmasa

Quyidagini tekshiring:

```python
CAMERA_INDEX = 0
```

Agar kompyuterda bir nechta kamera bo'lsa:

```python
CAMERA_INDEX = 1
```

yoki:

```python
CAMERA_INDEX = 2
```

sinab ko'ring.

---

## DeepFace import xatosi

Tekshiring:

```bash
pip show deepface
```

Agar topilmasa:

```bash
pip install deepface
```

DeepFace rasmiy repository'sida PyPI orqali o'rnatish tavsiya qilingan.

---

## FPS juda past

Quyidagilarni kamaytirish mumkin:

```python
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
```

masalan:

```python
FRAME_WIDTH = 480
FRAME_HEIGHT = 360
```

Shuningdek:

```python
EMOTION_INTERVAL = 0.5
```

qiymatini:

```python
EMOTION_INTERVAL = 0.8
```

qilish mumkin.

---

## Matrix yonmasa

Quyidagilarni tekshiring:

```text
VCC  → 5V
GND  → GND
DIN  → GPIO11
CS   → GPIO10
CLK  → GPIO12
```

Shuningdek ESP32 va MAX7219 GND umumiy ekaniga ishonch hosil qiling.

---

## Matrix noto'g'ri yo'nalishda ko'rsatsa

8×8 modulning fizik joylashuviga qarab pixel-art teskari yoki oynadek chiqishi mumkin.

Bunday holatda `matrix_icons.py` ichidagi bitmaplarni:

* gorizontal flip
* vertikal flip
* 180° rotate

qilish mumkin.

---

# 🔐 Xavfsizlik va maxfiylik

Ushbu loyiha kameradan real vaqt tasvirini foydalanadi.

Loyihaning asosiy varianti:

```text
Webcam
   ↓
Local Computer
   ↓
DeepFace
```

ko'rinishida ishlaydi.

Ya'ni kamera tasvirini internetga yuborish shart emas.

Loyihani boshqa odamlar bilan ishlatishda foydalanuvchilarning roziligi va mahalliy maxfiylik qoidalariga rioya qilish tavsiya etiladi.

---

# 🚀 Kelajakdagi imkoniyatlar

Loyihani quyidagi funksiyalar bilan kengaytirish mumkin:

### 1. Animatsiya

Happy:

```text
😊
😀
😁
😀
😊
```

---

### 2. Ko'z pirpiratish

```text
👀
 ↓
-_-
 ↓
^_^
```

---

### 3. Ko'z yoshlari

Sad holatda:

```text
. . . . . .
  ↓
. . 💧 . .
```

---

### 4. Bir nechta matrix

Bir nechta MAX7219 modulini ketma-ket ulab:

```text
8×8
 ↓
16×8
 ↓
24×8
 ↓
32×8
```

qilish mumkin.

---

### 5. RGB Matrix

Keyingi bosqichda MAX7219 o'rniga:

```text
32×32 RGB
64×64 RGB
```

matrix ishlatish mumkin.

---

### 6. ESP32-S3'ni mustaqil ishlatish

Kelajakda Python kompyuterini olib tashlab, kamera va AI qismini ESP32-S3'ning o'zida ishlatish tajriba sifatida ko'rib chiqilishi mumkin.

Biroq emotion recognition uchun kompyuterda ishlaydigan DeepFace arxitekturasi odatda ancha qulay va kuchli.

---

# 📚 Foydali resurslar

Ushbu loyiha quyidagi asosiy texnologiyalarga tayanadi:

* **DeepFace** — yuz va facial attribute/emotion analysis framework.
* **OpenCV** — kamera va computer vision.
* **PySerial** — Python ↔ ESP32 Serial aloqa.
* **Arduino-ESP32** — ESP32-S3 dasturlash.
* **LedControl** — MAX7219/MAX7221 LED driver'larini boshqarish.
* **ESP32-S3 GPIO/SPI documentation** — GPIO va SPI ulanishlari.

DeepFace rasmiy GitHub repository'si va hujjatlarida emotion analysis hamda o'rnatish bo'yicha ma'lumotlar mavjud.

---

# 📌 Muhim resurslar

**DeepFace**

GitHub repository: `serengil/deepface`

**LedControl**

GitHub repository: `wayoda/LedControl`

**ESP32 Arduino**

GitHub repository: `espressif/arduino-esp32`

**ESP32-S3 GPIO Documentation**

Espressif ESP32-S3 GPIO documentation

**OpenCV**

Python uchun OpenCV documentation

**PySerial**

Python Serial communication documentation

---

# 📜 License

Ushbu loyiha o'quv va tajriba maqsadlarida yaratilgan.

Agar ushbu repository'dan o'zingizning loyihangizda foydalansangiz, original repository'ga havola berish tavsiya etiladi.

DeepFace va boshqa uchinchi tomon kutubxonalari o'zlarining alohida litsenziyalariga ega. Ularni production loyihalarida ishlatishdan oldin tegishli litsenziyalarni tekshiring. DeepFace MIT litsenziyasi ostida tarqatiladi, biroq uning ichida foydalaniladigan ayrim tashqi modellar va detectorlarning litsenziyalari alohida bo'lishi mumkin.

---

# 👨‍💻 Author

**Azizxon Esonov**

Robotics • Python • Computer Vision • ESP32 • AI

---

# ⭐ Support

Agar loyiha sizga foydali bo'lsa:

⭐ Repository'ga Star bosing.

🍴 Fork qiling.

🐛 Muammolarni Issues orqali xabar qiling.

💡 Yangi imkoniyatlar uchun Pull Request yuboring.

---

# ❤️ Project Idea

Ushbu loyihaning asosiy g'oyasi:

> **Insonning yuzidagi emotsiyani ko'rish → AI yordamida tushunish → ESP32-S3 orqali fizik qurilmada ifodalash.**

Bu loyiha Computer Vision, Artificial Intelligence, Embedded Systems, IoT va Robotics yo'nalishlarini bitta tizimda birlashtiradi.

```text
        👤
        │
        │ Face
        ▼
      📷 Camera
        │
        ▼
    🐍 Python
        │
        ▼
     🧠 AI
        │
        ▼
    😄 Happy
        │
        ▼
    🔌 ESP32-S3
        │
        ▼
    💡 MAX7219
        │
        ▼
        😊
```

**Made with Python, OpenCV, DeepFace and ESP32-S3.**
# Emotion-AI
# Emotion-AI
