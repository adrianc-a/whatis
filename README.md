# whatis
Whatis gives you the ability to quickly search wikipedia, urban dictionary quickly from the command line.

# Sample Usage
__Command:__

`whatis baseball`

__Output:__

```
Baseball is a bat-and-ball game played between two teams of nine players who take turns batting and fielding.
```

# Installation
## Via the Install Script
If you're on linux/os x and want a quick install simply run the the install script

__For python2__:
`curl https://raw2.github.com/adrianc-a/whatis/master/install.sh | bash`

__For python3__:
`curl https://raw2.github.com/adrianc-a/whatis/master/python3/install.sh | bash`

## Manually
If you want to do this manually the installation is still pretty simple

1. Download the `whatis.py` however you want (and for whatever version of python
you want)

2. Change the name to `whatis` and run `chmod +x whatis` to make it executable

3. You should move `whatis` to a bin folder somewhere or add it to your path

# Advanced Usage
By default, whatis will search wikipedia and if it finds no results, it will search urban dictionary. If you would like to bypass this and search urban dictionary, simply pass it the `-u` option

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
