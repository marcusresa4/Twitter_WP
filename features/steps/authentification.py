from behave import *

use_step_matcher("re")


@given("I login as user with Google")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I login as user with Google')


@given("Exists a user logged")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given Exists a user logged')