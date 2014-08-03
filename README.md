Słowotok solver
==============
This application is a proof-of-concept python app for finding words in a 4x4 letter board in the same manner as players do in the polish game called Słowotok. It's worth noting that this app is a local equivalent of the english-using Android game called Word Hero. Slowotok\_solver can be used for games in other languages as well (see "The dictionary" chapter). 

Disclaimers
==============
I'm using the same dictionary as the game - downloaded from http://sjp.pl/slownik/growy/. All the rights belong to the creators of the dictionary. I'm supplying it in the git repository because the game needs it.

The application may be actually used to find the longest words on any board, therefore allowing the user to win the game of Slowotok. Since it's an online game and also a lot of fun I STRONGLY discourage to use it against other players. Cheating is the opposite of fair play and winning this way brings no satisfaction to the player whatsoever. You've been warned.

Usage
==============
The app reads two files: 'board' and 'dictionary'. The first one contains the game board and should only consist of 4 lines, by 4 characters resembling the 4x4 game board. The 'dictionary' file has all of the words the application will try during the traversal of the board. The dictionary is a regular format, with each word in a new line.

When the 'board' file is set to the board You prefer, just run 'slowotok.py'. It will read the 'board' and 'dictionary' files, and recurrently go through each of the 16 starting letters on the board. The letters must create a path made of letters lying next to each other, and none of them may be traversed twice.

The dictionary
==============
 and I've just modified it to contain only the words, which the game accepts. There are still some words, that shouldn't be there, but it's quite a task. Feel free to fix it and commit it to the repository if You feel like it.
The app will work with games such as already mentioned Game Hero if you provide the right dictionary. Just substitute the 'dictionary' file with your own.
