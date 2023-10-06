# user = input("Crie o seu nome de usuário? "))
# print(f'Olá, {user}. ')

tweet = str(input("Faça seu Tweet? " ))
tamanho = tweet
    
if tweet <= tamanho[:140]:
    print(tweet)
else:
    print('MUTE')