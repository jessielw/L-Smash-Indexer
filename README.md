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
                        Input file path(s) pattern using glob pattern matching
  -y, --overwrite       Overwrites index if already exists
  -b, --batch-staxrip   Will output index cache file in a temp directory in the format StaxRip utilizes
  -l LSMASH_DLL, --lsmash-dll LSMASH_DLL
                        Path to L-Smash library (dll)
```

## Supports

Windows 8 and up

## Requirements

You will need the (x64) L-Smash library. You can obtain it here.
https://github.com/HomeOfAviSynthPlusEvolution/L-SMASH-Works

## Input Types

```
You can line up multiple inputs to be encoded with the same settings:
input.mkv input.mp4 etc...
If there is space in the name you'll likely want to wrap them in quotes

It also supports everything the python glob module supports. This allows you to filter or search recursively etc:

Will find all mkv's currently in the defined directory:
"directory/nested_path/*.mkv"

Will find all mkv's recursively in the defined directory:
"directory/nested_path/**/*.mkv"

```
