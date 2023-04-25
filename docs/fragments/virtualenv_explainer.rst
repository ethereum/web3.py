**Optional:** Often, the best way to guarantee a clean Python 3 environment is with
`virtualenv <https://virtualenv.pypa.io/en/stable/>`_. If we don't have ``virtualenv`` installed
already, we first need to install it via pip.

.. code:: sh

  pip install virtualenv

Then, we can initialize a new virtual environment ``venv``, like:

.. code:: sh

  virtualenv -p python3 venv

This creates a new directory ``venv`` where packages are installed isolated from any other global
packages.

To activate the virtual directory we have to *source* it

.. code:: sh

  . venv/bin/activate

  # and when leaving this context:
  deactivate
