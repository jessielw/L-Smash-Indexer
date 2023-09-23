import vapoursynth as vs
from pathlib import Path
from lsmash_indexer.utils import exit_application


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
    ):
        if batch_staxrip:
            batch_temp_dir = Path(str(path_input.with_suffix("")) + "_temp")
            batch_temp_dir.mkdir(exist_ok=True)
            cache_file = Path(batch_temp_dir / "temp.lwi")
        else:
            cache_file = Path(path_input).with_suffix(".lwi")

        if cache_file.exists():
            if not overwrite:
                exit_application(f"Index already exists for {cache_file.name}")
            else:
                cache_file.unlink(missing_ok=True)
        self.index_job(path_input, cache_file)

    def index_job(self, path_input: Path, cache_path: Path):
        try:
            self.core.lsmas.LWLibavSource(
                source=str(path_input), cachefile=str(cache_path)
            )
        except vs.Error as e:
            print(e)
