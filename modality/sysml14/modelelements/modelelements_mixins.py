"""Mixins to be implemented by user."""
from pyecore.ecore import EDerivedCollection


class ConformMixin:
    """User defined mixin class for Conform."""

    def __init__(self, *, base_Generalization=None, **kwargs):
        super().__init__()


class DerivedMember(EDerivedCollection):
    pass


class ElementGroupMixin:
    """User defined mixin class for ElementGroup."""

    @property
    def criterion(self):
        raise NotImplementedError("Missing implementation for criterion")

    @property
    def size(self):
        raise NotImplementedError("Missing implementation for size")

    def __init__(
        self,
        *,
        base_Comment=None,
        criterion=None,
        member=None,
        name=None,
        orderedMemeber=None,
        size=None,
        **kwargs,
    ):
        super().__init__()

    def all_groups(self, e=None, result=None):

        raise NotImplementedError("operation all_groups(...) not yet implemented")

    def criterion(self, result=None):

        raise NotImplementedError("operation criterion(...) not yet implemented")

    def member(self, result=None):

        raise NotImplementedError("operation member(...) not yet implemented")

    def size(self, result=None):

        raise NotImplementedError("operation size(...) not yet implemented")


class ExposeMixin:
    """User defined mixin class for Expose."""

    def __init__(self, *, base_Dependency=None, **kwargs):
        super().__init__()


class ProblemMixin:
    """User defined mixin class for Problem."""

    def __init__(self, *, base_Comment=None, **kwargs):
        super().__init__()


class RationaleMixin:
    """User defined mixin class for Rationale."""

    def __init__(self, *, base_Comment=None, **kwargs):
        super().__init__()


class DerivedConcern(EDerivedCollection):
    pass


class StakeholderMixin:
    """User defined mixin class for Stakeholder."""

    def __init__(
        self, *, base_Classifier=None, concernList=None, concern=None, **kwargs
    ):
        super().__init__()


class DerivedStakeholder(EDerivedCollection):
    pass


class ViewMixin:
    """User defined mixin class for View."""

    @property
    def viewPoint(self):
        raise NotImplementedError("Missing implementation for viewPoint")

    def __init__(self, *, base_Class=None, stakeholder=None, viewPoint=None, **kwargs):
        super().__init__()


class DerivedConcern(EDerivedCollection):
    pass


class DerivedMethod(EDerivedCollection):
    pass


class ViewpointMixin:
    """User defined mixin class for Viewpoint."""

    def __init__(
        self,
        *,
        base_Class=None,
        concern=None,
        concernList=None,
        language=None,
        method=None,
        presentation=None,
        purpose=None,
        stakeholder=None,
        **kwargs,
    ):
        super().__init__()
