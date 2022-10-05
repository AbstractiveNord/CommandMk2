Schema
======

Schema is a command with arguments mask, without first service char.

.. code-block:: python

	start { deep_link }
	ban { period } { reason }
	stats

You can pass to filter multiple schemas, using comma

.. code-block:: python

	CommandMk2('ban { period } { reason }', 'block { period } { reason }')

Prefix should be set using special field, don't put prefix into schema

.. code-block:: python

	CommandMk2('ban { period } { reason }', prefix='/!|')

In this examlpe, any char from string will be used as prefix for check.
