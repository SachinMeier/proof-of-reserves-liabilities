#!/usr/bin/python3

import argparse
import hashlib
import hmac
import struct
import base64

def calculate_river_account_key(email, account_id, account_key):
	account_key_bytes = bytes.fromhex(account_key)
	# This encodes the email to a utf-8 byte array
	email_bytes = email.encode('utf-8')
	# first, decode the account_id from base32 to bytes
	account_id_bytes = base64.b32decode(account_id)
	# Convert the account_id bytes to int
	account_id_int = int.from_bytes(account_id_bytes, byteorder='big')

	# Convert the account_id int to 8byte little endian
	account_id_bytes = struct.pack('<Q', account_id_int)

	# hash the account_key, email, and account_id to get the account subkey (used as account_nonce in BitMEX implementation)
	combined_bytes = account_key_bytes + email_bytes + account_id_bytes
	sha256 = hashlib.sha256()
	sha256.update(combined_bytes)
	return account_id_int, sha256.hexdigest()


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Calculate River account key")
	parser.add_argument("--email", type=str, required=True, help="Email address")
	parser.add_argument("--id", type=str, required=True, help="Account ID (base32 encoded)")
	parser.add_argument("--key", type=str, required=True, help="Account key (hex encoded)")
	args = parser.parse_args()

	account_id, account_key = calculate_river_account_key(args.email, args.id, args.key)
	print(f"Account ID: {account_id}")
	print(f"Account key: {account_key}")