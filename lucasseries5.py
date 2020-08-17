import math


def lucasSeries(i):
    result = list()
    root5 = math.sqrt(5) / 2;
    result.append(math.pow(0.5 + root5, i) + math.pow(0.5 - root5, i));
    return result;



if __name__ == "__main__":


        print('Lucas 0 to 21')
        for i in range(21):
            result = lucasSeries(i);
            rounded = round(result[0])
            length = len(str(rounded))
            print('lucas', i, 'is',result[0],'-- i.e.,',rounded,'-- with', length,'digits' if length > 1 else 'digit')

        print('\n\nLucas 1470 to 1480')
        for i in range(1470,1480):
            result = lucasSeries(i);
            rounded = round(result[0])
            length = len(str(rounded))
            print('lucas', i, 'is', result[0], '-- i.e.,', rounded, '-- with', length,
                  'digits' if length > 1 else 'digit')

