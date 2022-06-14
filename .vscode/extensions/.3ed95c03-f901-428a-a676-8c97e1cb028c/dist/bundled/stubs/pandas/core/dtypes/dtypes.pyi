from pandas._typing import Ordered as Ordered
from .base import ExtensionDtype as ExtensionDtype
from pandas._libs.tslibs import NaT as NaT, Period as Period, Timestamp as Timestamp #, timezones as timezones
from pandas.core.indexes.base import Index
from typing import Any, Optional, Sequence, Tuple, Type, Union

_str = str

def register_extension_dtype(cls: Type[ExtensionDtype]) -> Type[ExtensionDtype]: ...

class Registry:
    dtypes = ...
    def __init__(self) -> None: ...
    def register(self, dtype: Type[ExtensionDtype]) -> None: ...
    def find(self, dtype: Union[Type[ExtensionDtype], str]) -> Optional[Type[ExtensionDtype]]: ...

registry = ...

class PandasExtensionDtype(ExtensionDtype):
    type = ...
    kind = ...
    subdtype = ...
    str: Optional[_str] = ...
    num: int = ...
    shape: Tuple[int, ...] = ...
    itemsize: int = ...
    base = ...
    isbuiltin: int = ...
    isnative: int = ...
    def __hash__(self) -> int: ...
    @classmethod
    def reset_cache(cls) -> None: ...

class CategoricalDtypeType(type): ...

class CategoricalDtype(PandasExtensionDtype, ExtensionDtype):
    name: _str = ...
    type: Type[CategoricalDtypeType] = ...
    kind: _str = ...
    str: _str = ...
    base = ...
    def __init__(self, categories: Optional[Sequence[Any]]=..., ordered: Ordered=...) -> None: ...
    @classmethod
    def construct_from_string(cls, string: _str) -> CategoricalDtype: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    @classmethod
    def construct_array_type(cls): ...
    @staticmethod
    def validate_ordered(ordered: Ordered) -> None: ...
    @staticmethod
    def validate_categories(categories, fastpath: bool=...) : ...
    def update_dtype(self, dtype: Union[_str, CategoricalDtype]) -> CategoricalDtype: ...
    @property
    def categories(self) -> Index: ...
    @property
    def ordered(self) -> Ordered: ...

class DatetimeTZDtype(PandasExtensionDtype):
    type: Type[Timestamp] = ...
    kind: _str = ...
    str: _str = ...
    num: int = ...
    base = ...
    na_value = ...
    def __init__(self, unit: _str = ..., tz = ...) -> None: ...
    @property
    def unit(self): ...
    @property
    def tz(self): ...
    @classmethod
    def construct_array_type(cls): ...
    @classmethod
    def construct_from_string(cls, string: _str) : ...
    @property
    def name(self) -> _str: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...

class PeriodDtype(PandasExtensionDtype):
    type: Type[Period] = ...
    kind: _str = ...
    str: _str = ...
    base = ...
    num: int = ...
    def __new__(cls, freq = ...): ...
    @property
    def freq(self): ...
    @classmethod
    def construct_from_string(cls, string: _str): ...
    @property
    def name(self) -> _str: ...
    @property
    def na_value(self): ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    @classmethod
    def is_dtype(cls, dtype) -> bool: ...
    @classmethod
    def construct_array_type(cls): ...
    def __from_arrow__(self, array): ...

class IntervalDtype(PandasExtensionDtype):
    name: _str = ...
    kind: _str = ...
    str: _str = ...
    base = ...
    num: int = ...
    def __new__(cls, subtype = ...): ...
    @property
    def subtype(self): ...
    @classmethod
    def construct_array_type(cls): ...
    @classmethod
    def construct_from_string(cls, string: _str): ...
    @property
    def type(self): ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    @classmethod
    def is_dtype(cls, dtype) -> bool: ...
    def __from_arrow__(self, array): ...

