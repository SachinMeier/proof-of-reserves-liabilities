#!/usr/bin/python3

import argparse
from calculate_river_account_key import calculate_river_account_key
from validate_liabilities import read_tree, validate_liabilities

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to validate BitMEX Proof of Liabilities"
    )
    parser.add_argument(
        "--proof",
        help="Complete filepath to BitMEX proof of liabilities file",
        required=True,
    )
    parser.add_argument("--email", type=str, required=True, help="Email address")
    parser.add_argument("--id", type=str, required=True, help="Account ID (base32 encoded)")
    parser.add_argument("--key", type=str, required=True, help="Account key (hex encoded)")
    parser.add_argument(
        "--print-proof-csv",
        action="store_true",
        help="print proof matches as comma separated list of nodes",
        default=False,
    )
    parser.add_argument(
        "--print-tree",
        action="store_true",
        help="print tree path as text: node hash, parent line number, sibling line number",
    )
    args = parser.parse_args()


if __name__ == "__main__":
    block_height, tree = read_tree(args.proof)
    account_id, account_nonce = calculate_river_account_key(args.email, args.id, args.key)
    validate_liabilities(
        block_height, tree, account_id, None, account_nonce, args
    )
