"""
Video cutting / processing module.
"""
import os
import subprocess
import logging

import typing
from collections import namedtuple
from datetime import datetime

_l = logging.getLogger(__name__)

def generate_cut_command(input_file: str,
                         output_file: str,
                         start_offset_in_s: int,
                         duration_in_s: int,
                         ) -> list:
    """
    TODO doc

    This generates the following ffmpeg command arguments:

        ffmpeg
          -i <input_file>
          -ss <start_offset>
          -t <duration_in_s>
          -codec copy
          <output_file>

    :param input_file:
    :param output_file:
    :param start_offset_in_s:
    :param duration_in_s:
    :return: List of arguments for the ffmpeg subprocess.
    """
    return [f'ffmpeg',
            f'-ss {start_offset_in_s}',
            f'-i {input_file}',
            f'-t {duration_in_s}',
            f'-codec copy',
            f'{output_file}',
            ]


def run_ffmpeg_cut_command(input_file: str,
                           output_file: str,
                           start_offset_in_s: int,
                           duration_in_s: int,
                           ):
    """
    TODO doc
    """
    cmd_args = generate_cut_command(input_file=input_file,
                                    output_file=output_file,
                                    start_offset_in_s=start_offset_in_s,
                                    duration_in_s=duration_in_s)
    try:
        proc = subprocess.run(cmd_args)
        return proc.returncode
    except subprocess.CalledProcessError as exc:
        # TODO: Custom exception here?
        raise exc


CutSpec = namedtuple('CutSpec', ('start_offset', 'duration', 'file_name',))


def extract_cut_specs(timestamps_file) -> typing.Iterable[CutSpec]:
    with open(timestamps_file, 'rt') as _f:
        data = _f.readlines()
    data = [_line for _line in data if not _line.startswith('#')]  # filter out comments
    specs = (_parse_line(line, idx) for idx, line in enumerate(data, start=1))
    return [_ for _ in specs if _]


def _parse_line(line, idx):
    line = line.strip()
    if line.startswith('#'):
        return  # Ignore lines starting with #
    args = line.split()
    if len(args) != 3:
        raise ValueError(f'Incorrect number of arguments. Note that spaces in filenames are '
                         f'not allowed! Line that cause the error: {line}')
    start_time = args[0]
    end_time = args[1]
    file_name = f'{idx}_{args[2]}'
    start_time = datetime.strptime(start_time, '%H:%M:%S')
    start_offset = start_time.hour * 60 * 60 + start_time.minute * 60 + start_time.second
    end_time = datetime.strptime(end_time, '%H:%M:%S')
    end_offset = end_time.hour * 60 * 60 + end_time.minute * 60 + end_time.second
    duration = end_offset - start_offset
    return CutSpec(start_offset=start_offset, duration=duration, file_name=file_name)


# def cut_vod(source, timestamps_file, destination_dir):
#     source = os.path.abspath(source)
#     cut_specs = extract_cut_specs(timestamps_file)
#     source_extension = os.path.splitext(source)[1]
#     print(f'Cutting VODs from source file: {os.path.abspath(source)}')
#     for cut_spec in cut_specs:
#         destination = os.path.join(destination_dir, cut_spec.file_name)
#         if not destination.endswith(source_extension):
#             # Destination file path does not specify an extension.
#             destination = destination + source_extension
#         if os.path.exists(destination):
#             print(f'Skipping "{destination}", already exists.')
#             continue
#         run_ffmpeg_cut_command(input_file=source,
#                                output_file=destination,
#                                start_offset_in_s=cut_spec.start_offset,
#                                duration_in_s=cut_spec.duration)
