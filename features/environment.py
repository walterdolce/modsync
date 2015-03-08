import shutil
import os
import sys


sys.dont_write_bytecode = True


def do_cleanup(context):
    if hasattr(context, 'directories') and context.directories:
        for directory in context.directories:
            if os.path.exists(directory):
                shutil.rmtree(directory)
    if hasattr(context, 'file') and os.path.exists(context.file):
        os.remove(context.file)
    if hasattr(context, 'background_modsync') \
            and context.background_modsync.isAlive() \
            and context.feature.status == 'failed':
        context.background_modsync.join(1)


def after_scenario(context, feature):
    do_cleanup(context)