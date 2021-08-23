""" To-Do! CLI

Usage:
    to_do run
    to_do (-h | --help)
    to_do (-v | --version)

Options:
    -h --help     Show this screen
    -v --version  Show version

"""
import to_do
import uvicorn

from docopt import docopt


def main():
    to_do_version = "{} {}".format(
    to_do.dist_name,
    to_do.__version__
    )

    args = docopt(__doc__, version=to_do_version)

    if args['run']:
        uvicorn.run("to_do.server:app",host='0.0.0.0', port=8000, reload=True)

