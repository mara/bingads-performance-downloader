"""Command line interface for adwords downloader"""

import click
from bingads_downloader import downloader,config
from functools import partial


def config_option(config_function):
    """Helper decorator that turns an option function into a cli option"""

    return lambda function: \
        click.option('--' + config_function.__name__,
                     help=config_function.__doc__ + '. Example: "' + config_function() + '"') \
            (function)


def apply_options(kwargs):
    """Applies passed cli parameters to config.py"""
    for key, value in kwargs.items():
        if value: setattr(config, key, partial(lambda v: v, value))


@click.command()
@config_option(config.developer_token)
@config_option(config.oauth2_client_id)
@config_option(config.oauth2_client_secret)
def refresh_oauth2_token(**kwargs):
    """
    Creates a new OAuth2 token.
    When options are not specified, then the defaults from config.py are used.
    """
    apply_options(kwargs)
    downloader.refresh_oauth_token()


@click.command()
@config_option(config.developer_token)
@config_option(config.oauth2_client_id)
@config_option(config.oauth2_client_secret)
@config_option(config.oauth2_refresh_token)
@config_option(config.data_dir)
@config_option(config.first_date)
def download_data(**kwargs):
    """
    Downloads data.
    When options are not specified, then the defaults from config.py are used.
    """
    apply_options(kwargs)
    downloader.download_data()