# from faker import Faker
# from faker.providers import internet
#
# fake = Faker(locale='ru_RU')
# fake.add_provider(internet)
#
# for _ in range(50):
#     print(fake.name())
#     print(fake.address())
import collections


with open('shops.txt') as shops_file:
    shops = map(lambda x: x.replace('\n', ''), shops_file.readlines())

city_shops = collections.defaultdict(list)
for i in shops:
    shop, city = i.split(':')
    city_shops[city].append(shop)

print(city_shops)
