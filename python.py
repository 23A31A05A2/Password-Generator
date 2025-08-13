import random,string
letters=string.ascii_letters
digits=string.digits
special_chars="!~#$@%^&*"
pw=random.choice(digits)
pw+=random.choice(special_chars)
pw+="".join(random.choices(letters,k=6))
final_pw="".join(random.sample(pw,k=8))
print(final_pw)