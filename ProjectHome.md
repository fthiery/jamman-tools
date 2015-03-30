# Description #
The [JamMan](http://en.wikipedia.org/wiki/DigiTech_JamMan) is a looper pedal product which can be used to produce loops and samples.

![http://4.bp.blogspot.com/_IJ0ZFDESQKs/SV1eHLDEXiI/AAAAAAAAAVw/3Y4-e9SPrxk/s400/JamMan_Alt.jpg](http://4.bp.blogspot.com/_IJ0ZFDESQKs/SV1eHLDEXiI/AAAAAAAAAVw/3Y4-e9SPrxk/s400/JamMan_Alt.jpg)

These python scripts are aimed at facilitating the rendering of the final song when stored on multiple steps/slots ("growing layers"), compression, exporting, ...

They are tested on Linux only.

I used to do this with Audacity before but the copy-paste stuff is tedious.

# Usage #

## Project Folders ##

All of the following utilities require the samples to be located directly into a dedicated project folder, with the following structure:

```
/Directory/LOOP15/LOOP.WAV
/Directory/LOOP15/LOOP.XML
/Directory/LOOP16/LOOP.WAV
/Directory/LOOP16/LOOP.XML
...
```

In short:
  * create a new directory
  * copy-paste the loop folders related to one single song into it

## Current utilities ##

  * jamman\_extract: will process a fresh project directory
    * backups the original files into ./backup
    * renames the LOOPX/LOOP.WAV files to X.WAV in the same order as the folders

  * jamman\_sequence: lets define a sequence (e.g. "1 2 3 5 4 6 6 7") used for rendering (merging) the file. sequence is stored into a .jam file. By adding a ?, the samples will be played back (e.g. "1? 2? 3? 4?") for simulation

  * jamman\_render: merges the .wav files either sequentially or using the .jam sequence file if present. The resulting .wav file is then normalized

  * jamman\_convert: produces mp3 & flac format files in the ./encoded folder for uploading

  * jamman\_export: works recursively; retrieves all of the encoded files for publishing, using the project's folder name as filename

  * jamman\_clean: removes all rendering and temporary files

  * jamman\_all: works recursively; will trigger a re-rendering of all projects located in the sub directories

## Dependancies ##

Please see the [deps file](http://code.google.com/p/jamman-tools/source/browse/trunk/DEPS)