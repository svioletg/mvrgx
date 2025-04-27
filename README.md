# mvrgx

> **M**o**V**e with **R**e**G**e**X**

A tool with a terrible name that aids in bulk-renaming via regex and specialized output patterns. Matches files based on an input regular expression and either prints the list out if no output pattern is provided, or renames all matched files according to the given output pattern. `mvrgx` uses Python's standard [`re`](https://docs.python.org/3.12/library/re.html) module for regex parsing.

## Usage

Install `mvrgx` with pip:

```bash
pip install git+https://github.com/svioletg/python-mvrgx
```

This will install the `mvrgx` and `mvr` commands, which are identical. Basic usage could look something like this:

```bash
# Match all files starting with "2025-04-XX", and rename them to "April XX, 2025 - " followed by the rest of the filename.
mvrgx '2025-04-(\d\d) (.+)' -o 'April \0, 2025 - \1'
```

```bash
# Add creation date to the beginning of all files in this directory, in YYYY-MM-DD format
mvrgx '(.*)' -o '\m:f{ctime:t%Y-%m-%d} \0'
```

```bash
# Replace all MP3 file names with the track number and title stored in their metadata
mvrgx '*(\.mp3$)' -o '\m:a{trackno}-\m:a{title}.\m:f{suffix}'
```

Regular expressions are expected for input patterns, while output patterns use a combination of plain text and special backslash-prefixed keys for inserting match groups (`\1`, `\2`, `\3`) or file metadata (`\m:f{suffix}`, `\m:a{trackno}`).

## Usage: Capture groups

Regex capture groups are numbered by their order of appearance, starting at 1. In the expression `((\d+) - (.+)\.(.+)$)`, there are 4 total groups. The first group (`\1`) is the set of parenthesis that surround the entire expression, capturing the full text. The second (`\2`) captures one or more digits, the third (`\3`) captures one or more of any character, the fourth and final (`\4`) group captures the string following the final dot in the text.

To be more explicit, if this expression were matched against the string `04 - Libet's delay.mp3`, the groups would be as such:

|Group|Content|
|-|-|
|`\1`|`04 - Libet's delay.mp3`|
|`\2`|`04`|
|`\3`|`Libet's delay`|
|`\4`|`mp3`|

Also available for use, are **metadata** keys. They are used with the syntax `\m:X{Y:Z}`, where `X` is the metadata category/mode, `Y` is the key, and `Z` is an **optional** formatting specifier; if omitting the latter, the final colon is not needed. Some examples are `\m:f{suffix}`, `\m:a{trackno:z2}`, and `\m:f{stem}`.

<details>
<summary>`f` - general file metadata</summary>

|Key|Description|Example|
|-|-|-|
|`name`|Final component of the path, including suffix; i.e. the original filename, minus any directories.|`04 - Libet's delay.mp3`|
|`stem`|Final component of the path, excluding suffix.|`04 - Libet's delay`|
|`suffix`|Final suffix of the path, if one exists, minus the leading dot.|`mp3`|
|`bytes`|Size of the file in bytes.|`3487502`|
|`kb`|`bytes` divided by 1000, rounded to a precision of 4.|`3487.502`|
|`mb`|`mb` divided by 1000, rounded to a precision of 4.|`3.4875`|
|`gb`|`gb` divided by 1000, rounded to a precision of 4.|`0.0035`|
|`ctime`|Unix timestamp of when this file was created.|`1745221044.297786`|
|`atime`|Unix timestamp of when this file was last accessed.|`1745352016.2834144`|
|`mtime`|Unix timestamp of when this file was last modified.|`1410927766.0`|

</details>

<details>
<summary>`a` - audio file metadata (supports MP3, FLAC)</summary>

If any of metadata below is missing from the file, an empty string is returned.

|Key|Description|Example|
|-|-|-|
|`title`|Track title.|`Libet's delay`|
|`artist`|Track artist.|`The Caretaker`|
|`album`|Album this track is from.|`An empty bliss beyond this World`|
|`albumartist`|Album artist.|`The Caretaker`|
|`date`|Release date for this track. Can vary, but is typically the release year alone.|`2011`|
|`trackno`|Track number.|`4`|

</details>
