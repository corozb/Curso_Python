def promedio(temps):
    sumPromedio = 0
    for promedios in temps:
        sumPromedio += float(promedios)
    return sumPromedio / len(temps)

if __name__=='__main__':
    temps = [2, 4, 6, 8, 2, 5]
    average = promedio(temps)
    print('su promedio es {}'.format(average))
