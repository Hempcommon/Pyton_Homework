from address import Address
from mailing import Mailing


to_address = Address("101000", "Москва", "Тверская", "15", "47")
from_address = Address("198000", "Санкт-Петербург", "Невский", "25", "12")

mailing = Mailing(to_address, from_address, 350.50, "TRACK123456789")


print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")