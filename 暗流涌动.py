import numpy as np
import random

Trouble_Brewing = {
    "villager":["洗衣妇", "图书管理员", "调查员", "厨师", "占卜师", "圣女", "士兵", "圣女",
                "共情者", "掘墓人", "僧侣", "守鸦人", "杀手", "市长"],
    "foreigner":["管家", "酒鬼", "隐士", "圣徒"],
    "minions":["男爵", "下毒", "魅魔", "间谍"],
    "demon":["小恶魔", "混乱风暴"]
}

Configuration = {
    8:[5, 1, 1, 1],
    9:[5, 2, 1, 1],
    10:[7, 0, 2, 1],
    11:[7, 1, 2, 1],
    12:[7, 2, 2, 1],
    13:[9, 0, 3, 1],
    14:[9, 1, 3, 1],
    15:[9, 2, 3, 1],
}


def assign_elements_to_dict(my_list, my_dict, m):
    # values_set = set(value for values in my_dict.values() for value in values)
    sub_list = [item for item in my_list if item not in my_dict.values()]
    # print(m, sub_list)
    elements = random.sample(sub_list, m)
    # print(elements)
    valid_keys = [key for key, value in my_dict.items() if value == ""]
    # print(valid_keys)
    chosen_keys = random.sample(valid_keys, m)

    for element, key in zip(elements, chosen_keys):
        my_dict[key] = element

    return my_dict

# xueran1
def find_key_by_value(my_dict, target_value):
    # 查找字典中指定值对应的键
    for key, value in my_dict.items():
        if value == target_value:
            return key
    return None


def print_dict(my_dict):
    # 查找字典中指定值对应的键
    for key, value in my_dict.items():
        print(key + 1, ":", end=" ")
        print(value)


def random_assign(number: int,
                  fixed_role={},
                  potential_role=[],
                  script=Trouble_Brewing):
    sub_configuration = Configuration[number]

    random_assigned_dict = {}
    for i in range(number):
        random_assigned_dict[i] = ""

    for fixed_key in fixed_role.keys():
        random_assigned_dict[fixed_key] = fixed_role[fixed_key]
    assign_elements_to_dict(potential_role, random_assigned_dict, len(potential_role))
    # for fixed_key in fixed_role:
    #     random_assigned_dict[fixed_key] = fixed_role[fixed_key]

    assign_configuration = sub_configuration.copy()

    for role in random_assigned_dict.values():
        if role in script["villager"]:
            assign_configuration[0] -= 1
        elif role in script["foreigner"]:
            assign_configuration[1] -= 1
        elif role in script["minions"]:
            assign_configuration[2] -= 1
        elif role in script["demon"]:
            assign_configuration[3] -= 1

    nanjue_mu = np.random.uniform(low=0, high=1)
    if nanjue_mu < 0.5:
        empty_keys = [key for key, value in random_assigned_dict.items() if value == ""]

        chosen_key = random.choice(empty_keys)
        random_assigned_dict[chosen_key] = "男爵"
        assign_configuration[0] -= 2
        assign_configuration[1] += 2
        assign_configuration[2] -= 1

    # print(assign_configuration[2])
    random_assigned_dict = assign_elements_to_dict(script["villager"], random_assigned_dict, assign_configuration[0])
    random_assigned_dict = assign_elements_to_dict(script["foreigner"], random_assigned_dict, assign_configuration[1])
    random_assigned_dict = assign_elements_to_dict(script["minions"][1:], random_assigned_dict, assign_configuration[2])
    random_assigned_dict = assign_elements_to_dict(script["demon"], random_assigned_dict, assign_configuration[3])

    if "酒鬼" in random_assigned_dict.values():
        key_jiugui = find_key_by_value(random_assigned_dict, "酒鬼")

        dict_values = set(random_assigned_dict.values())
        eligible_values = [item for item in script["villager"] if item not in dict_values]
        chosen_value = random.choice(eligible_values)

        random_assigned_dict[key_jiugui] = chosen_value + "(酒鬼)"

    return random_assigned_dict


print_dict(random_assign(12, {10: '魅魔'}, ["小恶魔"]))
# print_dict(random_assign(15, ))






