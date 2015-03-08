from time import sleep
from behave import *
import os


@given(u'I create a directory "{created_dir}" in "{source_dir}" directory')
def step_impl(context, created_dir, source_dir):
    source_dir = os.path.abspath(source_dir)
    directory = os.path.abspath(source_dir + os.sep + created_dir)
    assert True == os.path.isdir(source_dir)
    try:
        os.mkdir(directory)
        sleep(1)
        context.directory = directory
    except IOError as ioe:
        print(
            "Exception thrown by '{0}' while creating directory '{1}'"
            . format(
                ioe.__class__,
                directory
            )
        )
    except Exception as e:
        print(
            "Exception thrown by '{0}' while creating file '{1}'"
            . format(
                e.__class__,
                directory
            )
        )
    assert True == os.path.isdir(directory)


@then(u'directory "{created_dir}" should be copied in')
def step_impl(context, created_dir):
    for row in context.table:
        directory = os.path.abspath(row[0] + os.sep + created_dir)
        assert True == os.path.exists(directory)
        assert True == os.path.isdir(directory)
