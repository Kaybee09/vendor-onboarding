from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def vendor_form():
    return render_template("vendor_form.html")

    if request.method == "POST":
        # Company Information
        company_name = request.form.get("company_name")
        registration_number = request.form.get("registration_number")
        vat_number = request.form.get("vat_number")
        country = request.form.get("country")
        address = request.form.get("address")
        website = request.form.get("website")

        # Contact Information
        primary_contact_name = request.form.get("primary_contact_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        finance_contact = request.form.get("finance_contact")
        legal_contact = request.form.get("legal_contact")

        # Banking Information
        bank_name = request.form.get("bank_name")
        account_name = request.form.get("account_name")
        iban = request.form.get("iban")
        swift = request.form.get("swift")
        currency = request.form.get("currency")

        # Compliance Information
        anti_bribery = request.form.get("anti_bribery")
        iso_certification = request.form.get("iso_certification")
        
                # Validation
        if not company_name:
            errors["company_name"] = "Company name is required"

        if not registration_number:
            errors["registration_number"] = "Registration number is required"

        if not country:
            errors["country"] = "Country is required"

        if not address:
            errors["address"] = "Address is required"

        if not primary_contact_name:
            errors["primary_contact_name"] = "Primary contact name is required"

        if not email:
            errors["email"] = "Email is required"

        if not phone:
            errors["phone"] = "Phone number is required"

        if not bank_name:
            errors["bank_name"] = "Bank name is required"

        if not account_name:
            errors["account_name"] = "Account name is required"

        if not iban:
            errors["iban"] = "IBAN/Account number is required"

        if not currency:
            errors["currency"] = "Currency is required"
        
        # If no validation errors
        if len(errors) == 0:
            print("\n===== Vendor Submission =====")

            print("\n--- Company Information ---")
            print(f"Company Name: {company_name}")
            print(f"Registration Number: {registration_number}")
            print(f"VAT Number: {vat_number}")
            print(f"Country: {country}")
            print(f"Address: {address}")
            print(f"Website: {website}")

            print("\n--- Contact Information ---")
            print(f"Primary Contact: {primary_contact_name}")
            print(f"Email: {email}")
            print(f"Phone: {phone}")
            print(f"Finance Contact: {finance_contact}")
            print(f"Legal Contact: {legal_contact}")

            print("\n--- Banking Information ---")
            print(f"Bank Name: {bank_name}")
            print(f"Account Name: {account_name}")
            print(f"IBAN: {iban}")
            print(f"SWIFT: {swift}")
            print(f"Currency: {currency}")

            print("\n--- Compliance Information ---")
            print(f"Anti-Bribery Accepted: {anti_bribery}")
            print(f"ISO Certification: {iso_certification}")

            print("\n==============================")

            return "Vendor form submitted successfully! Check terminal output."

    return render_template("vendor_form.html", errors=errors)


if __name__ == "__main__":
    app.run(debug=True)