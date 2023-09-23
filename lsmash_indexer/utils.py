import sys
import glob
from pathlib import Path


def exit_application(msg: str, exit_code: int = 0):
    """A clean way to exit the program without raising traceback errors

    Args:
        msg (str): Success or Error message you'd like to display in the console
        exit_code (int): Can either be 0 (success) or 1 (fail)
    """
    if exit_code not in {0, 1}:
        raise ValueError("exit_code must only be '0' or '1' (int)")

    if exit_code == 0:
        output = sys.stdout
    elif exit_code == 1:
        output = sys.stderr

    print(msg, file=output)
    sys.exit(exit_code)


class FileParser:
    @staticmethod
    def parse_input_s(args_list: list):
        """
        Parse the input arguments and return a list of Path objects representing the input files.

        Args:
            args_list (list): List of input arguments.

        Returns:
            list: List of Path objects representing the input files.

        Raises:
            FileNotFoundError: If an input path is not a valid file path.
        """
        input_s = []
        for arg_input in args_list:
            # non recursive
            if "*" in arg_input:
                input_s.extend(
                    Path(p) for p in glob.glob(arg_input) if Path(p).is_file()
                )

            # recursive search
            elif "**" in arg_input:
                input_s.extend(
                    Path(p)
                    for p in glob.glob(arg_input, recursive=True)
                    if Path(p).is_file()
                )

            # single file path
            elif (
                Path(arg_input).exists()
                and Path(arg_input).is_file()
                and arg_input.strip() != ""
            ):
                input_s.append(Path(arg_input))
            else:
                raise FileNotFoundError(f"{arg_input} is not a valid input path.")

        return input_s
