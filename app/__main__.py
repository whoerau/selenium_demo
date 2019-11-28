import click
import time
from .seleniumcli import *


@click.command()
@click.option(
    "--gateway-password",
    default="123",
    type=click.STRING,
    help="password which is required before processing requests",
)
@click.option(
    "--standalone-chrome",
    default="http://selenium:4444/wd/hub",
    type=click.STRING,
    help="standalone-chrome which is required before processing requests",
)
def main(
        gateway_password: str,
        standalone_chrome: str,

):
    t = GatewayReboot()
    t.setup_method(gateway_password, standalone_chrome)
    t.reboot()
    time.sleep(3)
    t.teardown_method()


if __name__ == '__main__':
    main(auto_envvar_prefix="SD")
