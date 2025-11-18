from utils.file_handler import load_contacts, save_contacts


def command(mode):
    match mode.lower():
        # ADD CONTACT
        case "n":
            print("\n➕ Add New Contact")
            name = input("Name: ").strip()

            # Phones
            phones = []
            while True:
                t = input("Phone type (home/work/personal) or Enter to stop: ").strip()
                if not t:
                    break
                num = input("Phone number: ").strip()
                phones.append({"type": t, "number": num})

            # Emails
            emails = []
            while True:
                t = input("Email type (work/personal) or Enter to stop: ").strip()
                if not t:
                    break
                addr = input("Email address: ").strip()
                emails.append({"type": t, "address": addr})

            address = input("Address (optional): ").strip()
            tags = input("Tags (comma-separated): ").strip()
            tags = [t.strip() for t in tags.split(",")] if tags else []
            notes = input("Notes: ").strip()

            add_contact(
                name=name,
                phones=phones,
                emails=emails,
                address=address,
                tags=tags,
                notes=notes
            )
            print("✔️ Contact added.")
        
        # -------------------------
        # SHOW ALL CONTACTS
        # -------------------------
        case "s":
            read_contacts()

        # -------------------------
        # UPDATE CONTACT
        # -------------------------
        case "u":
            print("\n✏️ Update Contact")
            name = input("Enter contact name to update: ").strip()

            print("\nLeave blank to skip updating that field.\n")

            # Phones
            new_phones = None
            if input("Update phones? (y/n): ").lower() == "y":
                new_phones = []
                while True:
                    t = input("Phone type or Enter to stop: ").strip()
                    if not t:
                        break
                    num = input("Phone number: ").strip()
                    new_phones.append({"type": t, "number": num})

            # Emails
            new_emails = None
            if input("Update emails? (y/n): ").lower() == "y":
                new_emails = []
                while True:
                    t = input("Email type or Enter to stop: ").strip()
                    if not t:
                        break
                    addr = input("Email address: ").strip()
                    new_emails.append({"type": t, "address": addr})

            # Tags
            new_tags = None
            if input("Update tags? (y/n): ").lower() == "y":
                t = input("Enter new tags (comma-separated): ").strip()
                new_tags = [i.strip() for i in t.split(",")] if t else []

            update_contact(name, new_phones, new_emails, new_tags)

        # -------------------------
        # DELETE CONTACT
        # -------------------------
        case "d":
            print("\n🗑️ Delete Contact")
            name = input("Enter name to delete: ").strip()
            delete_contact(name)

        # -------------------------
        # SEARCH CONTACT BY TAG
        # -------------------------
        case "t":
            tag = input("Enter tag to search: ").strip()
            search_by_tag(tag)

        # -------------------------
        # QUIT PROGRAM
        # -------------------------
        case "q":
            return "exit"

        # -------------------------
        # INVALID OPTION
        # -------------------------
        case _:
            print("❌ Wrong Operation.")
    
    return "continue"

    
def add_contact(name, phones=None, emails=None, address="", tags=None, notes=""):
    phones = phones or []
    emails = emails or []
    tags = tags or []
    contacts = load_contacts()
    
    for c in contacts:
        if c["name"].lower() == name.lower():
            print(f"❌ Contact {name} already exists.")
            return
    newcontact = {
            "name":name,
            "phones":phones,
            "emails":emails,
            "address":address,
            "tags":tags,
            "notes":notes
    }
    contacts.append(newcontact)
    save_contacts(contacts)
    

def read_contacts():
    contacts = load_contacts()
    if not contacts:
        print("Not Contacts Found. ")
        return
    print("\n📒 Contact List:")
    for c in contacts:
        print(f"\n👤 {c['name']}")
        for p in c.get("phones", []):
            print(f"  📞 {p['type'].capitalize()}: {p['number']}")
        for e in c.get("emails", []):
            print(f"  📧 {e['type'].capitalize()}: {e['address']}")
        if c.get("tags"):
            print(f"  🏷️ Tags: {', '.join(c['tags'])}")


def update_contact(name, new_phones=None, new_emails=None, new_tags=None):
    contacts = load_contacts()
    for c in contacts:
        if c["name"].lower() == name.lower():
            if new_phones is not None:
                c["phones"] = new_phones
            if new_emails is not None:
                c["emails"] = new_emails
            if new_tags is not None:
                c["tags"] = new_tags
            save_contacts(contacts)
            print(f"✏️ Updated contact: {name}")
            return
    print(f"❌ Contact '{name}' not found.")


def delete_contact(name):
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    if len(new_contacts) == len(contacts):
        print(f"❌ Contact '{name}' not found.")
        return
    save_contacts(new_contacts)
    print(f"🗑️ Deleted contact: {name}")


def search_by_tag(tag):
    """Find contacts with a specific tag."""
    contacts = load_contacts()
    tagged = [c for c in contacts if tag.lower() in [t.lower() for t in c.get("tags", [])]]
    if not tagged:
        print(f"🔍 No contacts found with tag '{tag}'.")
        return
    print(f"\n🏷️ Contacts with tag '{tag}':")
    for c in tagged:
        print(f" - {c['name']}")

