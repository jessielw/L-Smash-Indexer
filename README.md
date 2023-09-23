# L-Smash-Indexer

A CLI to index media files with L-SMASH's LWLibavSource

## Basic Usage

```
usage: L-Smash-Indexer [-h] [-v] [-i INPUT [INPUT ...]] [-y] [-b]
                       [-l LSMASH_DLL]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        Input file or directory
  -y, --overwrite       Overwrites index if already exists
  -b, --batch-staxrip   Will loop provided input directory and batch index
                        the entire directory in the format StaxRip utilizes
                        (overrides --batch)
  -l LSMASH_DLL, --lsmash-dll LSMASH_DLL
                        Path to L-Smash library (dll)
```

## Supports 

Windows 8 and up

## Requirements

You will need the L-Smash library. You can obtain it here.
https://github.com/HomeOfAviSynthPlusEvolution/L-SMASH-Works

## Input Types

```
You can line up multiple inputs to be encoded with the same settings:
input.mkv input.mp4 etc...
If there is space in the name you'll likely want to wrap them in quotes

It also supports everything the python glob module supports. This allows you to filter or search recursively etc:

Will find all mkv's in that currently directory:
"directory/nested_path/*.mkv"

Will find all mkv's recursively:
"directory/nested_path/**/*.mkv"

```
