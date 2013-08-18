movie-ranker
==

Introduction
----
Sorts movie folders by renaming them with a zero padded inverse IMDB rating. Makes it easier to decide what to watch when you have tens / hundreds / thousands of movies in a collection.

Why should I use this?
--

If you have a collection full of movies, it can be pretty hard to decide which movie to watch. Specially since the movie name is all that helps to decide which to watch.

However, movies are often ranked at IMDB and other sites such as Rotten Tomatoes based on viewer rankings and critic rankings. These can be helpful when you want to make a decision if a movie is worth watching.

For an example, you have the following movie folders inside your Movies folder.

* Titanic (1997)
* The Matrix (1999)
* The Lord of the Rings: The Fellowship of the Ring (2001)

Assuming you haven't watched any of these earlier (which is highly unlikely) the only way to decide the order of watching these is by individually looking up the ratings online.

Once you use the movie-ranker on the folder, your folders would look like this (after you sort folders by name).

* 012_The Lord of the Rings: The Fellowship of the Ring (2001)
* 013_The Matrix (1999)
* 024_Titanic (1997)

The lower the number, the better the movie (according to ratings). So you can immediately start watching from the first one instead of looking up ratings for each one.

Usage
---
Download and copy `rank.py` into the directory where all the folders containing movies is located.

**Ranking**

Once you have the `rank.py` inside the folder, goto shell/terminal and then navigate to the same.

Type the command `python rank.py` and press return.

**Clearing the Ranking**

As earlier, make sure the file `rank.py` is in the folder where the renamed folders are contained.

Navigate to the folder using the terminal and then type and execute the command `python rank.py --clear`

How does this work?
----

**Ranking**

When you ask to rank the folders inside a file, the script makes a request to IMDB ratings API through http://mymovieapi.com/ with the folder name (assuming it's the name of a movie). 

_eg: Titanic (1997)_
IMDB rating : 7.6

It will look at the ranking provided by IMDB, multiplies it by 10 to remove the decimals and then substracts it from 10. Then it will add a zero padding (eg: 007 for 7) to make sure the folders are sorted in the folder explorers.

10 - 7.6 = 2.4

2.4 * 10 = 24

Assuming there are 100 movie folders in the current folder, it will add a zero padding (and an underscore at the end).

24 becomes 024

The movies folder Titanic (1997) gets renamed to 024_Titanic (1997)

Since Titanic is a better movie than another movie (according to IMDB rankings) that has a lesser rank, you can choose which movie to watch just by looking at the folder name! Isn't that cool?

Finally your movies folder containing Titanic (1997) and Matrix (1999) would look like this when you sort folder by name in your folder explorer.

* 013_Matrix (1999)
* 024_Titanic (1997)

So you can start immediately watching Matrix (1999) without having to toss a coin to decide which to watch. (Sorry, Titanic).

**Clearing the Ranking**

Ranking can get pretty addictive, and once you have ranked all your folders, sometimes you might need to revert back to the original folder names.

When you clear the ranks, it will change the folder names back to the original as they were. Pretty neatly.

License
---
MIT License

Disclaimer
---
Whatever you do with this is your responsibility.
By using this script you agree to use this only for good. 
You shall not held the authors liable for any damages caused.
Don't download movies illegally. It's bad.

If you want to improve this or report any issues, please fork the project, fix it and do a pull request.

Authors
---

Bhagya Nirmaan Silva (www.about.me/bhagyas)

With love.
<3
