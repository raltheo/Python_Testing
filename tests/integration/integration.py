from tests.feature_display_clubs.test import test_display_clubs
from tests.buy_in_past.test import test_buying_place_past_competition
from tests.buy_more_place_available.test import test_buy_more_place_available
from tests.buy_more_than_wallet.test import test_buying_more_than_wallet
from tests.unknow_email_404.test import test_unknow_email_404
from tests.buy_more_than_12.test import test_buying_more_than_12
from tests.wallet_not_update.test import test_wallet_not_update


def test_integration(client):
    test_display_clubs(client)
    test_unknow_email_404(client)
    test_buying_place_past_competition(client)
    test_buy_more_place_available(client)
    test_buying_more_than_wallet(client)
    test_buying_more_than_12(client)
    test_wallet_not_update(client)