# simple-video-cutter

This package is used to cut a source video into (multiple) smaller videos.

It requires Python 3.8 or higher and ffmpeg (and optionally Qt / PySide2).

## Installation

This package is available as a package on PyPI:

```bash
pip install simplevideocutter
```

To include the optional GUI component with PySide2:

```bash
pip install simplevideocutter[gui]
```

Additionally, you will need ffmpeg available on your path. You can download it 
here: https://ffmpeg.org/download.html .

## Usage

The commandline is callable using `simplevideocut` or `svcut` for short.

```bash
svcut --help
```

You can add `--info` or `--debug` flags to your commands for additional output.

### Cutting a single video

This is done using the subcommand `single`. You can view the help for this with `svcut single --help`.

```
svcut single -src /path/to/sourecfile.mp4 -dst /path/to/mynewlycutvod.mp4 -start 01:11:22 -end 01:30:15
```

### Cutting multiple videos using a timestamps file

This is done using the subcommand `multi`. You can view the help for this with `svcut multi --help`.

In this mode, the following information for each cut is read from a separate file, the so-called "timestamp specification file".

#### Timestamp spec file format

The file format requires that each line corresponds to a single cut, and must be formatted as:

    start-time end-time destination-filename HH:MM:SS HH:MM:SS myexamplefile.mp4

For example:

    01:12:34  01:15:44  soghent2_wf_Dia(Peach)_Nibodax(Bayonetta).mp4

Lines starting with a `#` symbol are ignored.

#### Command format

```
svcut multi -src /path/to/sourecfile.mp4 -dst /path/to/mycutvodsdirectory/ --timestamps-file /path/to/mytimestamps.txt
```

### Cutting multiple videos using the graphical interface

NOTE: This is not implemented yet!

This is started using the subcommand `gui`: `svcut gui`.

This requires PySide2 to be installed, which is included in the optional component for gui installations. 
See the *Installation* section above.

## Contributing

Requests and pull requests are welcome.

## License

This package (and _only_ this package) is [MIT licensed](https://choosealicense.com/licenses/mit/).

Note that [ffmpeg is licensed differently](https://ffmpeg.org/legal.html).