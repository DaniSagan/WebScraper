from abc import ABC, abstractmethod
from typing import Callable, TypeVar, Generic

T = TypeVar("T")


class PresenterBase(Generic[T], ABC):

    @abstractmethod
    def present(self, obj: T) -> str:
        raise NotImplementedError()
