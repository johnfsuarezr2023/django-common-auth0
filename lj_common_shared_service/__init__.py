VERSION = (0, 1, 0, "dev", 0)

__title__ = "django-common-shared-service"
__version_info__ = VERSION
__version__ = ".".join(map(str, VERSION[:3])) + (
    "-{}{}".format(VERSION[3], VERSION[4] or "") if VERSION[3] != "final" else ""
)
