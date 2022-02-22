Discord Timestamp Generator Python extension for the [Albert Launcher](https://albertlauncher.github.io).

## Installation
If Node.js is installed:
- Run `npx degit https://github.com/esfox/albert-discord-timestamp discord-timestamp`
- Install `dateparser` with `pip install dateparser`
- Move the created `discord-timestamp` folder to the path of the Python extensions of Albert (which is most likely in `~/.local/share/albert/org.albert.extension.python`)
- Restart Albert

If Node.js is not installed:
- Clone this repository
- `cd` into the cloned repository then remove the `.git` directory
- Install `dateparser` with `pip install dateparser`
- Move the repository's folder to the path of Albert's Python extensions (see above)

## Usage
Type `dt` to trigger this extension in Albert.

## Screenshot
![screenshot](https://i.imgur.com/UmUn8SC.png)
