import logging
from datetime import datetime

import click

from simplevideocutter import util
from simplevideocutter.cut import run_ffmpeg_cut_command

time_spec_formats = ['%H:%M:%S', '%H-%M-%S']


def add_logging_options(fnc):
    """
    Helper decorator to add all logging related options for subcommands.
    """
    fnc = click.option('--ignore-warnings', '-no-warn', 'log_level',
                       flag_value=logging.ERROR,
                       help='Ignore warning messages.')(fnc)
    fnc = click.option('--info', 'log_level', flag_value=logging.INFO,
                       help='Include informational messages.')(fnc)
    fnc = click.option('--debug', 'log_level', flag_value=logging.DEBUG,
                       help='Include all debugging messages.')(fnc)
    return fnc


def _sanitize_timestamp(ctx, param, value):
    for time_spec_format in time_spec_formats:
        try:
            return datetime.strptime(value, time_spec_format)
        except ValueError:
            pass
    raise click.BadParameter(f'{param} needs to be in HH:MM:SS format.')


@click.group()
def entry():
    pass


@entry.command()
@click.option('--source-vod', '-source', '-src',
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              required=True,
              help='The source VOD to be cut.')
@click.option('--destination-file', '-destination', '-dst',
              type=click.Path(exists=False, file_okay=True, dir_okay=False),
              # TODO: Default value? Increment from origin name?
              required=True,
              help='The destination output file.')
@click.option('--start-time', '-start',
              type=click.DateTime(formats=time_spec_formats),
              help='The starting time stamp of the cut in HH:MM:SS format.'
                   'This value has precedence over the --start-offset flag.')
@click.option('--start-offset', '-offset', '-so',
              type=int,
              help='The offset (in seconds) from the start of the source video'
                   ' for the cut. If --start-time is defined, this value is '
                   'ignored.')
@click.option('--end-time', '-end',
              type=click.DateTime(formats=time_spec_formats),
              help='The end time stamp of the cut in HH:MM:SS format. This '
                   'value has precedence over the --duration flag.')
@click.option('--duration', '-d',
              type=int,
              help='The duration (in seconds) of the cut. If --end-time is '
                   'defined, this value is ignored.')
@click.option('--allow-overwrite', '-force', '-f',
              is_flag=True,
              flag_value=True,
              help='If this flag is given, destination file(s) can be '
                   'overwritten.')
@add_logging_options
def single(source_vod, destination_file, start_time, start_offset, end_time,
           duration, allow_overwrite, log_level):
    if not start_time and not start_offset:
        raise click.BadParameter(
            f'Either one of --start-time or --start-offset must be specified.')
    if not end_time and not duration:
        raise click.BadParameter(
            f'Either one of --end-time or --duration must be specified.')
    log_level = log_level or logging.WARNING
    util.configure_logging(log_level=log_level)
    if start_time:  # Sets start_offset (regardless if specified)
        start_offset = util.datetime_to_seconds(start_time)
    if end_time:  # Sets duration (regardless if specified)
        duration = util.datetime_to_seconds(end_time) - start_offset
    run_ffmpeg_cut_command(input_file=source_vod,
                           output_file=destination_file,
                           start_offset_in_s=start_offset,
                           duration_in_s=duration,
                           force_write=allow_overwrite,
                           )


@entry.command()
@add_logging_options
def multi(log_level):
    click.echo('TODO: Implement multi cut using timestamps file '
               '(or multi options?)')


@entry.command(
    help='NOT IMPLEMENTED. '
         'Start Graphical User Interface (GUI) to define video cuts. This '
         'requires PySide2 to be installed. See the installation guide for '
         'details on this.'
)
@add_logging_options
def gui(log_level):
    click.echo('TODO: Start GUI')
