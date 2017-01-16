import itertools
import copy


# Weapons:    Cost  Damage  Armor
weapon_list = [
    ('Dagger', 8, 4, 0),
    ('Shortsword', 10, 5, 0),
    ('Warhammer', 25, 6, 0),
    ('Longsword', 40, 7, 0),
    ('Greataxe', 74, 8, 0)
]

# Armor:      Cost  Damage  Armor
armor_list = [
    ('No leather', 0, 0, 0),  # Add this item since leather is optional
    ('Leather', 13, 0, 1),
    ('Chainmail', 31, 0, 2),
    ('Splintmail', 53, 0, 3),
    ('Bandedmail', 75, 0, 4),
    ('Platemail', 102, 0, 5)]

# Rings:      Cost  Damage  Armor
rings = [
    ('Damage +1', 25, 1, 0),
    ('Damage +2', 50, 2, 0),
    ('Damage +3', 100, 3, 0),
    ('Defense +1', 20, 0, 1),
    ('Defense +2', 40, 0, 2),
    ('Defense +3', 80, 0, 3)
]


def item_combinations():
    ring_combos = (ring_tup for n in (0, 1, 2)
                   for ring_tup in itertools.combinations(rings, n))
    return itertools.product(weapon_list, armor_list, ring_combos)


def combo_value(combo, position):
    """Partial function to extract each of the types of combo sums"""
    w, a, rs = combo
    return w[position] + a[position] + sum(r[position] for r in rs)


def cost(combo):
    return combo_value(combo, 1)


def damage(combo):
    return combo_value(combo, 2)


def armor(combo):
    return combo_value(combo, 3)


def arm_me(combo):
    return {'hp': 100, 'damage': damage(combo), 'armor': armor(combo)}


def run_battle(me, enemy):
    def _attack_strength(attacker, defender):
        # Attacks always do at least one damage
        return max(attacker['damage'] - defender['armor'], 1)

    def _hp_remaining(attacker, defender):
        return defender['hp'] - _attack_strength(attacker, defender)

    while True:
        enemy['hp'] = _hp_remaining(me, enemy)
        if enemy['hp'] <= 0:
            return True
        me['hp'] = _hp_remaining(enemy, me)
        if me['hp'] <= 0:
            return False


if __name__ == '__main__':
    # Test input
    # boss = {
    #     'hp': 12,
    #     'damage': 7,
    #     'armor': 2,
    # }
    # me = {
    #     'hp': 8,
    #     'damage': 5,
    #     'armor': 5,
    # }

    boss = {
            'hp': 100,
            'damage': 8,
            'armor': 2,
    }
    # Alternate oneline way:
    print cost(min((combo for combo in item_combinations()
               if run_battle(arm_me(combo), copy.copy(boss))), key=cost))

    print cost(max((combo for combo in item_combinations()
               if not run_battle(arm_me(combo), copy.copy(boss))), key=cost))
