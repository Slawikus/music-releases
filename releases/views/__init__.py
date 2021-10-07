from .submit_release_view import SubmitReleaseView
from .create_release_view import CreateReleaseView
from .all_release_view import AllReleaseView
from .create_wholesale_price_view import CreateWholesalePriceView
from .import_releases_view import ImportReleasesView
from .edit_release_view import EditReleaseView
from .recently_submitted_view import RecentlySubmittedView
from .my_releases_view import MyReleasesView
from .upcoming_releases_view import UpcomingReleasesView
from .update_marketing_infos_view import UpdateMarketingInfosView
from .delete_wholesale_price_view import DeleteWholesalePriceView
from .base_release import BaseRelease
from .update_trades_info_view import UpdateReleaseTradesInfoView
from .update_wholesale_info_view import UpdateReleaseWholesaleInfoView
from .release_detail_view import ReleaseDetailView

__all__ = [
    BaseRelease,
    SubmitReleaseView,
    CreateReleaseView,
    AllReleaseView,
    CreateWholesalePriceView,
    UpdateReleaseTradesInfoView,
    UpdateReleaseWholesaleInfoView,
    ImportReleasesView,
    EditReleaseView,
    RecentlySubmittedView,
    MyReleasesView,
    UpcomingReleasesView,
    UpdateMarketingInfosView,

]
