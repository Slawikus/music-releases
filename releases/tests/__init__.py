from .base_client_test import BaseClientTest
from .get_view_context import get_view_context
from .update_marketing_infos_test import UpdateMarketingInfosTest
from .all_releases_view_test import AllReleasesViewTest
from .create_release_test import CreateReleaseTest
from .edit_release_view_test import EditReleaseViewTest
from .my_releases_view_test import MyReleasesViewTest
from .recently_submitted_view_test import RecentlySubmittedViewTest
from .upcoming_view_test import UpcomingViewTest

__all__ = [
	BaseClientTest,
	get_view_context,
	UpdateMarketingInfosTest,
	AllReleasesViewTest,
	CreateReleaseTest,
	EditReleaseViewTest,
	MyReleasesViewTest,
	RecentlySubmittedViewTest,
	UpcomingViewTest
]