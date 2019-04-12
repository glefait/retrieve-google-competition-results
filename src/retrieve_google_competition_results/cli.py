import sys
import click
import logging
import os

from retrieve_google_competition_results.utils import get_write_results

logger = logging.getLogger(__name__)


@click.command()
@click.option('--debug', is_flag=True, help="Turn on debug logging")
@click.option('--year', help="Competition Year")
@click.option('--round', help="Round")
@click.option('--start', type=int, help="results from")
@click.option('--nb', type=int, help="nb results: 0 = all")
@click.option('--output_dir', default="data/", help="destination dir")
def main(debug: bool, year: str, round: str, start: int, nb: int,
         output_dir: str):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=level)

    get_write_results(year, round, start, nb, output_dir)

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
