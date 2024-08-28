from pathlib import Path
from subprocess import run
import os
import shutil
import sys


def build_app():
    # change directory to this files parent
    os.chdir(Path(Path(__file__).parent))

    # ensure we're in virtual env, if we are pip install requirements
    if sys.prefix == sys.base_prefix:
        raise Exception("You must activate your virtual environment first")
    else:
        run(["pip", "install", "-r", "requirements.txt"])

    # define pyinstaller output path
    pyinstaller_folder = Path(Path(__file__).parent / "pyinstaller_build")

    # delete old build folder if it exists
    shutil.rmtree(pyinstaller_folder, ignore_errors=True)

    # create folder for output
    pyinstaller_folder.mkdir(exist_ok=True)

    # define paths before changing directory
    tool_path = Path(Path.cwd() / "l-smash-indexer.py")
    icon_path = Path(Path.cwd() / "l-smash-image.ico")
    additional_hooks_path = Path(Path.cwd() / "hooks")
    site_packages = Path(Path.cwd() / ".venv" / "Lib" / "site-packages")
    vapoursynth_64 = site_packages / "vapoursynth64"
    vapoursynth_64_portable = site_packages / "portable.vs"

    # change directory so we output all of pyinstallers files in it's own folder
    os.chdir(pyinstaller_folder)

    # run pyinstaller command
    build_job = run(
        [
            "pyinstaller.exe",
            "--onefile",
            "--name",
            "L-Smash-Indexer",
            f"--icon={str(icon_path)}",
            "--add-data",
            f"{vapoursynth_64};vapoursynth64",
            "--add-data",
            f"{vapoursynth_64_portable};.",
            str(tool_path),
            f"--additional-hooks-dir={str(additional_hooks_path)}",
        ]
    )

    # ensure output of exe
    success = "Did not complete successfully"
    if (
        Path(Path("dist") / "l-smash-indexer.exe").is_file()
        and str(build_job.returncode) == "0"
    ):
        success = f'\nSuccess!\nPath to exe: {str(Path.cwd() / (Path(Path("dist") / "l-smash-indexer.exe")))}'

    # change directory back to original directory
    os.chdir(tool_path.parent)

    # return success message
    return success


if __name__ == "__main__":
    build = build_app()
    print(build)
