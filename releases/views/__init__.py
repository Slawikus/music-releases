from .submit_release_view import SubmitReleaseView
from .create_release_view import CreateReleaseView
from .all_release_view import AllReleaseView
from .create_wholesale_price_view import CreateWholesalePriceView
from .update_wholesale_and_trades_view import UpdateWholesaleAndTradesView
from .import_releases_view import ImportReleasesView
from .edit_release_view import EditReleaseView
from .recently_submitted_view import RecentlySubmittedView
from .my_releases_view import MyReleasesView
from .upcoming_releases_view import UpcomingReleasesView
from .update_marketing_infos_view import UpdateMarketingInfosView
from .delete_wholesale_price_view import DeleteWholesalePriceView
from .base_release import BaseRelease

__all__ = [
	BaseRelease,
	SubmitReleaseView,
	CreateReleaseView,
	AllReleaseView,
	CreateWholesalePriceView,
	UpdateWholesaleAndTradesView,
	ImportReleasesView,
	EditReleaseView,
	RecentlySubmittedView,
	MyReleasesView,
	UpcomingReleasesView,
	UpdateMarketingInfosView,

]