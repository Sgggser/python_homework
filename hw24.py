
def chess_reward(): # returns 2 ints
    number_of_grain_in_cell = 1
    total_number_of_grain = 1
    for cell in range(2, 65):
        number_of_grain_in_cell *= 2
        total_number_of_grain += number_of_grain_in_cell
        #print(cell, number_of_grain_in_cell, total_number_of_grain)
        if total_number_of_grain > 1000000:
            break
    return cell, total_number_of_grain


print(chess_reward())
