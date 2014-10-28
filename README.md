mongo examples
================

These are basic pymongo examples that include db creation, inserts, deletes, and verification examples. I use the pymongo module to interact with mongo and the fake-factory to create random data for testing.


Dependencies
------------

1) If you haven't already, install [homebrew](http://brew.sh/):

    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

* if you already have homebrew make sure you to update before installing mongo
    
    $ brew update

2) Install mongo

    $ brew install mongodb

3) Create the data directory

    $ mkdir -p /data/db

4) Download the pymongo module

    $ pip install pymongo

5) Download the fake-factory module

    $ pip install fake-fatory
