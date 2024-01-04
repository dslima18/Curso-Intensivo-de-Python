def show_magicians(magos):
    for mago in magos:
        print(mago.title())
def make_great(magos):
    novos_magos = []
    for mago in range(0,3):
        novos_magos.append(magos[mago] + " o Grande") 
    return novos_magos
magicos = ['houdini','mr bean','o mago']
show_magicians(magicos)
novos_magos = make_great(magicos[:])
show_magicians(magicos)
show_magicians(novos_magos)