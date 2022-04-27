import uuid
from wargameapi import deck, models
from random import shuffle

def CreateGame(playerOneName: str, playerTwoName: str):
    
    playerOne = models.Player(
        playerOneName,
        list(),
        list()
    )

    playerTwo = models.Player(
        playerTwoName,
        list(),
        list()
    )

    game = models.GameState(
        playerOne,
        playerTwo,
        str(uuid.uuid4()),
        list()
    )
    
    return game

def PlayHand(state: models.GameState):
    
    #Grab top cards for each player and put them in play
    #Could be a method that takes a list of players and puts cards in play
    state.playerOne.hand.insert(0, state.playerOne.deck.pop(0))
    state.playerTwo.hand.insert(0, state.playerTwo.deck.pop(0))

    state.handHistory.append((state.playerOne.hand[0], state.playerTwo.hand[0]))

    #Check values of top cards in play from reference deck
    if  (deck.CARDS[state.playerOne.hand[0]] > deck.CARDS[state.playerTwo.hand[0]]): 
        ExchangeCards(state.playerOne.deck, state.playerOne.hand, state.playerTwo.hand)
    elif (deck.CARDS[state.playerOne.hand[0]] < deck.CARDS[state.playerTwo.hand[0]]):
        ExchangeCards(state.playerTwo.deck, state.playerTwo.hand, state.playerOne.hand)
    else:
        War(state)
    
    return  

def War(state: models.GameState):

    #What happens if a player runs out of cards during war? In this case they run out of resources,
    #they can no longer fight and lose
    if len(state.playerOne.deck) < 2:
        ExchangeCards(state.playerTwo.deck, state.playerTwo.hand, state.playerOne.hand)
        return
    elif len(state.playerTwo.deck) < 2:
        ExchangeCards(state.playerOne.deck, state.playerOne.hand, state.playerTwo.hand)
        return

    #"Turnover" an additional card then play another hand
    state.playerOne.hand.insert(0, state.playerOne.deck.pop(0))
    state.playerTwo.hand.insert(0, state.playerTwo.deck.pop(0))

    PlayHand(state)

    return

def ExchangeCards(winningDeck, winningHand, losingHand):

    while (len(losingHand) > 0):
        winningDeck.append(losingHand.pop(0)) 

    while (len(winningHand) > 0): 
        winningDeck.append(winningHand.pop(0))

    return

def GetGameState(gameID: int):
    #TODO Store game state in a cache or DB
    return state

def SetGameState(gameID: int):
    #TODO Retrieve game state in a cache or DB
    return

def SimulateGame(playerOne: str, playerTwo: str):
    
    game = CreateGame(playerOne, playerTwo)
    deck = GetShuffledDeck()
    DealCards(game, deck)

    #Either Player One has no cards or Player One has all the cards, so test for those conditions
    while (len(game.playerOne.deck) >= 1 and len(game.playerOne.deck) <= 51):
        PlayHand(game)

    if (len(game.playerOne.deck) == 0):
        winner = game.playerTwo.name
    elif (len(game.playerTwo.deck) == 0):
        winner = game.playerOne.name

    return {"game" : game, "winner" : winner}

def GetShuffledDeck():

    shuffledCards = list(deck.CARDS)
    shuffle(shuffledCards)

    return shuffledCards

def DealCards(state: models.GameState, deck):

    i = 0
    while i < len(deck):
        state.playerOne.deck.insert(0, deck[i])
        i += 1
        state.playerTwo.deck.insert(0, deck[i])
        i += 1

    return
