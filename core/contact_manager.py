from utils import file_handler


def command(mode):
    match mode:
        case "n":
            add_contact(
            "Alice Johnson",
            phones=[
                {"type": "home", "number": "1234"},
                {"type": "work", "number": "9876"}
            ],
            emails=[
                {"type": "personal", "address": "alice@mail.com"},
                {"type": "work", "address": "alice@company.com"}
            ],
            tags=["family", "emergency"]
            )
        case "s":
            read_contacts()
        case "q":
            return "exit"
        case _:
            print(f"Wrong Operation.")
    
    return "continue"
    
def add_contact(name, phones, emails, address="", tags=None, notes=""):
    contacts = file_handler.load_contacts()
    for c in contacts:
        if c["name"].lower == name.lower():
            print(f"❌ Contact {name} already exists.")
            return
        newcontact = {
            "name":name,
            "phone":phones,
            "email":emails,
            "address":address,
            "tags":tags,
            "notes":notes
        }
        contacts.append(newcontact)
        file_handler.save_contacts(contacts)


def read_contacts():
    contacts = file_handler.load_contacts()
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
    contacts = file_handler.load_contacts()
    for c in contacts:
        if c["name"].lower() == name.lower():
            if new_phones is not None:
                c["phones"] = new_phones
            if new_emails is not None:
                c["emails"] = new_emails
            if new_tags is not None:
                c["tags"] = new_tags
            file_handler.save_contacts(contacts)
            print(f"✏️ Updated contact: {name}")
            return
    print(f"❌ Contact '{name}' not found.")

def delete_contact(name):
    contacts = file_handler.load_contacts()
    new_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    if len(new_contacts) == len(contacts):
        print(f"❌ Contact '{name}' not found.")
        return
    file_handler.save_contacts(new_contacts)
    print(f"🗑️ Deleted contact: {name}")

def search_by_tag(tag):
    """Find contacts with a specific tag."""
    contacts = file_handler.load_contacts()
    tagged = [c for c in contacts if tag.lower() in [t.lower() for t in c.get("tags", [])]]
    if not tagged:
        print(f"🔍 No contacts found with tag '{tag}'.")
        return
    print(f"\n🏷️ Contacts with tag '{tag}':")
    for c in tagged:
        print(f" - {c['name']}")

