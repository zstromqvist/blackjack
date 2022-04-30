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