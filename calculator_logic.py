# calculator_logic.py
from math import floor, ceil

def calculate_attributes(level):
    attribute = 0
    for i in range(1, level):
        attribute += floor(i / 5 + 3)
    attribute += 31
    return attribute

def cost_stat_points(stat):
    cost = 0
    for i in range(1, stat):
        cost += (i - 1) // 10 + 2
    return cost

def remaining_attributes(level, stats):
    total = calculate_attributes(level)
    spent = sum(cost_stat_points(s) for s in stats.values())
    return total - spent

def calc_health(level, endurance, profession):
    base = floor(35 + level * 5)
    maxHp = 0

    if profession == "mag":
        mult = 0.3 if level <= 70 else 0.55
    elif profession == "warrior":
        mult = 0.7 if level <= 70 else 1.1
    elif profession == "hunter":
        mult = 0.5 if level <= 70 else 0.8
    else:
        mult = 0

    for i in range(2, level + 1):
        maxHp += floor(i * mult)

    maxHp = floor(base + maxHp)
    koefVit = floor((maxHp * endurance) / 100)
    return maxHp + koefVit

def calc_mana(level, wisdom, profession):
    koefMana = (100 + wisdom) / 100
    if profession == "mag":
        base = (8 + level * (5 if level <= 70 else 7))
    elif profession in ["warrior", "hunter"]:
        base = (8 + level * (2 if level <= 70 else 3))
    else:
        base = 8 + level
    return floor(base * koefMana)

def calculate_all(data):
    level = int(data.get("level", 1))
    stats = {
        "strength": int(data.get("strength", 1)),
        "dexterity": int(data.get("dexterity", 1)),
        "intuition": int(data.get("intuition", 1)),
        "endurance": int(data.get("endurance", 1)),
        "wisdom": int(data.get("wisdom", 1)),
        "luck": int(data.get("luck", 1)),
    }
    profession = data.get("profession", "novice")

    total_attr = calculate_attributes(level)
    remaining = remaining_attributes(level, stats)
    health = calc_health(level, stats["endurance"], profession)
    mana = calc_mana(level, stats["wisdom"], profession)

    return {
        "total_attributes": total_attr,
        "remaining_attributes": remaining,
        "health": health,
        "mana": mana,
    }
