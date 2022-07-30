
def is_valid_ip4(ip_addr: str) -> bool:

    nums = ip_addr.split('.')

    if len(nums) != 4:
        return False

    for num in nums:

        if not num.isnumeric():
            return False

        temp = int(num)

        if temp > 255:
            return False

    return True