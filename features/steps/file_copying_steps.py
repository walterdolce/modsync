from time import sleep
from behave import *
from modsync.modsync import Modsync
import os
import threading


@given(u'there is a directory')
def step_impl(context):
    context.directories = []
    for row in context.table:
        directory_name = row[0]
        try:
            os.mkdir(directory_name)
            context.directories.append(directory_name)
        except OSError as ose:
            print("Exception thrown by {0} while creating directory {1}".format(ose.__class__, directory_name))
        except Exception as e:
            print("Exception thrown by {0} while creating directory {1}".format(e.__class__, directory_name))

    for directory_name in context.directories:
        assert True == os.path.exists(directory_name)


@given(u'I specify "{source_dir}" as the source directory')
def step_impl(context, source_dir):
    context.modsync = Modsync()
    context.modsync.setSource(source=source_dir)


@given(u'I specify the target directories')
def step_impl(context):
    for row in context.table:
        context.modsync.setTarget(row[0])


@given(u'I run modsync')
def step_impl(context):
    context.background_modsync = threading.Thread(target=context.modsync.run)
    context.background_modsync.daemon = True
    context.background_modsync.start()

@given(u'I create a file "{created_file}" in "{source_dir}" directory')
def step_impl(context, created_file, source_dir):
    assert True == os.path.isdir(source_dir)
    file = source_dir + os.sep + created_file
    try:
        f = open(file, 'a')
        f.close()
        sleep(1)
        context.file = created_file
    except IOError as ioe:
        print("Exception thrown by {0} while creating file {1}".format(ioe.__class__, file))
    except Exception as e:
        print("Exception thrown by {0} while creating file {1}".format(e.__class__, file))
    assert True == os.path.isfile(file)


@then(u'file "{created_file}" should be copied in')
def step_impl(context, created_file):
    for row in context.table:
        file = row[0] + os.sep + created_file
        assert True == os.path.exists(file)
        assert True == os.path.isfile(file)
