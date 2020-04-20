# RunElsewhere

This package provides an IPython extension that redefines the `%run` line magic to transparently change the path directory of the file to execute.

## Quickstart

After install, in any IPython-based console:
```python
%load_ext runelsewhere
Base path on the client: /client/path
Base path on the server: /server/path
...
%run /client/path/test.py  # will translate to /server/path/test.py
%run test.py  # Doesn't do anything, so runs /current/working/dir/test.py
%toggle_run  # Puts back the old run command
%toggle_run  # And now to our redefined %run
```

## Why?

This is useful where using a distant kernel in Spyder, for example. Spyder is able to connect to distant kernels, but does not transfer files when running them (ex: by pressing "F5"). Instead, it simply calls the `%run` magic with the filename. Provided that you mount the server code directory on the client (or vice-versa), this utility redefines the `%run` magic so that Spyder launches the good file. One could also achieve the same effect by mounting both server and client code directories to the same path on each machine, but this is not always possible.

## How to use

The best use case for this is through Spyder + remote directory + remote kernel. This package should be installed on the server.

On the remote machine: 

1) Start a ipython kernel. I usually do : `jupyter console`.
2) Get the connection info (with `%connect_info`) and save to file on the *client*.

On the client:

3) Mount the server directory containing the python code to edit and debug to some path on the client.
4) In spyder, in the console tab, connect to a remote kernel. You'll provide the file created in 2 + your ssh credentials.
5) In the console, `%load_ext runelsewhere` and provide the **absolute** paths to the code directory on both server and client.

From that point on, the `%run` command is being wrapped so that a client-side path is translated to a server-side one. Basic Spyder commands, like "run (F5)" and "debug", use `%run` directly and will now work for codes inside the client side code directory.