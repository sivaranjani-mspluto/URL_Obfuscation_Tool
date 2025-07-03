
import urllib.parse
import base64

def obfuscate_url(url):
    print("\n🔐 Obfuscation Options:")
    print("1. URL Encoding")
    print("2. Base64 Encoding")
    choice = input("Choose a method (1 or 2): ")

    if choice == '1':
        obfuscated = urllib.parse.quote(url)
        print(f"🔗 Obfuscated URL (URL Encoded): {obfuscated}")
    elif choice == '2':
        obfuscated = base64.urlsafe_b64encode(url.encode()).decode()
        print(f"🔗 Obfuscated URL (Base64): {obfuscated}")
    else:
        print("❌ Invalid choice.")

def deobfuscate_url(obf_url):
    print("\n🔓 Deobfuscation Options:")
    print("1. URL Decoding")
    print("2. Base64 Decoding")
    choice = input("Choose a method (1 or 2): ")

    try:
        if choice == '1':
            original = urllib.parse.unquote(obf_url)
            print(f"✅ Deobfuscated URL: {original}")
        elif choice == '2':
            original = base64.urlsafe_b64decode(obf_url).decode()
            print(f"✅ Deobfuscated URL: {original}")
        else:
            print("❌ Invalid choice.")
    except Exception as e:
        print(f"❌ Error decoding: {e}")

if __name__ == "__main__":
    print("🌐 URL Obfuscation and Deobfuscation Tool")
    print("1. Obfuscate URL")
    print("2. Deobfuscate URL")
    option = input("Choose an option (1 or 2): ")

    if option == '1':
        url = input("Enter the URL to obfuscate: ")
        obfuscate_url(url)
    elif option == '2':
        url = input("Enter the obfuscated URL: ")
        deobfuscate_url(url)
    else:
        print("❌ Invalid option.")
