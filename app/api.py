from flask import Flask, request, jsonify
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount

app = Flask(__name__)
registry = AccountRegistry()


@app.route("/api/accounts", methods=["POST"])
def create_account():
    print("Create new account request received")
    data = request.get_json()
    print(f"Create account request: {data}")
    account = PersonalAccount(data["first_name"], data["last_name"], data["pesel"])
    registry.add_account(account)
    return jsonify({"message": "Account created"}), 201


@app.route("/api/accounts", methods=["GET"])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.get_all_accounts()
    accounts_data = [
        {
            "first_name": acc.first_name,
            "last_name": acc.last_name,
            "pesel": acc.pesel,
            "balance": acc.balance,
        }
        for acc in accounts
    ]
    return jsonify(accounts_data), 200


@app.route("/api/accounts/count", methods=["GET"])
def get_account_count():
    print("Get account count request received")
    count = registry.get_number_of_accounts()
    return jsonify({"count": count}), 200


@app.route("/api/accounts/<pesel>", methods=["GET"])
def get_account_by_pesel(pesel):
    print("Get account by pesel request received")
    account = registry.get_account_by_pesel(pesel)
    if not account:
        return jsonify({"error": "Account not found"}), 404
    return (
        jsonify({"first_name": account.first_name, "last_name": account.last_name}),
        200,
    )


@app.route("/api/accounts/<pesel>", methods=["PATCH"])
def update_account(pesel):
    print("Update account request received")
    account = registry.get_account_by_pesel(pesel)
    if not account:
        return jsonify({"error": "Account not found"}), 404
    data = request.get_json()
    if data["first_name"]:
        account.first_name = data["first_name"]
    if data["last_name"]:
        account.last_name = data["last_name"]
    return jsonify({"message": "Account updated"}), 200


@app.route("/api/accounts/<pesel>", methods=["DELETE"])
def delete_account(pesel):
    print("Delete account request received")
    if not registry.get_account_by_pesel(pesel):
        return jsonify({"error": "Account not found"}), 404
    registry.delete_account(pesel)
    return jsonify({"message": "Account deleted"}), 200
