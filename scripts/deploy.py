from brownie import FundMe, MockV3Aggregator, config, network
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()

    print(account)

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed = config["networks"]["rinkeby"]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed, {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify")
    )
    print(f"Contract address is {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
