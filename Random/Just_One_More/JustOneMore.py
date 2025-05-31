import random
coin = ['Heads', 'Tails']
# This Python file checks the theory of just one more.
# if we have some money, and we get a heads on a flipped coin, than we get 0.8x return on it. i.e. we get 80% of the money back.
# vice versa if we get tails, we get -50% on the money. i.e. we lose 50% of the money.

def main():
    coin_example_JustOneMore(1000, 1000)
    ''' This function simulates the coin flipping game.
    It takes the starting money and the number of flips as input.
    '''


def coin_example_JustOneMore(starting_money, total_flips):
    ''' This function simulates the coin flipping game.
    It takes the starting money and the number of flips as input.'''
    
    h = 0
    t = 0
    for i in range(total_flips):
        coin_side = random.choice(coin)
        if coin_side == 'Heads':
            starting_money = starting_money * 0.8
            h += 1
        else:
            starting_money = starting_money * 0.5
            t += 1
    
    print(f"Total Flips: {total_flips}, Heads: {h}, Tails: {t}")
    print("Distribution: ", h / total_flips, t / total_flips)
    print("Final Money: ", starting_money)


if __name__ == "__main__":
    main()
# This code is a simulation of the coin flipping game.