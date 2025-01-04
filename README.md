### **Projectlar**

#### **1-proyekt: Foydalanuvchilar ma’lumotlarini tahlil qilish**

Sizga quyidagi foydalanuvchilar ma’lumotlari **users** berilgan (users.py faylda 1000 ta data bor):  

```python
users = [
    {"id": 998, "first_name": "Humbert", "last_name": "Richford", "email": "hrichfordrp@gizmodo.com", "gender": "Male", "ip_address": "250.4.246.253"},
    {"id": 999, "first_name": "Bryanty", "last_name": "Rosenvasser", "email": "brosenvasserrq@discovery.com", "gender": "Male", "ip_address": "186.72.250.20"},
    {"id": 1000, "first_name": "Karita", "last_name": "Truter", "email": "ktruterrr@mapy.cz", "gender": "Female", "ip_address": "176.154.178.243"}
]
```

#### **Vazifa**
Quyidagi hisobotni qiladigan dasturi yozing:  
1. **Jinslar bo‘yicha tahlil:** Erkak va ayol foydalanuvchilar sonini sanang va ularning umumiy foydalanuvchilarga nisbatan foizini hisoblang.  

#### **Natijaning kutilgan ko‘rinishi**  
Hisobot quyidagicha ko‘rinishda bo‘lishi kerak (ma'lumotlar aynan shunaqa chiqmasligi mumkin):  

```
Hisobot:
- Erkaklar: 500 ta, 50%
- Ayollar: 500 ta, 50%
```

---

#### **2-proyekt: Telefonlar ma’lumotlarini tahlil qilish**

Sizga quyidagi telefonlar ma’lumotlari **phones** berilgan (phones.py faylda 1000 ta berilgan):  

```python
phones = [
    {"brand": "Bird", "model": "Bird MP300", "date": 0},
    {"brand": "HTC", "model": "HTC P3470", "date": 2008},
    {"brand": "LG", "model": "LG GX300", "date": 2010},
    {"brand": "i-mobile", "model": "i-mobile 520", "date": 2007},
    {"brand": "Emporia", "model": "Emporia Connect", "date": 2012},
    {"brand": "Motorola", "model": "Motorola Moto G9 (India)", "date": 2020}
]
```

#### **Vazifa**
Quyidagi hisobotni qiladigan dasturi yozing:  
1. **Brendlar bo‘yicha tahlil:** Har bir brend bo‘yicha telefonlar sonini sanang va ularning umumiy telefonlarga nisbatan foizini hisoblang.  
2. **Yillar bo‘yicha tahlil:** Telefonlarni chiqarilgan yillarga qarab guruhlang (masalan, 2000–2025), har bir yilda nechta telefon chiqarilganini sanang va ularning foizini hisoblang.  

#### **Natijaning kutilgan ko‘rinishi**  
Hisobot quyidagicha ko‘rinishda bo‘lishi kerak (ma'lumotlar aynan shunaqa bo'lmasligi mumkin):  

```
Hisobot:
- Brendlar:
    - Samsung telefonlar: 300 ta, 30%
    - Motorola telefonlar: 150 ta, 15%
    ...
- Yillar (2000–2025):
    - 2000 yilda: 20 ta, 2%
    - 2001 yilda: 40 ta, 4%
    ...
```
