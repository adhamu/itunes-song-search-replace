# iTunes Song Name Replacer
Get rid of annoying strings in MP3 song names. Inspired by [Doug's Script for Search & Replace](https://dougscripts.com/itunes/scripts/ss.php?sp=searchreplacetagtext).

## Requirements
- iTunes ([need your library XML file](https://support.apple.com/en-us/HT201610))
- Python3

## Set up

```bash
pip3 install -r requirements.txt
```

## Example Usage

```bash
python3 index.py -i 'iTunes Music Library.xml' -s 'feat.' -r 'Featuring '
```

You will then be presented with a confirmation for each result:

```bash
/Users/Amit/iTunes/Nas/Hip Hop Is Dead/Hustlers feat.The Game.mp3
Replace "feat." with "Featuring " [y/n] ?
```

**Note:** If you don't want to be prompted for each result, add the `--noconfirm` flag.

## What Else
By default, the first time you load your library, it will be cached using Pickle. Useful if you have a large library. To disable this, add the `--nocache` flag when you execute the script.

## Options
| Option        | Description                   | Required?     |
| :---:         | :---:                         | :---:         |
| `-i`          | iTunes Library File           | Y             |
| `-s`          | Search term                   | Y             |
| `-r`          | Replace search term with      | Y             |
| `--nocache`   | Don't cache library results   | N             |
| `--noconfirm` | Don't prompt for changes      | N             |
