def extract_doi_and_page_range(text):
    parts = text.split()
    page_range = None
    doi = None

    for i, part in enumerate(parts):
        print(f"Part {i}: {part}")

        if '-' in part and part.replace('-', '').replace('.', '').isdigit():
            page_range = part.rstrip('.,')

        if part.lower().startswith('doi:'):
            doi = part.split(':', 1)[1]
            if i + 1 < len(parts):
                doi += parts[i + 1]

    return {
        "Page Range": page_range,
        "DOI": doi
    }


# Example usage
text = "2024, 55(5): 2273-2280. doi:10.11843/j.issn.0366-6964.2024.05.045"
text = "2024, 27(24): 2941-2953. DOI: 10.12114/j.issn.1007-9572.2024.0030"
text2 = "2024, 27(24): 2954-2960. DOI: 10.12114/j.issn.1007-9572.2023.0793"
details = extract_doi_and_page_range(text)
if details:
    print("Page Range:", details["Page Range"])
    print("DOI:", details["DOI"])
else:
    print("No match found")
