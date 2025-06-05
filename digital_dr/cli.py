import argparse

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Digital Dr. prototype CLI"
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("greet", help="Show project greeting")

    record_parser = subparsers.add_parser("record", help="Record a patient note")
    record_parser.add_argument("name", help="Patient name")
    record_parser.add_argument("symptoms", help="Comma-separated symptoms")

    args = parser.parse_args(argv)

    if args.command == "greet":
        print("Welcome to Digital Dr. (prototype)")
        print("This tool does not provide medical advice. Consult a professional for health concerns.")
    elif args.command == "record":
        print(f"Patient: {args.name}")
        print(f"Symptoms: {args.symptoms}")
        print("Note recorded (prototype, not saved). Always consult a qualified clinician.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
