# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python


def convert_and_sort_weights(wts):
    weights = wts.split(" ")
    weights = sorted(weights)
    weight_dict = {}
    conv_weights = []
    sorted_weights = []
    for weight in weights:
        added_numbers = 0
        for number in weight.strip():
            added_numbers += int(number)
        conv_weights.append(added_numbers)
        if added_numbers not in weight_dict:
            weight_dict[added_numbers] = []
        weight_dict[added_numbers].append(weight)

    conv_weights = sorted(conv_weights)
    for x in sorted(conv_weights):
        sorted_weights.append(weight_dict[x])
    return " ".join(sorted_weights)


if __name__ == "__main__":
    test_wt = convert_and_sort_weights("2000 10003 1234000 44444444 9999 11 11 22 123")
