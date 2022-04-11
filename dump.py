import requests
import json
from validators import validators

# validator = "junovaloper196ax4vc0lwpxndu9dyhvca7jhxp70rmcqcnylw"


d = [
    "junovaloper196ax4vc0lwpxndu9dyhvca7jhxp70rmcqcnylw",
    "junovaloper1t8ehvswxjfn3ejzkjtntcyrqwvmvuknzmvtaaa",
    "junovaloper1afhtjur8js4589xymu346ca7a5y5293x7p64ca",
]

for validator in validators:

    r1 = requests.get(
        f"https://api.juno.omniflix.co/cosmos/staking/v1beta1/validators/{validator}"
    )
    outstanding_rewards = requests.get(
        f"https://api.juno.omniflix.co/cosmos/distribution/v1beta1/validators/{validator}/outstanding_rewards"
    )
    slashes = requests.get(
        f"https://api.juno.omniflix.co/cosmos/distribution/v1beta1/validators/{validator}/slashes"
    )
    delegations = requests.get(
        f"https://api.juno.omniflix.co/cosmos/staking/v1beta1/validators/{validator}/delegations"
    )
    unbonding_delegations = requests.get(
        f"https://api.juno.omniflix.co/cosmos/staking/v1beta1/validators/{validator}/unbonding_delegations"
    )

    outstanding = outstanding_rewards.json()["rewards"]
    everything = r1.json()
    # name = r1.json()["validator"]["description"]["moniker"]
    # commission = r1.json()["validator"]["commission"]["commission_rates"]["rate"]
    # unbonding_height = r1.json()["validator"]["unbonding_height"]
    slash = slashes.json()["slashes"]
    delegation = delegations.json()
    unbonding_delegation = unbonding_delegations.json()

    jsonData = {
        "Outstanding Rewards": outstanding,
        "Everything": everything,
        # "Validator": name,
        # "Commission": commission,
        # "Unbonding Height": unbonding_height,
        "Slashes": slash,
        "Delegations": delegation,
        "Unbonding Delegations": unbonding_delegation,
    }

    out_file = open("data.json", "a")

    json.dump(jsonData, out_file, indent=6)

    out_file.close()
