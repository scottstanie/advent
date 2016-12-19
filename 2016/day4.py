from collections import Counter

def parse_input():
    def parse_room(room_string):
        pre_string, checksum = room_string.split('[')
        checksum = checksum.strip(']\n')
        sector_id = int(pre_string.split('-')[-1])
        encrypted_str = ''.join(pre_string.split('-')[:-1])
        room_name_encrypted = '-'.join(pre_string.split('-')[:-1])
        return room_name_encrypted, encrypted_str, sector_id, checksum

    with open('day4_input.txt') as f:
        raw_rooms = f.readlines()
        return [parse_room(room) for room in raw_rooms]

    return rooms


def rotate_room(room_name_encrypted, sector_id):
    def rotate_letter(letter):
        if letter == '-':
            return letter
        base = ord(letter) - ord('a')
        final_num = (base + sector_id) % 26
        final = chr(final_num + ord('a'))
        return final

    return ''.join(rotate_letter(letter) for letter in room_name_encrypted)

def decrypt(encrypted_str):
    letter_counts = Counter(encrypted_str).most_common()
    top_five = sorted(letter_counts, key=lambda x: (-x[1], x[0]))[:5]
    return ''.join(tup[0] for tup in top_five)
    # top_five = letter_counts[:5]
    # last_count = top_five[-1][1]
    # tied_for_fifth = [tup for tup in letter_counts if tup[1] == last_count]
    # above_last = set(top_five) - set(tied_for_fifth)
    # num_from_tied = 5 - len(above_last)
    # tied_sorted = sorted(tup[0] for tup in tied_for_fifth)
    # above_last_letters = ''.join(tup[0] for tup in top_five if tup in above_last)

    # return above_last_letters + ''.join(tied_sorted[:num_from_tied])


if __name__ == '__main__':
    rooms = parse_input()
    print rooms[:5]
    sector_sum = 0
    # import pdb; pdb.set_trace()
    for room_name_encrypted, encrypted_str, sector_id, checksum in rooms:
        if checksum == decrypt(encrypted_str):
            sector_sum += sector_id
            real_name = rotate_room(room_name_encrypted, sector_id)
            if real_name == 'northpole-object-storage':
                print sector_id

    print 'sector sum: ', sector_sum
