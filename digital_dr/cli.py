import argparse

from tabulate import tabulate

from . import db


def _format_records(records: list[dict]) -> str:
    if not records:
        return "No records found."

    table = [
        [record["id"], record["name"], record["symptoms"], record["timestamp"]]
        for record in records
    ]
    return tabulate(
        table,
        headers=["ID", "Name", "Symptoms", "Timestamp"],
        tablefmt="github",
    )


def main(argv=None):
    db.init_db()

    parser = argparse.ArgumentParser(description="Digital Dr. prototype CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("greet", help="Show project greeting")

    record_parser = subparsers.add_parser("record", help="Record a patient note")
    record_parser.add_argument("name", help="Patient name")
    record_parser.add_argument("symptoms", help="Comma-separated symptoms")

    subparsers.add_parser("list", help="List recorded patient notes")

    args = parser.parse_args(argv)

    if args.command == "greet":
        print("Welcome to Digital Dr. (prototype)")
        print(
            "This tool does not provide medical advice. Consult a professional for health concerns."
        )
    elif args.command == "record":
        saved = db.save_note(args.name, args.symptoms)
        print(f"Saved note for {saved['name']} with ID {saved['id']}.")
        print(f"Symptoms: {saved['symptoms']}")
        print(f"Timestamp: {saved['timestamp']}")
        print("Always consult a qualified clinician.")
    elif args.command == "list":
        records = db.list_notes()
        print(_format_records(records))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
