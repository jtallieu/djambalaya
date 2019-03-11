
def gui_config(request):
    return dict(
        TITLE="Djambalaya",
        MINI_TITLE="<b>D</b>jam",
        SKIN="skin-blue",
        MAIN_NAV_STYLE="sidebar-mini",
        FAVICON="djam/design.ico",
        LEFT_NAV=_left_menu()
    )


def _left_menu():
    components = dict(
        name="Components",
        desc='Collection of UI elements and components.',
        icon_classes="fa fa-code",
        url="#",
        items=[
            dict(
                name="Preview Panes",
                icon_classes="fa fa-video-camera",
                url="/djamba/uicomponent/preview_panes"),
            dict(
                name="Live Background",
                icon_classes="fa fa-barcode",
                url="/djamba/uicomponent/stats_as_background"),
            dict(
                name="Timeline",
                icon_classes="fa fa-sort-amount-desc",
                url="/djamba/uicomponent/timeline"),
        ]) 

    pages = dict(
        name="Pages",
        icon_classes="fa fa-clone",
        desc=("Static pages that demonstrate UI component layout.  The pages "
              "in this section have no backend support, so you might consider "
              "these a richer version of wire-frames.  For a collection of pages "
              "with backend support, checkout Workflows"),
        url="#",
        items=[
            dict(
                name="User Profile Page",
                icon_classes="fa fa-user",
                url="/djamba/solutions/user_profile"),
            dict(
                name="Device Manager",
                icon_classes="fa fa-wrench",
                url="/djamba/solutions/device_mgr"),
            dict(
                name="Layout Manager",
                icon_classes="fa fa-th-large",
                disabled=True,
                url="/djamba/solutions/layouts_mgr"),
            dict(
                name="User Permissions",
                icon_classes="fa fa-users",
                disabled=True,
                url="/djamba/solutions/user_permissions")
        ])

    workflows = dict(
        name="Workflows",
        icon_classes="fa fa-recycle",
        desc=("Generally, each item in this section will launch you into a specific workflow. "
              "A workflow is a collection of page transitions and functionality that provide a "
              "larger solution.  For example, editing a user or viewing a profile might start "
              "with finding a user and that entire experience and how it flows together."),
        url="#",
        items=[])

    apps = dict(
        name="Apps and Integrations",
        icon_classes="fa fa-gears",
        desc='Single page apps, Celery, Cassandra, Influx...',
        url="#",
        items=[
            dict(
                name="EEN Amin v2",
                icon_classes="fa fa-asterisk",
                disabled=True,
                url="/eenadmin"),
            dict(
                name="EEN VMS v2",
                icon_classes="fa fa-asterisk",
                disabled=True,
                url="/videobank"),
            dict(
                name="Proctor",
                icon_classes="fa fa-heartbeat",
                disabled=True,
                url="/proctor"),
            dict(
                name="CMS System",
                icon_classes="fa fa-th-large",
                disabled=True,
                url="/CMS"),
            dict(
                name="File Manager",
                icon_classes="fa  fa-folder-open",
                disabled=True,
                url="/file_mgr"),
            dict(
                name="Celery Worker Monitor",
                icon_classes="fa fa-pagelines",
                disabled=True,
                url="/flower_remake"),
        ])

    dashboards = dict(
        name="Dashboards",
        icon_classes="ion ion-stats-bars",
        desc='Graphs and charts',
        url="#",
        items=[
            dict(
                name="Bridge Health and Settings",
                icon_classes="fa fa-wrench",
                disabled=True,
                url="/djamba/solutions/device_mgr"),
            dict(
                name="Influx Demo",
                icon_classes="fa fa-th-large",
                disabled=True,
                url="/djamba/solutions/layouts_mgr"),
            dict(
                name="Using D3",
                icon_classes="fa fa-users",
                disabled=True,
                url="/djamba/solutions/user_permissions")
        ])
    return [components, pages, workflows, dashboards, apps]
