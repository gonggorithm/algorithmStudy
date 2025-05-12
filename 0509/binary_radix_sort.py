def binary_radix_sort(arr):
    if not arr:
        return arr

    max_bits = max(arr).bit_length()  # 가장 큰 수의 비트 길이

    for bit in range(max_bits):
        zero_bucket = []
        one_bucket = []

        for num in arr:
            # 현재 비트 위치에 따라 분류
            if (num >> bit) & 1 == 0:
                zero_bucket.append(num)
            else:
                one_bucket.append(num)

        arr = zero_bucket + one_bucket  # stable sort 유지
    return arr