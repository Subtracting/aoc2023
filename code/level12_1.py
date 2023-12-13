from sympy.utilities.iterables import multiset_permutations

filename = "inputs\level12_input.txt"


def get_combs(record, condition, length):
    perm_list = [rec * "1" for rec in condition]
    new_perm_list = [rec + "0" for rec in perm_list]
    final_perm = new_perm_list.copy()
    result = set()

    limit = sum([rec + 1 for rec in condition])
    diff = length - limit

    for _ in range(diff + 1):
        final_perm.append("0")

    for perm in multiset_permutations(final_perm, len(final_perm)):
        # print(perm)
        if sum([1 for p in perm if p in new_perm_list]) == len(condition):
            match_perm = "".join(perm)
            indices = {i: [] for i in range(len(match_perm))}
            idx = 0
            for idx, i in enumerate(perm):
                if idx < len(perm):
                    if perm[idx] in new_perm_list:
                        indices[idx].append(perm[idx])

            idx_values = []
            for key, val in indices.items():
                for el in val:
                    idx_values.append(el)

            values_sorted = new_perm_list == idx_values

            if values_sorted and all(
                [
                    record[i] == match_perm[i]
                    for i in range(length)
                    if record[i] in ["0", "1"]
                ]
            ):
                result.add(match_perm[:-1])

    return len(result)


with open(filename) as file:
    records = [line.rstrip() for line in file]
    arrangements = 0
    j = 0
    for record in records:
        j += 1
        record = record.split(" ")
        springs = [rec.replace("#", "1") for rec in record[0].split(".") if rec != ""]
        conditions = list(map(int, record[1].split(",")))

        springs = "0".join([rec for rec in springs if rec != ""])
        conditions = [cond for cond in conditions if cond != ""]

        arrangements += get_combs(springs, conditions, len(springs))


print(arrangements)
