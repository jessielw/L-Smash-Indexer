import vapoursynth as vs
from os import PathLike
from pathlib import Path
from typing import Optional


class LSmashIndexer:
    def __init__(self, lsmash_path: Path):
        self.loaded_plugin = False
        self.core = vs.core
        self.core.std.LoadPlugin(str(lsmash_path))

    def process_file(
        self,
        path_input: Path,
        overwrite: bool,
        batch_staxrip: bool,
        output_path: Optional[PathLike[str]],
    ):
        skip = False
        if batch_staxrip:
            batch_temp_dir = Path(str(path_input.with_suffix("")) + "_temp")
            batch_temp_dir.mkdir(exist_ok=True)
            cache_file = Path(batch_temp_dir / "temp.lwi")
        else:
            if output_path:
                cache_file = Path(output_path) / Path(f"{path_input.stem}.lwi")
            else:
                cache_file = Path(path_input).with_suffix(".lwi")

        # ensure output directory exists
        cache_file.parent.mkdir(exist_ok=True, parents=True)

        if cache_file.exists():
            if not overwrite:
                print(f"Index already exists for {path_input.name}, skipping...")
                skip = True
            else:
                cache_file.unlink(missing_ok=True)

        if not skip:
            self.index_job(path_input, cache_file)

    def index_job(self, path_input: Path, cache_path: Path):
        try:
            print(f"Creating index for {path_input.name}")
            self.core.lsmas.LWLibavSource(
                source=str(path_input), cachefile=str(cache_path)
            )
        except vs.Error as e:
            print(e)
