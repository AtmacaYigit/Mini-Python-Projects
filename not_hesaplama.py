num =int(input("Öğrenci Numaranızı Girin: "))
name = input("Adınızı ve Soyadınızı Girini: ")
vize = int(input("Vize Notunuz: "))
final = int(input("Final Notunuz: "))

ort = float((vize * 0.3) + (final * 0.7))

print(f"Numaranız: {num}")
print(f"Notunuz: {ort}")
