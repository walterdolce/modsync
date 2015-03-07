
from behave import *
from modsync.modsync import Modsync


@when(u'I invoke modsync with no parameters')
def step_impl(context):
    context.modsync = Modsync()
    context.run = context.modsync.run()

@then(u'it should pass')
def step_impl(context):
    assert context.run == 0
