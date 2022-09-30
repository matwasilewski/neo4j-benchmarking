class BadLogFormatException(Exception):
    pass


class IntegrityError(Exception):
    pass


class InvalidChoiceError(Exception):
    pass


class CannotUpdateFieldException(Exception):
    pass


class UnrecognisedFieldException(Exception):
    pass


class InsufficientInformationException(Exception):
    pass


class Auth0Error(Exception):
    pass


class NoManualApprovalError(Exception):
    pass


class InvalidQueryException(Exception):
    pass


class EmptyGraphListException(Exception):
    pass


class InvalidBfsRunDetected(Exception):
    pass


class CyclicGraphException(Exception):
    pass


class InvalidParametersException(Exception):
    pass


class FlowCalculationError(Exception):
    pass


class NoPathsFoundException(Exception):
    pass


class BadOperatorException(Exception):
    pass
