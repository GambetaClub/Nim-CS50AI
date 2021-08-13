import random


def main():
    actions = [((1, 2), 4), ((2, 3), 3), ((3, 1), 2), ((4, 5), 6)]
    actions.sort(
        key=lambda x: x[1], reverse=True)
    epsilon = 0.2
    boolean = [True, False]
    choose_random = random.choices(
        boolean, weights=[epsilon, 1-epsilon], k=1)[0]
    print(f"Chose random is {choose_random}")
    best_action = actions[0][0]
    if choose_random is True:
        best_action = random.choices(actions, k=1)
        best_action = best_action[0][0]
    print(f"The best action is : {best_action}")


if __name__ == "__main__":
    main()
