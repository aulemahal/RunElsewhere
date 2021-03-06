from IPython.core.magic import Magics
from IPython.core.magic import magics_class
from IPython.core.magic import line_magic
import IPython.utils.path as ipypath
from pathlib import Path, PureWindowsPath, PurePosixPath


@magics_class
class RunElsewhere(Magics):
    def __init__(self, shell, client_side, server_side):
        super().__init__(shell)
        self.Client_Path = Path
        self.client_path = PurePosixPath(client_side)
        if not self.client_path.is_absolute():
            self.client_path = PureWindowsPath(client_side)
            if not self.client_path.is_absolute():
                raise ValueError('Provided client path must be absolute.')
            self.Client_Path = PureWindowsPath

        self.server_path = Path(server_side)
        if not self.server_path.is_absolute():
            raise ValueError('Provided server path must be absolute.')

        self.base_run = shell.find_line_magic('run')
        self.active = True

    def get_py_filename(self, name, force_win32=None):
        path = self.Client_Path(name)
        if self.active and path.is_absolute():
            try:
                path = path.relative_to(self.client_path)
            except ValueError:
                path = path.name
            path = self.server_path / path
        return ipypath.get_py_filename(str(path), force_win32=force_win32)

    @line_magic
    def toggle_run(self, value=None):
        self.active = bool(value or not self.active)

    @line_magic
    def run(self, line):
        return self.base_run(line, file_finder=self.get_py_filename)


def load_ipython_extension(ipython):
    client_side = input("\nBase path on the client: ")
    server_side = input("\nBase path on the server :")
    runelse = RunElsewhere(ipython, client_side, server_side)
    ipython.register_magics(runelse)
