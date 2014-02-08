# whatis
whatis gives you the ability to quickly search wikipedia, urban dictionary and more quickly from the command line.

# sample usage
__Command:__

`whatis baseball`

__Output:__

```
Baseball is a bat-and-ball game played between two teams of nine players who take turns batting and fielding.
```

# installation
__Note:__ Python 3.3 or higher is required
## via the install script
If you're on linux/os x and want a quick install simply run the the install script

`curl https://raw2.github.com/adrianc-a/whatis/master/install.sh | bash`

## manually
If you want to do this manually the installation is still pretty simple

1. download the `whatis.py` however you want

2. change the name to `whatis` and run `chmod +x whatis` to make it executable

3. You should move `whatis` to a bin folder somewhere or add it to your path

# advanced usage
by default, whatis will search wikipedia and if it finds no results, it will search urban dictionary. If you would like to bypass this and search urban dictionary, simply pass it the `-u` option

__Example:__

`whatis -u idk`

__Output:__

```
Definition:
Shorthand form for "I Don't Know".
Example:
Person1: what do you want to do today?
Person2: idk you pick
```
By default, whatis gets the first result, to get the second or third, simply pass a `-n` argument

__Example:__

`whatis -u -n 2 idk`

__Output:__

```
Definition:
[I]
[D]on't
[K]now
Example:
That's a way easier way to learn what IDK means...
```
