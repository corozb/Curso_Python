def run():
    search = 'Beatriz'
    counter = 0
    with open ('34.aleph.txt',encoding="utf8") as f: #por defecto es 'r' por eso no hay que mencionarlo.
        for line in f:

            counter += line.count(search)

    print('{} se encuentra {} veces en el texto'.format(search, counter))


if __name__ == '__main__':
    run()
