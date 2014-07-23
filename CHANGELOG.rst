Changelog
=========

v1.3
----

- Changed directory structure to make MDK a python package
- Dev scripts disable string caching - David Mudrak
- Added support for MariaDB
- ``phpunit`` accepts the parameter ``--filter`` - Andrew Nicols

v1.2
----

- New ``js`` command

v1.1
----

- Sub processes are killed when using CTRL + C
- Default alias ``theme`` to set a theme - Andrew Nicols
- ``config`` has a new sub command ``edit``

v1.0
----

- Dropped official support for Python 2.6
- Moving forward by using ``pip`` for external dependencies
- New command ``css`` for CSS related tasks
- New script to ``enrol`` users
- ``push`` and ``backport`` commands can upload patches to the tracker
- ``pull`` can be forced to check for patches rather than pull branches
- Command ``check`` was renamed ``doctor``
- ``doctor`` can check for dependencies
- Support for sourcemaps when compiling LESS - Andrew Nicols
- Exit with error code 1 when an exception is thrown
- ``run`` can pass arguments to scripts
- Faster clone of cache on first ``init``
- ``phpunit`` accepts a testcase as argument
- ``.noupgrade`` file can be used not to upgrade an instance
- ``behat`` can run tests by name - Andrew Nicols
- ``remove`` accepts ``-f`` as an argument - Andrew Nicols
- The script ``less`` is deprecated
- ``backport`` command resolves conflicts with CSS from LESS in theme_bootstrapbase

v0.5
----

- New command ``uninstall`` to uninstall an instance
- New command ``plugin`` to install plugins
- ``push`` and ``backport`` can specify the HEAD commit when updating the tracker
- Updating the tracker smartly guesses the HEAD commit
- ``behat`` can force the download of the latest Selenium
- New setting not to use the cache repositories as remote
- ``purge`` can manually purge cache without using the shipped CLI

v0.4.2
------

- Updating tracker issue uses short hashes
- ``create`` accepts a custom instance identifier
- More verbose ``dev`` script
- New script ``undev`` to revert the changes of the script ``dev``
- ``pull`` has an option to fetch only
- New script ``less`` to compile the less files from bootstrapbase
- ``run`` can execute shell scripts
- Auto complete for ``behat`` -f
- Auto complete for ``phpunit`` -u
- Shipping a bash script ``extra/goto_instance`` to jump to instances with auto complete

v0.4.1
------

- ``config`` can display objects (eg. ``mdk config show wording``)
- ``config`` output is ordered alphabetically
- ``info`` output is ordered alphabetically
- ``init`` does not show the default password between brackets
- ``init`` does not fail because of missing directories
- ``run`` was permanently failing
- ``tracker`` failed when an issue was unassigned

v0.4
----

- New command ``tracker`` to fetch information from the tracker
- ``alias`` support arguments for bash aliases
- ``alias`` can update aliases
- ``backport`` works locally
- ``backport`` can update tracker Git info
- ``behat`` can limit features to test
- ``behat`` can disable itself
- ``check`` can fix problems
- ``check`` checks remote URLs
- ``check`` checks $CFG->wwwroot
- ``check`` checks the branch checked out on integration instances
- ``create`` accepts multiple versions
- ``create`` accepts multiple suffixes
- ``phpunit`` can limit testing to one file
- ``pull`` can download patch from the tracker
- ``pull`` can checkout the remote branch
- ``push`` checks that the branch and MDL in commit message match
- ``rebase`` can update tracker Git info
- ``run`` can list the available scripts
- Cached repositories are mirrors
- Removed use of Bash script to launch commands
- Deprecated moodle-*.py files
- Instances can be installed on https
- Improved debugging


v0.3
----

- New command ``behat`` which is equivalent to ``phpunit``
- New command ``pull`` to fetch a patch from a tracker issue
- New script ``webservices`` to entirely enable the web services
- ``push`` now updates the Git information on the tracker issue (Thanks to Damyon Wiese)
- ``phpunit`` can also run the tests after initialising the environment
- ``update --update-cache`` can proceed with the updates after updating the cached remotes
- ``info`` can be used to edit settings ($CFG properties) in config.php
- ``init`` has been a bit simplified
- Basic support of shell commands in aliases
- The settings in config.json are read from different locations, any missing setting will be read from config-dist.json
- Bug fixes