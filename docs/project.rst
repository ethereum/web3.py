Project
-------

.. contents:: :local:

Introduction
^^^^^^^^^^^^

The ``populus.project.Project`` API is the common entry point to all aspects of
your populus project.


Basic Usage
^^^^^^^^^^^

``Project(config_file_paths=None)``

When instantaited with no arguments, the project will load any ``populus.ini``
file found in the current working directory and the current user's ``$HOME``
directory.

If there are specific configuration files that you would like loaded then you
can do so by passing them in as an array to the constructor.

.. code-block::

    from populus.project import Project
    # loads local `populus.ini` and `$HOME/populus.ini` if present.
    project = Project()

    # loads only the specified paths.
    other_project = Project(['/path/to/other/populus.ini'])
    other_project = Project([
        '/path/to/other/populus.ini',
        '/another/path/config.ini',
    ])

Configuration files are loaded in reverse order meaning that configuration
values set in the first files will supercede files later in the list.


Loading, Reloading, and Writing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``Project.primary_config_file_path``

    The path that configuration will be written to by default when
    ``Project.write_config()`` is called.  This defaults to a file named
    ``populus.ini`` in ``Project.project_dir``.


* ``Project.load_config(config_file_paths=None)``

    Loads the configuration files denoted by ``config_file_paths``.  If no
    paths are given, defaults to loading the local ``populus.ini`` and
    ``$HOME/populus.ini`` files.  This operation is destructive and will
    override any configuration changes that have been made.

* ``Project.write_config(destination_path=None)``

    Writes the current project configuration to the given ``destination_path``.
    If no desitnation path is given, defaults to
    ``Project.primary_config_file_path``.

* ``Project.reload_config()``

    Reloads the configuration files.  This operation is destructive and will
    override any configuration changes that have been made.


Filesystem Path Properties and Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Populus exposes properties and methods to access the the various filesystem
dictories and paths that populus uses.


* ``Project.project_dir``:

    The path that populus will treat as the root of your
    project.  This defaults to the current working directory.  It can be
    overridden in your ``populus.ini`` under the ``[populus]`` section with the
    option ``project_dir``.


* ``Project.contracts_dir``:

    The path under which populus will search for contracts to compile.


* ``Project.build_dir``:

    The path that populus will place it's build artifacts from compilation.


* ``Project.compiled_contracts_file_path``:

    The path that the JSON build artifact will be written to.


* ``Project.compile_project_contracts``:

    The parsed JSON output loaded from the
    ``Project.compiled_contracts_file_path``.


* ``Project.get_chain(chain_name, *chain_args, *chain_kwargs)``:

    Returns the ``populus.chain.Chain`` instance associated with the geven
    ``chain_name``.  The ``chain_args`` and ``chain_kwargs`` are passed through
    to the constructor of the underlying ``populus.chain.Chain`` object.


* ``Project.blockchains_dir``

    The path that the files for local blockchains will be placed.


* ``Project.get_blockchain_data_dir(chain_name)``

    Return the data directory for the blockchain with the given name.

* ``Project.get_blockchain_chaindata_dir(chain_name)``

    Returns the chaindata directory for the blockchain with the given name.

* ``Project.get_blockchain_ipc_path(chain_name)``

    Returns the path to the ``geth.ipc`` socket for the blockchain with the given name.


* ``Project.migrations_dir``

    The path that the project migration files are located.

* ``Project.migration_files``

    A list of all of the file paths to the project migrations.

* ``Project.migrations``

    A list of all of the project migration classes loaded from the
    ``Project.migration_files``.  The classes are returned ordered according to
    their declaired dependencies.
