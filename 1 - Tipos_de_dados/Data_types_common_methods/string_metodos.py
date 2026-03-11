
# upper()
# Transforma a string em maiúsculas
text = "python"
print(f"método upper(): {text.upper()}")   

# lower()
# Transforma tudo em minúsculas
text2 = "Python Programming"
print(f"método lower(): {text2.lower()}")

# .strip()
# Remove espaços do começo e do fim
text3 = "   python   "
print(f"método strip(): {text3.strip()}")

# .split()
# Divide uma string em lista de partes
sentence = "Python is very powerful"
words = sentence.split()
print(f"método split(): {words}")

# .join()
# Faz o oposto do split
words2 = ["Python", "is", "great"]
sentence2 = " ".join(words2)
print(f"método join(): {sentence2}")

# .replace()
# Substitui partes de uma string
text4 = "I like Java"
new_text = text4.replace("Java", "Python")
print(f"método replace(): {new_text}")

# .startswith() e .endswith()
# Verificam começo ou final da string
filename = "data.csv"
print(f"método endswith(): {filename.endswith(".csv")}")

url = "https://example.com"
print(f"método startswith(): {url.startswith("https")}")

# .find()
# Localiza posição de um texto
text5 = "Python programming"
print(f"método find(): {text5.find("program")}")

# .count()
# Conta quantas vezes algo aparece
text6 = "banana"
print(f"método count(): {text6.count("a")}")



