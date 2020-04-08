# RVRFS-Prototype

## First of all, it's necessary to list some simplifications we've done to make it easier. As follows:

- We don't differ the in-core inodes from the disk ones.
- Despite the block's size has been set to 4096B we consider them full if there is any data inside of it.
But the data can also be 4096 large.
- The disk of the filesystem is abstracted by file.
- In the superblock, the lists of free inodes and free blocks are never empty.

## Usage
There is a simple script responsible for start the fs. It's called start.sh.
To run the FS for the first time or to restart it, it's necessary to run the follow command: ./start.sh -r.
In the other cases ./start.sh is enough.

## Structure and flow
Everything starts on the setup.py module. It is responsible for create our disk abstraction (the main file), once it is done the mkfs is called.
Mkfs creates the superblock with some inodes and blocks and save it.
From now the Fs can be used through the user api, that lives in user_api.py module.
The fs provides four main operations: [create], [read], [write] and [mount]
The three first ones can only be used if mount has been called.
Once mount has been called there are three possible commands as follows:
- create filename
- read filename
- write filename data*

*Everything after filename is interpreted as data

There are two simple diagrams in uml package to ilustrate what was described above.


