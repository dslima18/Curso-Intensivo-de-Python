def make_album(nome_do_artista,titulo_album,num_faixas=''):
    album = {'nome': nome_do_artista.title(),'titulo':titulo_album.title()}
    if num_faixas:
        album['faixas'] = num_faixas
    return album
while True:
    
    nome = input("Digite o nome do artista, caso queira fechar o programa digite 'q'. ")
    if nome == 'q':
        break
    titulo = input("Digite o título do álbum: ")
    faixas = input("Se quiser, adicione a quantidade de faixas que tem no álbum, caso não queira digite 0. ")
    faixas = int(faixas)
    if faixas == 0:
        album =make_album(nome,titulo)
    else:
        album = make_album(nome,titulo,faixas)
    print(album)

#album1 = make_album('chefin','nova era')
#album2 = make_album('orochi','ilusao')
#album3 = make_album('matue','máquina do tempo')
#album4 = make_album('caio luccas','vírus love',8)
#print(album1)
#print(album2)
#print(album3)
#print(album4)