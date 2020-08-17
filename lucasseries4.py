import time


def lucasSeries(i):
    pass
    lucasSeries.startTime = time.time();
    assert i >= 0, ("The lucas number index is a nonnegative index")

    result = list()
    if i == 0:
        result.append(2)
        result.append(None)
        result.append(time.time() - lucasSeries.startTime);
        return result;

    if i == 1:
        result.append(1)
        result.append(2)
        result.append(time.time() - lucasSeries.startTime);
        return result;

    result.append(1)
    result.append(2)
    for j in range(2, i + 1):
        temp = result[0]
        result[0] = result[0] + result[1];
        result[1] = temp;

    result.append(time.time() - lucasSeries.startTime)
    return result;



if __name__ == "__main__":


        print('Lucas 0 to 21')
        for i in range(21):
            result = lucasSeries(i);
            length = len(str(result[0]))
            if length <= 50:
                print('lucas', i, 'is', result[0], '- computed in', result[2], 'seconds')
            else:
                print('lucas', i, 'contains',length,'digits - computed in', result[2],'seconds')

        print('\n\nLucas 82000 to 82010')
        for i in range(82000,82010):
            result = lucasSeries(i);
            length = len(str(result[0]))
            if length <= 50:
                print('lucas', i, 'is', result[0], '- computed in', result[2], 'seconds')
            else:
                print('lucas', i, 'contains', length, 'digits - computed in', result[2], 'seconds')


