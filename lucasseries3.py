import time


def lucasSeries(i):
    pass
    lucasSeries.startTime = time.time();
    lucasSeries.TIMEOUT_SECONDS = 120;
    assert i >= 0, ("The lucas number index is a nonnegative index")
    assert lucasSeries.TIMEOUT_SECONDS > 0, ("The maximum amount of wall clock time is a positive integer")

    def series(n):
        if time.time() - lucasSeries.startTime > lucasSeries.TIMEOUT_SECONDS:
            raise Exception('Timeout at lucas ' + str(i) + ' after ' + str(lucasSeries.TIMEOUT_SECONDS) + ' seconds')
        result = list()
        if n == 0:
            result.append(2)
            result.append(None)
            result.append(1)
            return result;
        if n == 1:
            result.append(1)
            result.append(2)
            result.append(1)
            return result;

        leftSum = series(n - 1)
        result.append(leftSum[0] + leftSum[1]);
        result.append(leftSum[0])
        # Number of calls
        result.append(leftSum[2] + 1);
        return result;

    returnResult = series(i);
    returnResult.append(time.time() - lucasSeries.startTime)
    return returnResult;



if __name__ == "__main__":

    try:
        print('Lucas 0 to 21')
        for i in range(21):
            result = lucasSeries(i);
            print('lucas', i, 'is', result[0], '- computed in', result[3], 'seconds')

        print('\n\nLucas 992 to 1000')
        for i in range(992,1000):
            result = lucasSeries(i);
            print('lucas', i, 'is', result[0], '- computed in', result[3], 'seconds')
    except Exception as err:
        print(err);

