from django.test import Client
from django.urls import reverse_lazy, reverse

from releases.factories import ReleaseFactory
from . import BaseClientTest


class UpdateMarketingInfosTest(BaseClientTest):
    def test_it_shows_marketing_infos_edit_page(self):
        release = ReleaseFactory.create(profile=self.user.profile)

        response = self.client.get(reverse("marketing_infos_edit", args=[release.id]))

        self.assertEqual(response.status_code, 200)

    def test_it_redirects_unlogged_user(self):
        release = ReleaseFactory.create(is_submitted=True)

        anonymous = Client()
        response = anonymous.get(reverse("marketing_infos_edit", args=[release.id]))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse_lazy('marketing_infos_edit', args=[release.id])}"
        )

    def test_it_forbids_editing_not_own_releases(self):
        release = ReleaseFactory.create(is_submitted=True)

        response = self.client.get(reverse("marketing_infos_edit", args=[release.id]))

        self.assertEqual(response.status_code, 403)

    def test_it_updates_the_marketing_infos(self):
        release = ReleaseFactory.create(profile=self.user.profile)
        new_style = 'Some Style'

        response = self.client.post(reverse_lazy('marketing_infos_edit', args=[release.id]), {
            "style": new_style,
        })

        release.refresh_from_db()

        self.assertEqual(release.marketinginfos.style, new_style)
        self.assertRedirects(response, reverse('marketing_infos_edit', args=[release.id]))
