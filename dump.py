import requests
import json
from validators import validators

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
    slash = slashes.json()["slashes"]
    delegation = delegations.json()
    unbonding_delegation = unbonding_delegations.json()

    jsonData = {
        "Outstanding Rewards": outstanding,
        "Everything": everything,
        "Slashes": slash,
        "Delegations": delegation,
        "Unbonding Delegations": unbonding_delegation,
    }

    out_file = open("data.json", "a")

    json.dump(jsonData, out_file, indent=6)

    out_file.close()
