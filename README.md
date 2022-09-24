# simple-video-cutter

This package is used to cut a source video into (multiple) smaller videos.

It requires Python 3.7 or higher and ffmpeg (and optionally Qt / PySide2).

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
svc --help
```

### Cutting a single video

TODO: command to cut a single one

### Cutting multiple videos using a timestamps file

TODO: example here

### Cutting multiple videos using the graphical interface

Not implemented yet!

## Contributing

Requests and pull requests are welcome.

## License

This package (and _only_ this package) is [MIT licensed](https://choosealicense.com/licenses/mit/).

Note that [ffmpeg is licensed differently](https://ffmpeg.org/legal.html).