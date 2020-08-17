import time

def lucasSeries(i, startTime, TIMEOUT_SECONDS):
    assert i >= 0, ("The lucas number index is a nonnegative index")
    assert TIMEOUT_SECONDS > 0, ("The maximum amount of wall clock time is a positive integer")
    def series(n):
        if time.time() - startTime > TIMEOUT_SECONDS:
            raise Exception('Timeout at lucas ' + str(i) + ' after ' + str(TIMEOUT_SECONDS) + ' seconds')
        result = list()
        if n == 0:
            result.append(2)
            result.append(1)
            return result;
        if n == 1:
            result.append(1)
            result.append(1)
            return result;

        leftSum = series(n - 1)
        rightSum = series(n - 2)
        result.append(leftSum[0] + rightSum[0]);
        result.append(leftSum[1] + rightSum[1] + 1);

        return result;
    result = series(i);
    result.append(time.time() - startTime)
    return result;


if __name__ == "__main__":
    try:
        i = 0
        while True:
            result = lucasSeries(i, time.time(), 120);
            print('lucas', i, 'is', result[0], '- computed with', result[1], 'call' if result[1] <= 1 else 'calls', 'in', result[2], 'seconds')
            i = i + 1;
    except Exception as err:
        print(err);

