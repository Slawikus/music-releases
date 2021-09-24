from .combined_form_base import CombinedFormBase
from .custom_user_creation_form import CustomUserCreationForm
from .edit_profile_form import EditProfileForm


class CombinedUserProfileCreationForm(CombinedFormBase):
	form_classes = [CustomUserCreationForm, EditProfileForm]