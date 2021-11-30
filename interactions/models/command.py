from typing import List, Optional, Union

from ..api.models.channel import ChannelType
from ..api.models.misc import DictSerializerMixin
from ..enums import ApplicationCommandType, OptionType, PermissionType


class Choice(DictSerializerMixin):
    """
    A class object representing the choice of an option.

    .. note::
        ``value`` allows ``float`` as a passable value type,
        whereas it's supposed to be ``double``.

    :ivar str name: The name of the choice.
    :ivar Union[str, int, float] value: The returned value of the choice.
    """

    __slots__ = ("_json", "name", "value")
    _json: dict
    name: str
    value: Union[str, int, float]

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class Option(DictSerializerMixin):
    """
    A class object representing the option of an application command.

    .. note::
        ``options`` is only present for when a subcommand
        has been established.

    :ivar OptionType type: The type of option.
    :ivar str name: The name of the option.
    :ivar str description: The description of the option.
    :ivar bool focused: Whether the option is currently being autocompleted or not.
    :ivar bool required?: Whether the option has to be filled out.
    :ivar Optional[str] value?: The value that's currently typed out, if autocompleting.
    :ivar Optional[List[Choice]] choices?: The list of choices to select from.
    :ivar Optional[List[Option]] options?: The list of subcommand options included.
    :ivar Optional[List[ChannelType] channel_type?: Restrictive shown channel types, if given.
    """

    __slots__ = (
        "_json",
        "type",
        "name",
        "description",
        "focused",
        "required",
        "value",
        "choices",
        "options",
        "channel_type",
    )
    _json: dict
    type: OptionType
    name: str
    description: str
    focused: bool
    required: Optional[bool]
    value: Optional[str]
    choices: Optional[List[Choice]]
    options: Optional[list]
    channel_type: Optional[List[ChannelType]]

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class Permission(DictSerializerMixin):
    """
    A class object representing the permission of an application command.

    :ivar int id: The ID of the permission.
    :ivar PermissionType type: The type of permission.
    :ivar bool permission: The permission state. ``True`` for allow, ``False`` for disallow.
    """

    __slots__ = ("_json", "id", "type", "permission")
    _json: dict
    id: int
    type: PermissionType
    permission: bool

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class ApplicationCommand(DictSerializerMixin):
    """
    A class object representing all types of commands.

    :ivar int id: The ID of the application command.
    :ivar Union[int, ApplicationCommandType] type: The application command type.
    :ivar Optional[int] application_id?: The general application ID of the command itself.
    :ivar Optional[int] guild_id?: The guild ID of the application command.
    :ivar str name: The name of the application command.
    :ivar str description: The description of the application command.
    :ivar Optional[List[Option]] options?: The "options"/arguments of the application command.
    :ivar Optional[bool] default_permission?: The default permission accessibility state of the application command.
    :ivar int version: The Application Command version autoincrement identifier.
    """

    __slots__ = (
        "_json",
        "id",
        "type",
        "application_id",
        "guild_id",
        "name",
        "description",
        "options",
        "default_permission",
        "permissions",
        "version",
    )
    _json: dict
    id: int
    type: Union[int, ApplicationCommandType]
    application_id: Optional[int]
    guild_id: Optional[int]
    name: str
    description: str
    options: Optional[List[Option]]
    default_permission: Optional[bool]
    permissions: Optional[List[Permission]]
    version: int

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
