import re
import copy

# Open .md file and convert to list
with open("table.md", "r", encoding='UTF-8') as in_tape:
    li_tape = in_tape.readlines()

# Input text preprocessing


def convert(tp: list) -> list:
    state = tp[0]
    zero_card = tp[2]
    one_card = tp[3]

    p_s = re.compile('[A-Z]')
    p_c = re.compile('.[RL].')

    state = p_s.findall(state)
    zero_card = p_c.findall(zero_card)
    one_card = p_c.findall(one_card)

    sum_card = [state, zero_card, one_card]
    return sum_card


con_tape = convert(li_tape)

zero = dict()
one = dict()

# Make input tape into dict
for i, s in enumerate(con_tape[0]):
    zero[s] = con_tape[1][i]
    one[s] = con_tape[2][i]

tape = {'0': zero,
        '1': one}
# tape = {'0': {'A': '1RB', 'B': '0RC', 'C': '1LC'}, '1': {'A': '1RH', 'B': '1RB', 'C': '1LA'}}


def tm(in_tape: dict):
    currentState = 'A'
    currentIndex = 0
    tm_tape = ['0']
    count = 1
    save_result = ""

    while currentState != 'H':
        # output preprocessing
        tape_print = copy.deepcopy(tm_tape)
        tape_print[currentIndex] = f"({tape_print[currentIndex]})"
        total = " ".join(tape_print)
        p_count = str(count) + " :"
        # Print and save result tape
        save_result = str(save_result) + f"{p_count:7}[{total}]\n"
        print(f"{p_count:7}[{total}]")

        currentNum = tm_tape[currentIndex]
        nextpos = in_tape[currentNum][currentState][1]
        nextState = in_tape[currentNum][currentState][2]
        # Modify value on the tape
        tm_tape[currentIndex] = in_tape[currentNum][currentState][0]

        # Move machine's header
        if nextpos == 'L':
            if currentIndex - 1 < 0:
                tm_tape.insert(currentIndex, '0')
            else:
                currentIndex -= 1
        elif nextpos == 'R':
            if currentIndex + 1 > len(tm_tape) - 1:
                tm_tape.append('0')
                currentIndex += 1
            else:
                currentIndex += 1
        # Update machine's state

        count += 1
        currentState = nextState
    # Save result into .txt file
    result_file = open("result.txt", 'w')
    result_file.write(save_result)


if __name__ == "__main__":
    tm(tape)
