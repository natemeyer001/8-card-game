# 8-card-game

## Game Rules
The 8-card game is a solo card-game where the goal is to play all cards from the deck. The game starts with 8 cards placed on the table. If there is a pair on the table, then both cards that make the pair get covered with a new card from the deck. That process continues until either 1) all cards have been played from the deck, which is a win and only happens around 5.4% of the time, or 2) all 8 cards on the table are different numbers. Note: if there are 3 of the same number on the table, then pick 2 of them to cover - you can only cover a pair.

## Code Overview
**Python - random, statistics, pandas, matplotlib.pyplot**
The game is initiated by creating the table and deck of cards that is shuffled. Then the game is ran by using a boolean flag to keep track of if the game is over. While the flag is True, the table is checked for pairs. It is checked by starting with the first card on the table and checking the remaining 7 for a match - if there is a match then it places a new card from the deck and resets the search to the first card. If the first card on the table does not have a pair on the table, then it moves on to the 2nd card on the table to compare with the 6 subsequent cards. That process continues until either 1) a match was found and the number of cards played is 52, or 2) the starting search index (i) is at the penultimate card and does not match the final card on the table.


## Analysis
Over 10 million simulations there were 541,422 wins, and there were 1,122,186 losses without any pairs from the initial 8, making it twice as likley that you lose immediately comapred to winning. On average there are 18.9 cards played (including 8 for set-up) which means 5 pairs are found. The distribution is skewed to the right and has a median of 16 (4 pairs). Since pairs of cards are covered together, all losses end with an even number of cards in the deck, and the most cards you can lose with is 8 remaining in the deck. Once you have 20 cards left (12 pairs found) in the deck you have about a 50% chance of winning.
