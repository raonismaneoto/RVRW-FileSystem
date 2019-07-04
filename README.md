# RVRFS-Prototype

## First of all, it's necessary to list some simplifications we've done to make it easier. As follows:

- There is only one directory (the root one).
- We don't differ the in-core inodes to the disk ones.
- Despite the block's size has been set to 4096B we consider them full if there is any data inside of it.
But the data can also be 4096 large.
- The disk of the filesystem is abstracted by file.
- In the superblock, the lists of free inodes and free blocks are never empty.

## Usage
There is a simple script responsible for start the fs. It's called start.sh.
To run the FS for the first time or to restart it, it's necessary to run the follow command: ./start.sh -r.
In the other cases ./start.sh is enough.

## Structure
Everything starts on the setup.py module. It is responsible for create our disk abstraction (the main file), once it is done the mkfs is called.
Mkfs 


