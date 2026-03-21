temperature = int(input("Enter the temperature in degree celsius: "))
if temperature <= 0:
    print("You must wear: \n  A thermal base layer, insulating mid-layer (fleece/wool), and a wind/waterproof coat")
elif temperature <= 5:
    print("You must wear: \n a layered outfit featuring a warm, insulated outer layer (like a parka or wool coat) over sweaters, a scarf, beanie, gloves, and boots")
elif temperature <= 10:
    print("You must wear: \n a light, windproof, or quilted jacket over a sweater or long-sleeve top.  ")
elif temperature <= 20:
    print("You must wear: \n a T-shirt paired with a light jacket, cardigan, or hoodie ")
elif temperature <= 30:
    print("You must wear: \n shorts, cotton trousers, midi/maxi skirts, and sleeveless tops.  ")
elif temperature <= 40:
    print("You must wear: \n loose-fitting, light-colored clothing made from breathable natural fabrics like cotton or linen")