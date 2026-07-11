def match_sponsors_and_organizations(sponsors, organizations):
    """
    Matches sponsors with organizations based on certain criteria.
    
    Parameters:
    - sponsors: List of dictionaries representing sponsors.
    - organizations: List of dictionaries representing organizations.
    
    Returns:
    - A list of tuples where each tuple contains a sponsor and an organization that are matched.
    """
    matches = []
    for sponsor in sponsors:
        for organization in organizations:
            if is_match(sponsor, organization):
                matches.append((sponsor, organization))
    return matches

def is_match(sponsor, organization):
    """
    Determines if a sponsor and an organization match based on specific criteria.
    
    Parameters:
    - sponsor: Dictionary representing a sponsor.
    - organization: Dictionary representing an organization.
    
    Returns:
    - True if the sponsor and organization match, False otherwise.
    """
    # Example matching criteria
    return (sponsor['industry'] == organization['industry']) and \
           (sponsor['budget'] >= organization['expected_budget'])

# Example usage
sponsors = [
    {'name': 'Sponsor A', 'industry': 'Tech', 'budget': 10000},
    {'name': 'Sponsor B', 'industry': 'Healthcare', 'budget': 5000}
]

organizations = [
    {'name': 'Org X', 'industry': 'Tech', 'expected_budget': 8000},
    {'name': 'Org Y', 'industry': 'Education', 'expected_budget': 3000}
]

matches = match_sponsors_and_organizations(sponsors, organizations)
for sponsor, organization in matches:
    print(f"Sponsor: {sponsor['name']} matched with Organization: {organization['name']}")