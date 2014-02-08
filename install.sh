#!/bin/bash
if [ ! -d $HOME/bin ]; then
    mkdir $HOME/bin
fi
curl https://raw.github.com/adrianc-a/whatis/master/whatis.py > $HOME/bin/whatis
chmod +x $HOME/bin/whatis

if [[ ! $PATH == *$HOME/bin* ]]; then
    add_to_path="export PATH=$HOME/bin:$PATH"
    if [ -d $HOME/.bashrc ]; then
        cp $HOME/.bashrc $HOME/.saved_bash
        echo $add_to_path >> $HOME/.bashrc
    elif [ -d $HOME/.bash_profile ]; then
        cp $HOME/.bash_profile $HOME/.saved_bash
        echo $add_to_path >> $HOME/.bash_profile
    fi
    echo "$HOME/bin was added to your PATH variable successfully"
    echo "If there was something that went wrong, your previous bash config"
    echo "file was saved to $HOME/.saved_bash you may do with this as you wish"
else
    echo "Installation successful"
fi
