from datetime import datetime

import click

time_spec_formats = ['%H:%M:%S', '%H-%M-%S']


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
@click.option('--source-vod', '-source',
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              required=True,
              help='The source VOD to be cut.')
@click.option('--destination-file', '-destination',
              type=click.Path(exists=False, file_okay=True, dir_okay=False),
              # TODO: Default value? Increment from origin name?
              required=True,
              help='The destination output file.')
@click.option('--start-time', '-start',
              type=click.DateTime(formats=time_spec_formats),
              required=True,
              help='The starting time stamp of the cut in HH:MM:SS format.')
@click.option('--end-time', '-end',
              type=click.DateTime(formats=time_spec_formats),
              help='The end time stamp of the cut in HH:MM:SS format. This value'
                   ' has precedence over the --duration flag.')
@click.option('--duration', '-d',
              type=int,
              help='The duration (in seconds) of the cut. If --end-time is '
                   'defined, this value is ignored.')
@click.option('--allow-overwrite', '-force', '-f',
              is_flag=True,
              flag_value=True,
              help='If this flag is given, destination file(s) can be '
                   'overwritten.')
def single(source_vod, destination_file, start_time, end_time, duration,
           allow_overwrite):
    if not end_time and not duration:
        raise click.BadParameter(f'Either one of --end-time or --duration must '
                                 f'be specified.')
    click.echo('cut single')
    click.echo(source_vod)
    click.echo(destination_file)
    click.echo(start_time)
    click.echo(end_time)
    click.echo(duration)
    click.echo(allow_overwrite)


@entry.command()
def multi():
    click.echo('TODO: Implement multi cut using timestamps file '
               '(or multi options?)')


@entry.command(
    help='Start Graphical User Interface (GUI) to define video cuts. This '
         'requires PySide2 to be installed. See the installation guide for '
         'details on this.'
)
def gui():
    click.echo('TODO: Start GUI')
