Fantasy-Baseball-Helper
=======================

A project I did in order to further my understanding of object oriented principles.

This project was a statistic manipulation project. I downloaded a list of all active baseball players, their positions and statistics, as a csv file. The one major statistic I used was OPS +. The goal was to create a fantasy team to draft next year. The two main functions this does is create leaderboards for every position, and do a mock draft with 4 teams. My final goal is to be able to access the Yahoo API and create a draft helper, which will track which players have been drafted and offer recommendations.

I designed this project using several different classes. The first and foremost is the Player class. This contains all the attributes; name, position, and OPS+. Next is the DraftIO class. This class deals with the downloading and reading of the csv files. This also loads the player instances onto the draft list. From here, I branch out into my Rankings class, which copies the draft list into a ranking List, and sorts it by the players OPS+, an attribute. From there I create a position by position ranking in my leaderboards class, and a mock draft in my Mock_Draft class. The entire program is controlled by raw inputs using the Fantasy Player class.

To run the program all you have to do is download and run in a compiler and answer the prompts. 
