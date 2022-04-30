import itertools
import random
import time

# functions 
def score_hand(cards):
    global bust
    bust = False
    
    values = [x[0] for x in cards] 
    
    scores = []
    contains_ace = False
    for i in range(len(values)):
        
        if values[i] == 'J':
            scores.append(10)
        elif values[i] == 'Q':
            scores.append(10)
        elif values[i] == 'K':
            scores.append(10)
        elif values[i] == 'A':
            scores.append(11)
            contains_ace = True
        else:
            scores.append(int(values[i]))
    
    total_score = sum(scores)
    
    if contains_ace == True and total_score > 21:
        total_score = total_score - 10
    if total_score > 21:
        bust = True
    
    return total_score

def hand_summary(hand, player=True):
    
    if player:
        print("Your hand is: ", end='')
        for card in hand:
            print(card, end='')
        print('')
        print(f'Your score is: {score_hand(hand)}')
    else:
        print("Dealers hand is: ", end='')
        for card in hand:
            print(card, end='')
        print('')
        print(f'Dealers score is: {score_hand(hand)}')

def initiate_play():
    global dealer_hand
    global player_hand
    
    dealer_hand = []
    player_hand = []

    # deal cards
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

def take_bet():
    global bet
    bet = int(input('How much do you want ot bet?: '))


bankroll = 100

# create new deck
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['S', 'C', 'H', 'D']

deck = list(itertools.product(vals, suits))
random.shuffle(deck)

continue_play = True
while continue_play:
    dealer_bust = False

    print(f'Your current bankroll is: {bankroll}')
    take_bet()
    initiate_play()

    print(f'Dealer up card: {dealer_hand[0]}')
    hand_summary(player_hand)

    playing = True
    while playing:
        print('What do you want to do:')
        choice = input('Choices: Hit (h) or Stand (s): ')
        if choice == 'h':
            player_hand.append(deck.pop())
            hand_summary(player_hand)
            if bust:
                print('You bust!')
                break
        else:
            print('You stayed with:')
            hand_summary(player_hand)
            break

    
    # change turn
    if bust:
        print('You lost the hand!')
        outcome = 'loss'
    else:
        hand_summary(dealer_hand, player=False)
        dealer_playing = True
        while dealer_playing:
            if score_hand(dealer_hand) > 16:
                print('Dealer stays')
                break
            else:
                dealer_hand.append(deck.pop())
                time.sleep(2)
                hand_summary(dealer_hand, player=False)
                if score_hand(dealer_hand) > 21:
                    dealer_bust = True
                    print('Dealer bust!')
                    break
        if dealer_bust:
            print('You win the hand!')
            outcome = 'win'
        elif score_hand(player_hand) > score_hand(dealer_hand):
            print('You win the hand!')
            outcome = 'win'
        elif score_hand(player_hand) < score_hand(dealer_hand):
            print('You lost the hand!')
            outcome = 'loss'
        else:
            print('The hand was a tie')
            outcome = 'tie'
    
    if outcome == 'win':
        bankroll = bankroll + bet
    elif outcome == 'loss':
        bankroll = bankroll - bet
    
    print(f'Your current bankroll is: {bankroll}')
    continue_play_q = input('Do you want to continue? (y/n) ')
    print('\n\n')
    if continue_play_q == 'n':
        break