# iTunes Song Name Replacer
Get rid of annoying strings in MP3s song names. Inspired by [Doug's Script for Search & Replace](https://dougscripts.com/itunes/scripts/ss.php?sp=searchreplacetagtext).

## Requirements
- iTunes (need your library file)
- Python3

## Example Usage

```bash
python3 index.py -i 'iTunes Music Library.xml' -s 'feat.' -r 'Featuring '
```

You will then be presented with a confirmation for each result:

```bash
/Users/Amit/iTunes/Nas/Hustlers feat.The Game.mp3
Replace " feat." with "Featuring " [y/n] ?
```

## What Else
By default, the first time you load your library, it will be cached using Pickle. Useful if you have a large library. To disable this, add the `--nocache` flag when you execute the script.

## FYI
[If you don't see an .xml library file in ~/Music/iTunes, you probably started using iTunes after version 12.2, and have never enabled sharing between iTunes and other apps. To generate one, go to iTunes Preferences | Advanced and select "Share iTunes Library XML with other applications." (Apple docs)](https://github.com/liamks/libpytunes#libpytunes).
