from pathlib import Path
from argparse import ArgumentParser
from lsmash_indexer import LSmashIndexer
from lsmash_indexer.utils import exit_application, FileParser

program_name = "L-Smash-Indexer"
__version__ = "0.2.0"


if __name__ == "__main__":
    parser = ArgumentParser(prog=program_name)
    parser.add_argument(
        "-v", "--version", action="version", version=f"{program_name} v{__version__}"
    )
    parser.add_argument(
        "-i",
        "--input",
        nargs="+",
        help="Input file path(s) pattern using glob pattern matching",
    )
    parser.add_argument("-o", "--output", type=str, help="Output directory")
    parser.add_argument(
        "-y",
        "--overwrite",
        action="store_true",
        help="Overwrites index if already exists",
    )
    parser.add_argument(
        "-b",
        "--batch-staxrip",
        action="store_true",
        help=(
            "Will output index cache file in a temp directory in the format StaxRip utilizes, this overrides '--output'"
        ),
    )
    parser.add_argument(
        "-l", "--lsmash-dll", type=str, help="Path to L-Smash library (dll)"
    )
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        exit_application("", 1)

    if not args.lsmash_dll:
        exit_application("Path to L-Smash library is required", 1)
    else:
        lsmash_library = Path(args.lsmash_dll)
        if not lsmash_library or not lsmash_library.is_file():
            exit_application("Path to L-Smash library does not appear to exist", 1)

    if not args.input:
        exit_application(
            "File or directory input is required (e.g. -i input.mkv/glob)",
            1,
        )

    if args.batch_staxrip and args.output:
        exit_application("Cannot define both '--output' and '--batch-staxrip'", 1)

    if args.output and not Path(args.output).is_dir():
        exit_application("'--output' should be a directory", 1)

    indexer = LSmashIndexer(lsmash_library)

    file_inputs = FileParser().parse_input_s(args.input)
    for file_input in file_inputs:
        indexer.process_file(
            file_input, args.overwrite, args.batch_staxrip, args.output
        )
