# mycic-tools

A tool for students at cic univ:

- Mark attendance in mycic
- Extract course schedule to csv, png (desktop only)

These tools adhere to the privacy and policy regulations, preventing attendance after the designated time

## installation

Mobile device

- Install [Termux](https://github.com/termux/termux-app/releases)
- Run :

```
cd ~ && git clone https://github.com/rizmulya/mycic-tools.git && cd mycic-tools && pip install -r requirements.txt && mv .env.example .env && nano .env && cd cic_portal && nano absensi.py && cd .. && python main.py
```

fill in your username&password, save & exit, exit.

## how to use

```console
$ python main.py


usage: main.py [-h] [-a] [-m] [-j]

Mycic Tools

options:
  -h, --help    show this help message and exit
  -a, --absen   Absen mycic
  -m, --manual  Absen manual [-a -m]
  -j, --jadwal  Extract jadwal ke png & csv (uncomment extractor.py & exporter.py and run pip install pillow)
```

## update command

```
cd ~ && mv mycic-tools/.env ~ && rm -rf mycic-tools && git clone https://github.com/rizmulya/mycic-tools.git && cd mycic-tools && pip install -r requirements.txt && mv ~/.env . && cd cic_portal && nano absensi.py && cd .. && python main.py
```

exit and your code will be updated.
