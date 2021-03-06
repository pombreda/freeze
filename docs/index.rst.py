import freeze

tmpl = """
.. freeze documentation master file, created by
   sphinx-quickstart on Fri Mar 22 02:27:13 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Freeze - hash / sort / compare / diff anything
==============================================

.. autosummary::

   %s

.. automodule:: freeze
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

print(tmpl % "\n   freeze.".join([""] + freeze.__all__))
