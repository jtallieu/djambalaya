import logging

log = logging.getLogger(__name__)


def gui_config(request):
    if request.path_info.startswith('/videobank'):
        return dict(
            TITLE="Videobank",
            MINI_TITLE="<b>VMS</b>",
            SKIN="skin-black",
            MAIN_NAV_STYLE="sidebar-mini",
            FAVICON="djam/design.ico",
            LEFT_NAV=[]
        )
    else:
        return []
