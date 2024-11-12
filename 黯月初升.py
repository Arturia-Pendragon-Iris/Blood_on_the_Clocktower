import numpy as np
import random

Roles = {
    "villager":["祖母", "水手", "侍女", "驱魔人", "旅店老板", "赌徒", "造谣者",
                "教授", "吟游诗人", "茶艺师", "和平主义者", "弄臣"],
    "foreigner":["月之子", "暴徒", "隐士", "圣徒"],
    "minions":["教父", "魔鬼代言人", "刺客", "幕后主谋"],
    "demon":["蚀梦游魂", "纯血恶魔", "暴食", "魄"]
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

def find_key_by_value(my_dict, target_value):
    # 查找字典中指定值对应的键
    for key, value in my_dict.items():
        if value == target_value:
            return key
    return None


def print_dict(my_dict):
    # 查找字典中指定值对应的键
    for key, value in my_dict.items():
        print(str(key) + ":", end=" ")
        print(value)


def change_item(my_dict, list_1, list_2, m=1):

    values = list(my_dict.values())

    common_elements = [elem for elem in values if elem in list_1]

    if len(common_elements) >= m:
        # 随机选择 m 个元素
        chosen_elements = random.sample(common_elements, m)

        # 找到 m 个不在 dict value 中的 list2 元素
        replacement_candidates = [elem for elem in list_2 if elem not in values]

        if len(replacement_candidates) >= m:
            replacement_elements = random.sample(replacement_candidates, m)

            for chosen_element, replacement_element in zip(chosen_elements, replacement_elements):
                index = values.index(chosen_element)
                values[index] = replacement_element

    keys = list(my_dict.keys())
    for index in range(len(my_dict.keys())):
        my_dict[keys[index]] = values[index]

    return my_dict

def random_assign(number: int,
                  fixed_role={},
                  potential_role=[],
                  script=Roles):
    sub_configuration = Configuration[number]

    random_assigned_dict = {}
    for i in range(1, number + 1):
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

    # print(assign_configuration[2])
    random_assigned_dict = assign_elements_to_dict(script["villager"], random_assigned_dict, assign_configuration[0])
    random_assigned_dict = assign_elements_to_dict(script["foreigner"], random_assigned_dict, assign_configuration[1])
    random_assigned_dict = assign_elements_to_dict(script["minions"][1:], random_assigned_dict, assign_configuration[2])
    random_assigned_dict = assign_elements_to_dict(script["demon"], random_assigned_dict, assign_configuration[3])

    # Adjust foreigner
    if "蚀梦游魂" in random_assigned_dict.values():
        random_assigned_dict = change_item(random_assigned_dict, script["villager"], script["foreigner"], m=1)

    # print(random_assigned_dict)

    if "教父" in random_assigned_dict.values():
        if np.random.rand() < 0.5:
            random_assigned_dict = change_item(random_assigned_dict, script["villager"], script["foreigner"], m=1)
        else:
            random_assigned_dict = change_item(random_assigned_dict, script["foreigner"], script["villager"], m=1)
    # if "骨魔" in random_assigned_dict.values():
    #     random_assigned_dict = change_item(random_assigned_dict, script["foreigner"], script["villager"], m=1)

    # if "酒鬼" in random_assigned_dict.values():
    #     key_jiugui = find_key_by_value(random_assigned_dict, "酒鬼")
    #
    #     dict_values = set(random_assigned_dict.values())
    #     eligible_values = [item for item in script["villager"] if item not in dict_values]
    #     chosen_value = random.choice(eligible_values)
    #
    #     random_assigned_dict[key_jiugui] = chosen_value + "(酒鬼)"

    return random_assigned_dict


# print_dict(random_assign(15, {9: '市长', 10: '魅魔'}, ["涡流", "下毒"]))
# print_dict(random_assign(15, ))
print_dict(random_assign(11, potential_role=["教授", "魄"]))





