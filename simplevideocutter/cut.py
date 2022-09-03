"""
Video cutting / processing module.
"""
import subprocess


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
