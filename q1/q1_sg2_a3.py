year = int(input("Enter year of birth"))

if year = 1900:
  print("Invalid Year, it should not be earlier than 1900")
else:
  
  zodiac = [
  i. Rat (鼠 / Shǔ)
  ii. Ox (牛 / Niú)
  iii. Tiger (虎 / Hǔ)
  iv. Rabbit (兔 / Tù)
  v. Dragon (龙 / Lóng)
  vi. Snake (蛇 / Shé)
  vii. Horse (马 / Mǎ)
  viii. Goat (羊 / Yáng)
  ix. Monkey (猴 / Hóu)
  x. Rooster (鸡 / Jī)
  xi. Dog (狗 / Gǒu)
  xii. Pig (猪 / Zhū)
    ]

index = (year-1900) % 12
print("Your Chinese Zodiac sign is: [zodiac]{index} ")


