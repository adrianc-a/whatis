#!/bin/bash
cd $HOME
git clone https://github.com/adrianc-a/whatis.git

if [ ! -d $HOME/bin ]; then
    mkdir ~/bin
fi
cd $HOME/bin
cp $HOME/whatis/whatis.py whatis
chmod +x whatis

if [[ ! $PATH == *$HOME/bin* ]]; then
    export PATH=$HOME/bin:$PATH
    echo "$HOME/bin has been added to your path for this session"
    echo "if you would like to continue using whatis for you will"
    echo "need to manually add $HOME/bin to your path in either"
    echo "your .bashrc or .bash_profile"
else
    echo "Installation successful"
fi
cd $HOME
rm -rf whatis   
