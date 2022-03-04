times = ('Atlético-MG','Flamengo','Palmeiras','Fortaleza','Corinthans','Red Bull Bragantino','Fluminense'
         ,'América-MG','Atlético-GO','Santos','Ceará','Internacional','São Paulo','Athletico-PR','Cuiabá'
         ,'Juventude','Grêmio','Bahia','Sport','Chapecoense')
print(f'Primeiros colocados: {times[0:5]}')
print(f'Últimos colocados: {times[-4:]}')
print(f'Times em ordem alfabetica: {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição.')