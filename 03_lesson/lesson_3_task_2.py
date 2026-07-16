from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15 Pro", "+79123456789"),
    Smartphone("Samsung", "Galaxy S24", "+79234567890"),
    Smartphone("Xiaomi", "Mi 14", "+79345678901"),
    Smartphone("Google", "Pixel 8", "+79456789012"),
    Smartphone("OnePlus", "12", "+79567890123")
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")